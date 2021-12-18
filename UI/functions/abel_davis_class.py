import numpy as np
import matplotlib.pyplot as plt
from abel.tools import polar
from scipy.special import eval_legendre, hyp2f1
from scipy.interpolate import interp1d
from math import factorial
import time
import h5py
import os
class Abel_object():
    def __init__(self, data, center_rows, center_cols, d_alpha_deg, dr, N, Rmax, parent=None):
        """
            Creates an object that can Abel invert an image using the DAVIS
            (Direct Algorithm for Velocity-map Imaging) technique described in
            https://doi.org/10.1063/1.5025057

            Parameters
            ----------
            data : 2D np.array
                The data to invert
            center_rows : int
                Row coordinate of the center of the image, corresponds to the symmetry axis (polarization/propagation)
            center_cols : int
                Col coordinate of the center of the image, correspond to the other axis
            d_alpha_deg : float
                Angular coordinate spacing (in degrees)
            dr : int
                Radial coordinate spacing for the inverted array
            N : int
                number of photons. Determines the number of legendre polynomials
                to use (which is equal to 2N+1)
                ex: if N=1 then P0, P1 and P2 are used, if N=2 then P0 to P4 are used.
            Rmax : int
                maximum radius up to which the image is inverted
        """

        self.parent = parent

        self.center_rows = center_rows
        self.center_cols = center_cols
        self.d_alpha_deg = d_alpha_deg
        self.d_alpha = d_alpha_deg * np.pi / 180  # deg to rad conversion
        self.dr = dr
        self.N = N
        self.Rmax = Rmax

        self.Ny, self.Nx = data.shape

        self.N_alpha = int(2 * np.pi / self.d_alpha)
        self.N_R = int(Rmax/dr)

        self.R_vector = np.linspace(dr, Rmax, self.N_R)
        self.alpha_vector = np.linspace(2 * np.pi / self.N_alpha, 2 * np.pi, self.N_alpha)

        self.data_polar, r_grid, theta_grid = polar.reproject_image_into_polar(
            data, origin=(center_rows, center_cols), dr=dr, dt=self.d_alpha, Jacobian=True)
        self.alpha_vector = theta_grid[0,:]
        self.M_temp_dic = {}
        self.F = {}
        self.beta ={}

    def set_data(self, data):
        if data.shape != (self.Ny, self.Nx):
            print('Incorrect data shape')
            raise ValueError
        self.data_polar, r_grid, theta_grid = polar.reproject_image_into_polar(
            data, origin=(self.center_rows, self.center_cols), dr=self.dr, dt=self.d_alpha, Jacobian=True)

    def show(self, data):
        plt.figure()
        g = plt.imshow(data, cmap='jet', origin='lower')
        plt.colorbar(g)
        plt.show()

    def falling_factorial(self, x, m):
        prod = 1
        for i in range(int(m)):
            prod *= (x-i)
        return prod

    def summand_cnkl(self, n,k,l,p):
        ''' this function is used by the c function'''
        return self.falling_factorial(2*(n-2*k+l-p),2*(l-p))/\
                    self.falling_factorial(2*(l-p),2*(l-p))*self.c(n,k-l+p,p)

    def c(self, n,k,l):
        ''' This function is defined in eqn. 7 and used in the Gamma function
         to calculate the transformation matrices Mn,n-2k'''
        c = self.falling_factorial(n-k+l-1/2,k-l)*self.falling_factorial(n-k,l)*\
            self.falling_factorial(n-2*k+2*l-1/2,2*l)/(self.falling_factorial(2*l,2*l)*\
                                                       self.falling_factorial(n-k+l-1/2,l))
        if l>0:
            c = c - 1/(2**(k+l))*np.array([self.summand_cnkl(n,k,l,p) for p in range(0,l)]).sum()
        return c

    def Gammma(self,n,k,l,i,ip):
        ''' This function is defined in eqn. 11 and used to calculate the transformation matrices Mn,n-2k '''
        step = dr / 2
        R_minus = self.R_vector[i] - step
        R_plus = self.R_vector[i] + step
        if ip==i:
            R_plus -= step # this is a trick of mine, otherwise R_plus/R_vector[ip] > 1
            # and the hypergeometric function in eqn. 11 is not defined
        try:
            Gamma = 1/(2+2*l-2*k+n)*\
                  (((R_plus)/self.R_vector[ip])**(2+2*l-2*k+n)*\
                   hyp2f1(1/2+l-k,1+l-k+n/2,2+l-k+n/2,(R_plus/self.R_vector[ip])**2)\
                - ((R_minus)/self.R_vector[ip])**(2+2*l-2*k+n)*\
                   hyp2f1(1/2+l-k,1+l-k+n/2,2+l-k+n/2,(R_minus/self.R_vector[ip])**2))
            return Gamma
                # I replaced R_vector[i]+dr/2 by R_vector[i]
        except ZeroDivisionError:
            print('ZeroDivisionError in Gamma function')

    def M_eq13(self,N_R, n, k): # from equation 13
        ''' This function calculates the upper triangular transformation matrices Mn,n-2k using the formula of eqn. 13
        It uses the functions Gamma and c. It is not currently used but I thought it could be useful for n>4'''
        sM = np.zeros((N_R,N_R))
        for i in range (0, N_R):
            for ip in range(i, N_R):
                sM[i,ip] = np.array([(-1)**(k-l)*2**(2*l+1)/factorial(k-l)*self.c(n,k,l)*self.dr*self.d_alpha* \
                                        self.Gammma(n,k,l,i,ip) for l in range(0,max(k-1,0)+1)]).sum()
        for l in range(0,max(k-1,0)+1):
            print((-1)**(k-l)*2**(2*l+1)/factorial(k-l)*self.c(n,k,l))
        return sM

    def M(self):
            ''' This function calculates the upper triangular transformation matrices Mn,n-2k using the analytical formulas
            from Table I. It stores in a dictionnary the Mn,n-2k for k != 0 and Mn,n^-1 otherwise. 
            I checked that it's equal to M_eqn13(N_R,n,k). However it's faster than M_eq13 so this is the function
            actually used '''
            dr_over2 = self.dr/2
            coeff = self.dr*self.d_alpha
            # Initialize dictionnary
            for n in range(2 * self.N, -1, -1):  # reversed loop from 2N to 0 included
                N_threshold = self.N - ((n+1) // 2) #Threshold for entering the sum in equation 19 if smaller than N        
                for k in np.arange(N_threshold,-1,-1):  #Going backwards since range function in Python is a real pain  
                    self.M_temp_dic[(n+2*k,k)] = np.zeros((self.N_R,self.N_R))

            # Loop along each radius
            for i in range(0,self.N_R):                
                R_ip = self.R_vector[i:self.N_R]
                R_minus = R_ip[0] - dr_over2 # Ri v = Ri - DeltaR/2
                R_plus = R_ip[0] + dr_over2 # Ri v = Ri - DeltaR/2
                R_plus_frac = R_plus/R_ip  # Ri ^ / Ri
                R_plus_frac[0] = 1  # Force first value to be 1 to keep the square root + arcsin well defined
                R_minus_frac = R_minus/R_ip # Ri v  / Ri 
                sqrtR_plus = np.sqrt(1-(R_plus_frac)**2) # (1 - (Ri ^  / Ri)^2)^1/2
                sqrtR_minus = np.sqrt(1-(R_minus_frac)**2) # (1 - (Ri v  / Ri)^2)^1/2
                asin_Rdiff =  np.arcsin(R_plus_frac) - np.arcsin(R_minus_frac) # asin(Ri ^ / Ri) - asin(Ri v / Ri)

                for m in range(2 * self.N, -1, -1):  # reversed loop from 2N to 0 included
                    N_threshold = self.N - ((m+1) // 2) #Threshold for entering the sum in equation 19 if smaller than N
                    for k in np.arange(N_threshold,-1,-1):  #Going backwards since range function in Python is a real pain 
                        n = m + 2 * k 
                        if(n==0 and k==0): # M00
                            M_temp = 2*coeff*(sqrtR_minus-sqrtR_plus)
                        elif(n==1 and k==0): # M11                 
                            M_temp = coeff*\
                                    (R_minus_frac*sqrtR_minus-R_plus_frac*sqrtR_plus+asin_Rdiff)
                        elif(n==2 and k==0): # M22
                            M_temp = 2*coeff/3*\
                                    (sqrtR_minus*(2+R_minus_frac**2)-sqrtR_plus*(2+R_plus_frac**2))
                        elif(n==2 and k==1): # M20
                            M_temp = coeff/3*(sqrtR_plus**3-sqrtR_minus**3)
                        elif(n==3 and k==0): # M33
                            M_temp = coeff/4*\
                                    (R_minus_frac*sqrtR_minus*(3+2*R_minus_frac**2)
                                        -R_plus_frac*sqrtR_plus*(3+2*R_plus_frac**2)\
                                        +3*asin_Rdiff)
                        elif(n==3 and k==1): # M31
                            M_temp = 3*coeff/8*\
                                    (R_minus_frac*sqrtR_minus*(-1+2*R_minus_frac**2)\
                                        -R_plus_frac*sqrtR_plus*(-1+2*R_plus_frac**2)\
                                        -asin_Rdiff)                        
                        elif(n==4 and k==0): # M44
                            M_temp = 2*coeff/15*\
                                    (sqrtR_minus*(8+4*R_minus_frac**2+3*R_minus_frac**4)\
                                        -sqrtR_plus*(8+4*R_plus_frac**2+3*R_plus_frac**4))
                        elif(n==4 and k==1): # M42
                            M_temp = coeff/3*\
                                    (sqrtR_plus**3*(2+3*R_plus_frac**2)\
                                        -sqrtR_minus**3*(2+3*R_minus_frac**2))
                        elif(n==4 and k==2): # M40 (error in the article)
                            M_temp = coeff/(60)*\
                                    (sqrtR_plus**3*(19+51*R_plus_frac**2)\
                                        -sqrtR_minus**3*(19+51*R_minus_frac**2))
                        elif(n==5 and k==0): # M55
                            M_temp = coeff/24*\
                                    (sqrtR_minus*R_minus_frac*(15+10*R_minus_frac**2+8*R_minus_frac**4)\
                                        -sqrtR_plus*R_plus_frac*(15+10*R_plus_frac**2+8*R_plus_frac**4)\
                                        +15*asin_Rdiff)                                         
                        elif(n==5 and k==1): # M53
                            M_temp = 7*coeff/48*\
                                    (sqrtR_minus*R_minus_frac*(-3-2*R_minus_frac**2+8*R_minus_frac**4)\
                                        -sqrtR_plus*R_plus_frac*(-3-2*R_plus_frac**2+8*R_plus_frac**4)\
                                        -3*asin_Rdiff)        
                        elif(n==5 and k==2): # M51
                            M_temp = coeff/64*\
                                    (sqrtR_minus*R_minus_frac*(-81-134*R_minus_frac**2+296*R_minus_frac**4)\
                                        -sqrtR_plus*R_plus_frac*(-81-134*R_plus_frac**2+296*R_plus_frac**4)\
                                        -81*asin_Rdiff)     
                        elif(n==6 and k==0): # M66 (not in the article)
                            M_temp = 2*coeff/35*\
                                    (sqrtR_minus*(16+8*R_minus_frac**2+6*R_minus_frac**4+5*R_minus_frac**6)\
                                        -sqrtR_plus*(16+8*R_plus_frac**2+6*R_plus_frac**4+5*R_plus_frac**6))                                     
                        elif(n==6 and k==1): # M64 (not in the article)
                            M_temp = coeff/35*\
                                    (sqrtR_plus**3*(24+36*R_plus_frac**2+45*R_plus_frac**4)\
                                        -sqrtR_minus**3*(24+36*R_minus_frac**2+45*R_minus_frac**4))
                        elif(n==6 and k==2): # M62 (not in the article)
                            M_temp = coeff/84*\
                                        (sqrtR_plus**3*(422 + 633*R_plus_frac**2 + 975*R_plus_frac**4)\
                                        -sqrtR_minus**3*(422 + 633*R_minus_frac**2 + 975*R_minus_frac**4))
                        elif(n==6 and k==3): # M60 (not in the article)                     
                            M_temp = coeff/1680*\
                                    (sqrtR_plus**3*(-536 - 1329*R_plus_frac**2 + 2670*R_plus_frac**4)
                                    -sqrtR_minus**3*(-536 - 1329*R_minus_frac**2 + 2670*R_minus_frac**4))
                        else: #Take the numerical solution otherwise
                            for ip in range(i,self.N_R):
                                M_temp = np.array([self.C(n,k,l)*self.dr*self.d_alpha* \
                                                    self.Gammma(n,k,l,i,ip) for l in range(0,max(k-1,0)+1)]).sum()                                                    
                        self.M_temp_dic[(n,k)][i,i:self.N_R] = M_temp
                if not(np.mod(i,self.N_R/10)):
                    print(i / self.N_R * 100, " %")                    
            print(100, " %")     
            # Transformation of the diagonal value of the dictionnary to store the inverse of M_nn               
            for n in range(2 * self.N, -1, -1):  # reversed loop from 2N to 0 included
                self.M_temp_dic[(n,0)] = np.linalg.inv(self.M_temp_dic[(n,0)])  # inverse of M_nn

    def precalculate(self):
        filename = 'dr_' + (str(self.dr) + '_da_' + '{:.2f}'.format(self.d_alpha_deg) + '_N_' + \
                            str(self.N) + '_center_rows_' + \
                            str(self.center_rows) + '_cols_' + str(self.center_cols) + \
                            '_Rmax_' + str(self.Rmax)).replace('.','p') + '.npy'
        print(filename)
        if os.path.isfile('M_dic_'+filename):
        # if None:
            print('matrices already precalculated, loading them...')
            self.M_temp_dic = np.load('M_dic_'+filename, allow_pickle='TRUE').item()
        else:
            print('precalculating matrices...')
            self.M()            
            print('precalculation done, saving matrices as ', filename)
            np.save('M_dic_' + filename, self.M_temp_dic)

    def invert(self):         
        # Note (Constant): I removed the definition from Dominique who was first storing the delta_k
        # and then using them to calculate the matrice element.
        # Since we go from high k to low k, we can only load and work with
        # only one at a time avoiding unecessary storing and loops.
        Th_dist = self.data_polar[np.arange(0,self.N_R), :] #Theta distribution for all radius
        sTh = np.abs(np.sin(self.alpha_vector)) # Absolute value of sin(theta)
        cTh = np.cos(self.alpha_vector) # cos(theta)
        for n in range(2 * self.N, -1, -1):  # reversed loop from 2N to 0 included
            # Application of eqn. 16
            delta_corr = (2 * n + 1) / 2 * np.trapz(sTh*eval_legendre(n, cTh)*Th_dist,dx=self.d_alpha) #Calculate delta
            # Right side of eqn.19
            N_threshold = self.N - ((n+1) // 2) # Threshold for entering the sum in equation 19 if smaller than N                            
            if N_threshold: # Check if there is a need to enter into the sum
                # Update values of delta
                delta_corr -= np.array([np.dot(self.M_temp_dic[(n+2*k,k)], self.F[n+2*k]) \
                for k in range(N_threshold,0,-1)]).sum(axis=0)  # Going backwards since range function in Python is a real pain       
            # Application of eqn. 19                            
            self.F[n] = np.dot(self.M_temp_dic[(n,0)],delta_corr)

    def calculate_beta(self):
        for k in range(2 * self.N, -1, -1):
            self.beta[k] = self.F[k]/self.F[0]

    def make_inverse_image(self,L,Nmax = 3,even = 0):       
        if np.mod(L,2):
            L = L + 1     
        X_vect = np.arange(-L/2,L/2)
        Y_vect = np.arange(-L/2,L/2)
        S = np.zeros([L**2]) #Image
        R = np.sqrt(X_vect**2+Y_vect[:,np.newaxis]**2).flatten()
        cosTh = np.cos(np.arctan2(X_vect,Y_vect[:,np.newaxis])).flatten()
        mask = np.logical_and(R>0, R<self.Rmax)
        cosTh = cosTh[mask]
        R = R[mask]
        beta_range = np.arange(2*Nmax)
        if even:
            beta_range = beta_range[np.array(np.mod(beta_range,2),dtype = bool) == False] #Thats way too long for something so simple...
        for i in beta_range:
            h = interp1d(self.R_vector, abel_obj.F[i]) 
            S[mask] += h(R)*eval_legendre(i,cosTh) 
        return S.reshape([L,L])

if __name__ == '__main__':

    path = 'Q:\LIDyL\Atto\ATTOLAB\SE1\Data_Experiments\SE1_2021\\2021-02-15\\'
    filename='Ar-He_PE_Vrep1p0_Vext_0p794_MCP700+300_PMCP2p6em5_7p1em6_avg100_WITHfilter_WITHdrilled_WITHSB_2p3W_better.npy'    
    # data = np.load(path+filename)

    filename = 'D:\\Work\\Saclay\\Git\\analysis_GUI_Qt\\Dataset_20210423_003.h5'   
    scan = '000'  # vérifier dans hdfview
    path2 = ''.join(['Scan',scan,'/Detector000/Data2D/Ch000/Data'])
    with h5py.File(filename, 'r') as file:                          
        raw_datas = file['Raw_datas']   
        data = np.asarray(raw_datas[path2][0])

    ############# INPUT PARAMETERS ##########################################
    transpose = False
    remove_bkg = False
    # Image orientation:  “television” convention, where IM[0, 0] refers to the upper left corner of the image. 
    # This definition might not be consistent with the older definition of pyabel
    center_x = 1012 # Horizontal axis (COL)
    center_y = 1037 # Vertical axis (ROW)
    #Check ouput of abel.tools.center functions to test:
    #  abel.tools.center.center_image(data)

    d_alpha_deg = 0.1  # increment in angle alpha (in degrees)
    dr = 1  # increment in radius r
    N = 3  # number of photons. Determines the number of legendre polynomials to use (which is equal to 2N+1)
    # ex: if N=1 then P0, P1 and P2 are used. If N=2 then P0 to P4 are used.
    Rmax = 1000  # maximum radius up to which the image is inverted
    #########################################################################
    if transpose:
        data = np.transpose(data)
    data = data / np.sum(np.sum(data))        

    abel_obj = Abel_object(data, center_y, center_x, d_alpha_deg, dr, N, Rmax)    
    # abel_obj.show(data)
    abel_obj.precalculate()
    t = 0
    L = 10
    for i in range(L):
        t_init = time.time()
        abel_obj.invert()
        t += time.time()-t_init        
    print(t/L)
    # abel_obj.invert()

    fig = plt.figure(num=None, figsize=(9, 4.5), dpi=100, tight_layout=True)
    ax = plt.subplot(1,1,1)

    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(12)
    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(12)
    ax.set_xlabel("Radius (pixels)", fontsize=14)
    ax.set_ylabel("Intensity (arb. u.)", fontsize=14)
    for i in range(len(abel_obj.F)):
        ax.plot(abel_obj.F[i], label=f'P{i}')

    plt.legend()
    plt.show()


    L = 2048
    reconstr = True
    if reconstr:

        S_inv = abel_obj.make_inverse_image(L,3,0)
        fig_im, axs_im = plt.subplots(2, 1,sharex= True,sharey='col')  
        # plt.imshow(Sinv, origin='lower', cmap='jet')
        axs_im[0].imshow(S_inv, origin='lower', cmap='jet')
        axs_im[1].imshow(data, origin='lower', cmap='jet')


plt.show()
# plt.figure()
# plt.imshow(Sinv2, origin='lower', cmap='jet')
# plt.show()
