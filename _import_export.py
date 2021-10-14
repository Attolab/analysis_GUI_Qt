# _import_export.py

import os, traceback, sys
import h5py
from glob import glob
from PyQt5.QtWidgets import QFileDialog
from matplotlib.ticker import FormatStrFormatter

import glob_var as cts
import numpy as np
import analysis_functions as af
import scipy.special as sp

class Imp_Exp_Mixin:

    def import_tof(self, filename):
        if cts.software_version != 2:
            with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
            #with open(filename, 'r') as file:#with open(filename, 'r', encoding='utf-8',errors='ignore') as file:
                i = 0
                data = []
                try:
                    cts.path = filename
                    #data = [[float(digit) for digit in line.split()] for line in file]
                    for line in file:
                        if i < cts.skiplines:
                            # skipping header lines
                            pass
                        else:
                            data.append([float(digit) for digit in line.split()])
                        i += 1

                    '''
                    if cts.decimal_separ == 'dot':
                        data = [[float(digit) for digit in line.split()] for line in file]
                    elif cts.decimal_separ == 'comma':
                        data = [[float(digit.replace(',', '.')) for digit in line.split()] for line in file]
                    else:
                        print("Error in the code")'''

                except ValueError: #if the decimal separator is a comma
                    data = [[float(digit.replace(',', '.')) for digit in line.split()] for line in file]

                except IndexError:
                    print('Incorrect data file')
                    self.window().statusBar().showMessage('Incorrect data file')

                except Exception:
                    print(traceback.format_exception(*sys.exc_info()))

                finally:
                    data_array = np.asarray(data)  # converting 1D list into 2D array

        else:
            spectrum_i = cts.spectrum_i
            with h5py.File(filename, 'r') as file:
                cts.path = filename
                path = ''.join(['Scan',cts.str_scan_i,'/Detector000/Data1D/Ch000/'])
                raw_datas = file['Raw_datas']
                data_scan = np.array(raw_datas[path+'Data'])  # whole rabbit trace
                data = data_scan[spectrum_i,cts.skiplines:]  # taking tof spectrum corresponding to asked index
                tof = np.array(raw_datas[path+'X_axis'])[cts.skiplines:]
                data_array = np.column_stack((tof, data))

                self.window().updateglobvar_fn()

        return data_array


    # called by CalibWin or RabbitWin
    def importcalib_lr(self):
        #From a calibration file, loading afit, t0fit, cfit and the first harmonic
        # this function can be call either from the calibration tab or the rabbit tab. This means "self" represents
        # either an instance of CalibWin or RabbitWin.

        calib_tab = self.window().calib_tab
        rabbit_tab = self.window().rabbit_tab

        calib_fname = QFileDialog.getOpenFileName(self, 'Import calibration')
        calib_f = calib_fname[0]
        if (calib_f):
            with open(calib_f, 'r') as file:
                f = file.read().splitlines()
                try:
                    if (len(f) < 3):
                        raise IndexError
                    cts.afit, cts.t0fit, cts.cfit = [float(f[i]) for i in range(3)]

                    # calib_win part
                    calib_tab.calibloaded = True
                    calib_tab.calibBool = True
                    calib_tab.tof2en_btn.setEnabled(True)
                    calib_tab.update_fitpar_fn()

                    # rabbit_win part
                    rabbit_tab.reset_btn()
                    rabbit_tab.importdata_btn.setEnabled(True)

                    cts.calibloaded = True

                    self.window().updateglobvar_fn()

                except IndexError:
                    print('Not enough data in the calib file. Needed: a_fit, t0_fit and c_fit')
                except ValueError:
                    print("Incorrect calibration data")

    # called by CalibWin
    def exportcalib_lr(self):
        # Exporting afit, t0fit, cfit and the first harmonic in a file after choosing its name and location

        filename = QFileDialog.getSaveFileName(self, 'Save XUV')
        fname = filename[0]
        if fname:
            fit_param = self.p_opt
            np.savetxt(fname, fit_param, fmt='%1.4e', delimiter='\t')

    # called by RabbitWin
    def exportrab_lr(self):
        ''' "[Export] RABBIT" button listener. Saves the rabbit in two files: *_counts for the data and *_param for
        the parameters'''
        rab_fname = QFileDialog.getSaveFileName(self)
        rab_f = rab_fname[0]
        try:
            if (rab_f):
                header = 'elow\nehigh\ndE\nstepsnb\nbscanstep_nm\nafit\nt0fit\ncfit\nfirst_harm'
                self.rabbit_param = np.array([cts.elow, cts.ehigh, cts.dE, cts.stepsnb, cts.scanstep_nm,
                                              cts.afit, cts.t0fit, cts.cfit, cts.first_harm])
                np.savetxt((rab_f + "_param.txt"), self.rabbit_param, fmt='%.5e',
                           delimiter='\t',header=header)
                np.savetxt((rab_f + "_counts.txt"), cts.rabbit_mat, fmt='%.5e', delimiter='\t')
        except Exception:
            print(traceback.format_exception(*sys.exc_info()))


    # called by VMIWin
    def exportS3D_lr(self):
        ''' "[Export] RABBIT" button listener. Saves the rabbit in two files: *_counts for the data and *_param for
        the parameters'''

        S3D_fname = QFileDialog.getSaveFileName(self)
        S3D_f = S3D_fname[0]

        theta = np.linspace(0, np.pi / 2, 360, endpoint=False)
        ee, tt = np.meshgrid(cts.energy_vect, theta)
        print('np.shape(ee)'+ str(np.shape(ee)))

        angle_width_360 = cts.angle_width * 360 / 90
        print('angle_width_360 = '+str(angle_width_360))
        print('OK 1')
        S3D = []
        Em_angles_i_360 = [int(k * 360 / 90) for k in cts.angle_list]
        print('OK 2')
        for tau in range(0, len(cts.delay_vect)):
            # print(np.shape(sp.eval_legendre(0, np.cos(tt))))
            # print(np.shape(cts.rabbit_mat_P0[tau]))
            S3D_tau = cts.rabbit_mat_P0[tau] * sp.eval_legendre(0, np.cos(tt)) + \
                      cts.rabbit_mat_P2[tau] * sp.eval_legendre(2, np.cos(tt)) + cts.rabbit_mat_P4[tau] * sp.eval_legendre(4, np.cos(tt))
            S3D.append(S3D_tau)

        for theta_k in Em_angles_i_360:
            RABBIT_intg_ang = []
            theta_k_i = theta_k
            theta_k_f = theta_k + angle_width_360
            for i in range(0, len(S3D)):  # len(S3D) = 80 : delays
                S3D_t = S3D[i]  # (theta, E) at a given delay
                a = np.shape(ee)[1]
                RABBIT_sum = np.zeros([a])
                for j in range(int(theta_k_i), int(theta_k_f)):
                    RABBIT_sum = RABBIT_sum + S3D_t[j] * np.sin(j * 90 / 360 * 2 * np.pi / 360)
                RABBIT_intg_ang.append(RABBIT_sum)

            RABBIT_intg_ang = np.array(RABBIT_intg_ang)
            RABBIT_intg_ang3 = RABBIT_intg_ang.T  # only for saved data for analysis_GUI
            S3D_f = S3D_fname[0]
            theta_i_deg = theta_k_i * 90 / 360
            theta_f_deg = theta_k_f * 90 / 360
            name = cts.ang_filenametype.replace('0_5_deg', str(theta_i_deg) + '_' + str(theta_f_deg)+ '_deg')
            try:
                if (S3D_f):
                    np.savetxt((S3D_f + name +".txt"), RABBIT_intg_ang3, fmt='%.5e',
                               delimiter='\t')
            except Exception:
                print(traceback.format_exception(*sys.exc_info()))

    def save_phVSangle(self):
        ''' "[Export] RABBIT" button listener. Saves the phase VS angle of current SB. If ang intg is calcculated and the box is checked, it is also saved in another file'''

        save_phVSangle_fname = QFileDialog.getSaveFileName(self)
        save_phVSangle_f = save_phVSangle_fname[0]

        C = np.vstack((cts.Phi,cts.DPhi))
        Cbis = np.vstack((cts.Ampl,C))
        D = cts.tt_angles*180/np.pi
        E = np.vstack((D,Cbis)).T

        if cts.Add_angl_intg:
            self.SB_i = cts.sb_order.index(cts.SBi_choice)
            Phi_rec = cts.data_2w_std_ang[:, int(self.SB_i), 3]
            Ampl_rec = cts.data_2w_std_ang[:, int(self.SB_i), 2]
            if cts.Change_Sign:
                Phi_rec = - cts.data_2w_std_ang[:, int(self.SB_i), 3]
            Phi_rec_err = cts.data_2w_std_ang[:, int(self.SB_i), 4]
            U = np.vstack((Phi_rec, Phi_rec_err))
            Ubis = np.vstack((Ampl_rec, U))
            V = np.vstack((cts.angle_list, Ubis)).T

        try:
            if (save_phVSangle_f):
                np.savetxt((save_phVSangle_f + ".txt"), E , fmt='%.5e',
                           delimiter='\t' , header=" Angle(°) \t Amplitude(arbU) \tPhase (rad) evolving with angle\t Phase error(rad) \t")
                if cts.Add_angl_intg:
                    np.savetxt((save_phVSangle_f + '_angularly_intg'+".txt"), V, fmt='%.5e',
                               delimiter='\t',
                               header="Angle(°) \t Ampl(arbU) \t Phase (rad)\t Phase error(rad)\t")
        except Exception:
            print(traceback.format_exception(*sys.exc_info()))


    # called by RabbitWin
    def export_2w_lr(self):
        ''' "[Export] 2w" button listener'''
        twow_fname = QFileDialog.getSaveFileName(self)
        twow_f = twow_fname[0]
        try:
            if (twow_f):
                data_2w = np.dstack((self.energy, cts.peak, cts.peak_phase, cts.rabbit_mat.sum(axis=0)))[0]
                data_2w = np.array(data_2w)
                np.savetxt((twow_f), data_2w, fmt='%.5e', delimiter='\t',
                           header="Photon energy [eV]\t 2w Ampl [arb. u.] \t 2w Phase [rad] \
                            \t delay-integrated RABBIT trace")
        except Exception:
            print(traceback.format_exception(*sys.exc_info()))

    def export_2w_std_lr(self):
        ''' "[Export] 2w" button listener'''
        twow_fname = QFileDialog.getSaveFileName(self)
        twow_f = twow_fname[0]
        try:
            if (twow_f):
                data_2w = np.dstack((cts.bands_vect[:,0],cts.bands_vect[:,1], cts.peak, cts.peak_phase, cts.phase_err))[0]
                data_2w = np.array(data_2w)
                np.savetxt((twow_f), data_2w, fmt='%.5e', delimiter='\t',
                           header="Photon energy min[eV]\t Photon energy max[eV]\t 2w Ampl [arb. u.] \t 2w Phase [rad]\t 2w Phase error [rad]")
        except Exception:
            print(traceback.format_exception(*sys.exc_info()))



    # called by RainbowWin (_Rabbit_win_subwidgets.RainbowWin)
    def export_lr(self) -> None:
        filenamesave = QFileDialog.getSaveFileName(self)
        fname = filenamesave[0]
        try:
            if fname:
                en=[]
                amp=[]
                phase=[]
                header = "FT_padding = " + str(cts.FT_padding) + ", " + \
                         "FT_window = " + str(cts.FT_window) + ", " + \
                         "FT_zero_order = " + str(cts.FT_zero_order) + ", " + \
                         "FT_npad = " + str(cts.FT_npad) + "\n" + \
                         "two_w_average = " + str(cts.two_w_average) + ", " + \
                         "two_w_bfilter = " + str(cts.two_w_bfilter) + ", " + \
                         "two_w_integral = " + str(cts.two_w_integral) + ", " + \
                         "two_w_phioffset = " + str(cts.two_w_phioffset) + "\n\n" + \
                         "energy (eV)\t2w_amplitude\t2w_phase"
                k=0
                for i in range(self.par.energy_rainbow.shape[0]):
                    if (self.par.energy_rainbow[i] - self.par.energy_rainbow[i - 1] >\
                                    2 * cts.dE or i == self.par.energy_rainbow.shape[0] - 1):
                        l = np.array([en, amp, phase])
                        l = np.transpose(l)
                        np.savetxt((fname + "_SB" + str(cts.first_harm + 1 + 2 * k) + ".txt"), l, fmt='%.5e',
                                   delimiter='\t', header=header)
                        del en[:]
                        del amp[:]
                        del phase[:]
                        k += 1
                    en.append(self.par.energy_rainbow[i])
                    amp.append(cts.peak[i])
                    phase.append(cts.peak_phase[i])

        except Exception:
            print(traceback.format_exception(*sys.exc_info()))