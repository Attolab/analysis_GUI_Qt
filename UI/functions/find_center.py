import numpy as np
from numpy.ma.core import not_equal
from pyqtgraph.graphicsItems.PlotDataItem import dataType


class FindCenter():
    def __init__(self, image=np.ones(shape =(10,64,64),dtype= np.float64)):
        self.image = image
        
    def simplex_center(self):
        [layers,rows,cols] = self.image.shape
        self.rmax = np.max([rows,cols])

        self.rmin = 0
        center = np.zeros(shape=(2,layers),dtype = np.float64)
        prod=np.zeros(shape=(3,3),dtype = np.float64)
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
                    ind = center_ind + np.transpose(np.arange(-1,2))
                    # Calculate residual of image on
                    #(1,1) (1,2) (1,3)
                    #(2,1) (2,2) (2,3)
                    #(3,1) (3,2) (3,3)
                    # where (2,2) is the last guess of the center
                    prod[1,1]=self.MultiplyImages(im_temp,[ind[0,0], ind[0,1]],r_ind[1],r_restriction)
                    prod[1,2]=self.MultiplyImages(im_temp,[ind[0,0], ind[1,1]],r_ind[1],r_restriction)
                    prod[1,3]=self.MultiplyImages(im_temp,[ind[0,0], ind[2,1]],r_ind[1],r_restriction)
                    prod[2,1]=self.MultiplyImages(im_temp,[ind[1,0], ind[0,1]],r_ind[1],r_restriction)
                    prod[2,2]=self.MultiplyImages(im_temp,[ind[1,0], ind[1,1]],r_ind[1],r_restriction)
                    prod[2,3]=self.MultiplyImages(im_temp,[ind[1,0], ind[2,1]],r_ind[1],r_restriction)
                    prod[3,1]=self.MultiplyImages(im_temp,[ind[2,0], ind[0,1]],r_ind[1],r_restriction)
                    prod[3,2]=self.MultiplyImages(im_temp,[ind[2,0], ind[1,1]],r_ind[1],r_restriction)
                    prod[3,3]=self.MultiplyImages(im_temp,[ind[2,0], ind[2,1]],r_ind[1],r_restriction)
    def MakeMask(self,r_ind):
        x = np.meshgrid(np.arange(-r_ind[1],r_ind[1]**2))
        x = x + np.transpose(x) # grid of (x^2 + y^2)
        mask = np.logical_and(r_ind[0]**2 <= x,  x<= r_ind[1]**2)
        return mask

    def MultiplyImages(self,mat,center,r,r_restriction):
        # % Select rectangle
        select_zone = [center - r , center + r]
        # % Apply rectangle on image
        mat=mat[select_zone[0,1]:select_zone[1,1],select_zone[0,0]:select_zone[1,0]]
        # % Take reversed image
        mat_rot=np.rot90(mat,2)
        # % Calculate residual
        res=sum(sum(mat*mat_rot*r_restriction))
        return res




def main():

    F = FindCenter()
    F.simplex_center()
    

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
