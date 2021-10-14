import h5py
import numpy as np
from PyQt5.QtWidgets import QFileDialog
import matplotlib.pyplot as plt
from scipy import constants
C = constants.speed_of_light
import analysis_functions as af
from scipy.signal import gaussian, hamming, butter, freqz
from glob import glob
from numpy import loadtxt, arange, array, where, zeros, convolve
from numpy import savetxt, int32, append, linspace, argmin
import numpy as np
from scipy import optimize as opt
from scipy import interpolate
import glob_var as cts

#Données du TOF : importer un spectre TOF
data_filename = r'C:/Users/aautuori/Documents/Données labo/2020-02-06/Dataset_20200206_000.h5'


def jacobian_transform2(tof, counts):

    a_fit = 7.8510e-12
    t0_fit = -5.032e-9
    c_fit = 16.064
    nu = cts.cur_nu
    dE = 0.01
    elow = 24.80
    ehigh = 54.24

    qq = a_fit/(tof-t0_fit)**2 + c_fit
    EeV = cts.HEV*nu*qq
    qqderiv = 2*a_fit/(tof-t0_fit)**3
    Ederiv = abs(cts.HEV*nu*qqderiv)
    #print(Ederiv)
#    a_fit,t0_fit,c_fit,nu = np.loadtxt(fdir+'calib.txt')
#    EeV = a_fit/(tof-t0_fit)**2 + c_fit
#    Ederiv = 2*a_fit/(tof-t0_fit)**3

    nbsteps = int((ehigh-elow)/dE + 1)
    eevlin = np.linspace(elow, ehigh, nbsteps)  # for non integer steps, np.linspace is better than np.arange

    dshape = counts.shape
    #print(dshape)

    if len(dshape) > 1:
        counts = counts[:,::-1]
        dshape = counts.shape
        countsnew = np.zeros((dshape[0],dshape[1]))

        for i in range(dshape[0]):
            countsnew[i,:]=counts[i,:]/Ederiv

        f = interpolate.interp1d(EeV,countsnew)
        countsnew = f(eevlin)
        print("blop")
    else:
        counts = counts[::-1]
        countsj = counts/Ederiv
        countsnew = np.interp(eevlin,EeV,countsj)
    #print(countsnew)

    return eevlin, countsnew





skiplines = 0
with h5py.File(data_filename, 'r') as file:
    path = data_filename
    path = ''.join(['Scan', '000', '/Detector000/Data1D/Ch000/'])
    raw_datas = file['Raw_datas']
    data_scan = np.array(raw_datas[path + 'Data'])  # whole rabbit trace
    data = data_scan[0, skiplines:]  # taking tof spectrum corresponding to asked index
    tof = np.array(raw_datas[path + 'X_axis'])[skiplines:]
    data_array = np.column_stack((tof, data))

#
# # background substraction
# rmbg_avg_min = 300
# rmbg_avg_max = 400
# skiplines_RAB = 1500
#
# #Données du TOF : importer un RABBIT TOF
# with h5py.File(data_filename, 'r') as file:
#     data_path = ''.join(['Scan', '000', '/Detector000/Data1D/Ch000/'])
#     delay_path = ''.join(['Scan','000', '/Scan_x_axis'])
#
#     raw_datas = file['Raw_datas']
#     data_scan = np.array(raw_datas[data_path + 'Data'])[:,skiplines_RAB:]  # whole rabbit trace
#     tof_vect = np.array(raw_datas[data_path + 'X_axis'])[skiplines_RAB:]
#     delay_vect = np.array(raw_datas[delay_path])
#
#     scanstep_nm = (delay_vect[1:] - delay_vect[:-1]).mean() * 1000
#     delay_vect = (delay_vect - delay_vect[0])*2/(C*1e-9)
#     stepsnb = data_scan.shape[0]
#
#
#     for i in range(len(delay_vect)):
#         counts = data_scan[i, :] - data_scan[i, rmbg_avg_min:rmbg_avg_max].mean()
#         tofvect2 = tof_vect[::-1]
#         energy_vect, counts2 = jacobian_transform2(tofvect2[:], counts[:])
#
#         if i == 0:
#             rabbit_mat = np.zeros([stepsnb, energy_vect.shape[0]])
#             # print(cts.rabbit_mat.shape)
#         rabbit_mat[i, :] = counts2
#
# plt.imshow(rabbit_mat, vmin = -2e-13, vmax = 2e-11)
#
#
#



# #Données de la caméra
# data_filename = r'C:/Users/aautuori/Documents/Données labo/2020-07-24\Dataset_20200724_000\Dataset_20200724_000.h5'
#
# skiplines = 0
# with h5py.File(data_filename, 'r') as file:
#     path = data_filename
#     path = ''.join(['Scan', '000', '/Detector000/Data2D/Ch000/'])
#     raw_datas_vmi = file['Raw_datas']
#     data_scan_vmi = np.array(raw_datas_vmi[path + 'Data'])  # whole rabbit trace
#     data_vmi = data_scan_vmi[0, skiplines:]  # taking tof spectrum corresponding to asked index
#
# plt.imshow(data_vmi, vmin = 95, vmax = 110)
#
# skiplines = 0
# with h5py.File(data_filename, 'r') as file:
#     path = data_filename
#     path = ''.join(['Scan', '000', '/Detector000/Data2D/Ch000/'])
#     raw_datas_vmi2 = file['Raw_datas']
#     data_scan_vmi2 = np.array(raw_datas_vmi[path + 'Data'])  # whole rabbit trace
#     data_vmi2 = data_scan_vmi[10, skiplines:]  # taking tof spectrum corresponding to asked index
#
# plt.imshow(data_vmi2, vmin = 95, vmax = 110)
#
#





