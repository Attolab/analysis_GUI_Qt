import numpy as np
from numpy.core.fromnumeric import argmax
from numpy.ma.core import not_equal
from pyqtgraph.graphicsItems.PlotDataItem import dataType
import h5py

class FindCenter():
    def __init__(self, image=np.ones(shape =(10,64,64),dtype= np.float64), rmin=0, rmax=64):
        self.image = image
        self.rmin = rmin
        self.rmax = rmax

    def mean_center(self):
        [layers,rows,cols] = self.image.shape
        center = np.zeros(shape=(2,layers),dtype = np.float64)
        for index,im_temp in enumerate(self.image):
            center[0,index] = np.sum(im_temp.mean(axis = 1)*np.arange(rows))/np.sum(im_temp.mean(axis = 1))
            center[1,index] = np.sum(im_temp.mean(axis = 0)*np.arange(cols))/np.sum(im_temp.mean(axis = 0))
        print(center)
    def simplex_center(self):
        [layers,rows,cols] = self.image.shape
        center = np.zeros(shape=(2,layers),dtype = np.float64)
        n = 2
        N = 2*n+1
        prod=np.zeros(shape=(N,N),dtype = np.float64)
        for index,im_temp in enumerate(self.image):
            center[0,index] = np.sum(im_temp.mean(axis = 1)*np.arange(rows))/np.sum(im_temp.mean(axis = 1))
            center[1,index] = np.sum(im_temp.mean(axis = 0)*np.arange(cols))/np.sum(im_temp.mean(axis = 0))
            r_ind = 1 + np.floor([self.rmin ,self.rmax])
            i=1
            j=1
            r_old=[999] #Dummy check just to initialize loop
            # Centers coordinate in index of matrix
            center_ind = 1 + np.floor(center[:,index])
            while (not_equal(i,0) or not_equal(j,0)):
                r_ind[1]= np.min([rows-center_ind[1]-1,cols-center_ind[0]-1,center_ind[1]-1,center_ind[0]-1,r_ind[1]])
                if not_equal(r_ind[1],r_old):
                    r_restriction = self.MakeMask(r_ind) # Make mask to select aoi
                    r_old=r_ind[1] # Restock last meaningful range
            # Grid of index (3*3)

                ind = center_ind + np.linspace(-n,n,N)[:,np.newaxis]
                # Calculate residual of image on
                #(1,1) (1,2) (1,3)
                #(2,1) (2,2) (2,3)
                #(3,1) (3,2) (3,3)
                # where (2,2) is the last guess of the center
                for i in range(n+1):
                    for j in range(n+1):
                        prod[i,j] = self.MultiplyImages(im_temp,[ind[i,0], ind[j,1]],r_ind[1],r_restriction)

                # prod[0,0]=self.MultiplyImages(im_temp,[ind[0,0], ind[0,1]],r_ind[1],r_restriction)
                # prod[0,1]=self.MultiplyImages(im_temp,[ind[0,0], ind[1,1]],r_ind[1],r_restriction)
                # prod[0,2]=self.MultiplyImages(im_temp,[ind[0,0], ind[2,1]],r_ind[1],r_restriction)
                # prod[1,0]=self.MultiplyImages(im_temp,[ind[1,0], ind[0,1]],r_ind[1],r_restriction)
                # prod[1,1]=self.MultiplyImages(im_temp,[ind[1,0], ind[1,1]],r_ind[1],r_restriction)
                # prod[1,2]=self.MultiplyImages(im_temp,[ind[1,0], ind[2,1]],r_ind[1],r_restriction)
                # prod[2,0]=self.MultiplyImages(im_temp,[ind[2,0], ind[0,1]],r_ind[1],r_restriction)
                # prod[2,1]=self.MultiplyImages(im_temp,[ind[2,0], ind[1,1]],r_ind[1],r_restriction)
                # prod[2,2]=self.MultiplyImages(im_temp,[ind[2,0], ind[2,1]],r_ind[1],r_restriction)

                #Pick maximum residual as new guess for the center
                b=np.argmax(prod,axis = 1)
                a=np.array([prod[i,b[i]] for i in range(N)])                
                d=np.argmax(a)
                i=d-2
                j=b[d]-2
                # Redefinition of center
                center_ind = center_ind + [j,i]
                center[:,index] =  ( center_ind + 1) 
                # Break if meaningless, return center of mass
                if np.min(center[:,index])<0 or center[0,index] > cols or center[1,index] > rows:
                    print('Simplex center not found. Using geometric center instead.')
                    center[0,index] = np.round(np.sum(im_temp.mean(axis = 1)*np.arange(rows))/np.sum(im_temp.mean(axis = 1)))
                    center[1,index] = np.round(np.sum(im_temp.mean(axis = 0)*np.arange(cols))/np.sum(im_temp.mean(axis = 0)))
                    i=0
                    j=0
                # Retrieve center
                # center[:,index] =  ( center_ind - 1 ) 
                # * reshape_factor(l);
                #         center(k,:) =  ( center_ind(k,:)  ) * reshape_factor(l);
        print(center)

    def MakeMask(self,r_ind):
        x = np.meshgrid(np.arange(-r_ind[1],r_ind[1])**2)
        x = x + np.transpose(x) # grid of (x^2 + y^2)
        mask = np.logical_and(r_ind[0]**2 <= x,  x<= r_ind[1]**2)
        return mask

    def MultiplyImages(self,mat,center,r,r_restriction):
        # % Select rectangle
        select_zone = np.array([center - r , center + r],dtype=int)
        # % Apply rectangle on image
        mat=mat[select_zone[0][1]:select_zone[1][1],select_zone[0][0]:select_zone[1][0]]
        # % Take reversed image
        mat_rot=np.rot90(mat,2)
        # % Calculate residual
        res=np.sum(np.sum(mat*mat_rot*r_restriction))
        return res




def main():
   
    path_file = 'Q:\LIDyL\Atto\ATTOLAB\SE1\SlowRABBIT\\'
    filename = 'Dataset_20210423_003.h5'
    scan = '000'  # vérifier dans hdfview        
    with h5py.File(path_file + filename, 'r') as file:
        path = ''.join(['Scan', scan,
                        '/Detector000/Data2D/Ch000/'])  # Faire attention : parfois c'est Detector001 (voir dans hdfview)
        raw_datas = file['Raw_datas']
        data = np.array(raw_datas[path + 'Data'][0]) #Ne charger que l'image dont je vais déterminer le P0
        F = FindCenter(data[np.newaxis,:,:],10,1000)
        F.simplex_center()
        F.mean_center()


if __name__=="__main__":
    main()        

#         while(i~=0 || j~=0)
#             %check if center is closer to the edge than the radial range allows.
# %             r_ind(2)=min([rows_temp-center_ind(2)-2,cols_temp-center_ind(1)-2,center_ind(2)-2,center_ind(1)-2,r_ind(2)]);
#             r_ind(2)=min([rows_temp-center_ind(2)-1,cols_temp-center_ind(1)-1,center_ind(2)-1,center_ind(1)-1,r_ind(2)]);

#             % Recalculate mask if borders alert
            
#             if r_ind(2) ~= r_old
#                 [r_restriction] = MakeMask(r_ind); % Make mask to select aoi
#                 r_old=r_ind(2); % Restock last meaningful range
#             end
#             % Grid of index (3*3)
#             ind = center_ind + (-1:1)';
#             % Calculate residual of image on
#             %(1,1) (1,2) (1,3)
#             %(2,1) (2,2) (2,3)
#             %(3,1) (3,2) (3,3)
#             % where (2,2) is the last guess of the center
#             prod(1,1)=MultiplyImages(im_temp,[ind(1,1) ind(1,2)],r_ind(2),r_restriction);
#             prod(1,2)=MultiplyImages(im_temp,[ind(1,1) ind(2,2)],r_ind(2),r_restriction);
#             prod(1,3)=MultiplyImages(im_temp,[ind(1,1) ind(3,2)],r_ind(2),r_restriction);
#             prod(2,1)=MultiplyImages(im_temp,[ind(2,1) ind(1,2)],r_ind(2),r_restriction);
#             prod(2,2)=MultiplyImages(im_temp,[ind(2,1) ind(2,2)],r_ind(2),r_restriction);
#             prod(2,3)=MultiplyImages(im_temp,[ind(2,1) ind(3,2)],r_ind(2),r_restriction);
#             prod(3,1)=MultiplyImages(im_temp,[ind(3,1) ind(1,2)],r_ind(2),r_restriction);
#             prod(3,2)=MultiplyImages(im_temp,[ind(3,1) ind(2,2)],r_ind(2),r_restriction);
#             prod(3,3)=MultiplyImages(im_temp,[ind(3,1) ind(3,2)],r_ind(2),r_restriction);
            
#             % Pick maximum residual as new guess for the center
#             [a,b]=max(prod);
#             [~,d]=max(a);
#             i=d-2;
#             j=b(d)-2;
#             % Redefinition of center
#             center_ind = center_ind + [j,i] ;
            
#             % Break if meaningless, return center of mass
#             if min(center(k,:))<0 || center(k,1) > cols || center(k,2) > rows
#                 fprintf('Simplex center not found. Using geometric center instead.')
#                 center(k,:)=round([sum(sum(im(:,:,k),1).*(1:size(im,1))),sum(sum(im(:,:,k),2).*(1:size(im,2))')]/sum(sum(im(:,:,k))));
#                 i=0;
#                 j=0;
#             end
#         end
#         % Retrieve center
#         center(k,:) =  ( center_ind - 1 ) * reshape_factor(l);
#         %         center(k,:) =  ( center_ind(k,:)  ) * reshape_factor(l);
        
#     end
#     center(k,:) =  center(k,:) * set_s.imagebinsize;
# end
# end



# function res=MultiplyImages(mat,center,r,r_restriction)
# % Select rectangle
# select_zone = [center - r ; center + r];
# % Apply rectangle on image
# mat=mat(select_zone(1,2):select_zone(2,2),select_zone(1,1):select_zone(2,1));
# % Take reversed image
# mat_rot=rot90(mat,2);
# % Calculate residual
# res=sum(sum(mat.*mat_rot.*r_restriction));
# end
# function  [mask] = MakeMask(r_ind)
# x=meshgrid(-r_ind(2):r_ind(2)).^2;
# x =(x+x'); % grid of (x^2 + y^2)
# mask = r_ind(1)^2 <= x & x <= r_ind(2)^2 ; % Selected range on image
# end
