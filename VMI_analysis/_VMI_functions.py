# _VMI_functions.py

from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import Qt
from glob import glob
import traceback, sys, os
import numpy as np
import math
import scipy.optimize as opt
import scipy.special as sp

import scipy
import h5py

import glob_var as cts
import analysis_functions as af
from VMI_analysis import plot_3D_phase_angle_energy_win as pl3D
from VMI_analysis import plot_SBphase_VS_angle_win as plSB
from VMI_analysis import imshow_2w_ampl_win as imA
from VMI_analysis import imshow_2w_phase_win as imP

class VMI_functions_mixin:
    """ This is not really a standalone class. It's a trick I use to split the RabbitWin class definition
    ("Rabbit-win.py") into two files: one for the GUI, one for the function; but keeping the advantage
    of sharing instance variables (self.something) between the two

    Here are defined the majority of the functions (methods to be correct) used in the RabbitWin object,
    especially analysis functions.
    """
    #
    def import_P0_matrix(self):
        """ Used to load VMI P0 matrices already energy to radius converted"""
        print(' P0 function OK')
        fname = QFileDialog.getOpenFileName(self, "Import P0 RABBIT matrix")
        f = fname[0]
        if f:
            cts.path = f
            try:
                P0 = np.loadtxt(f)
                print(f)
            except Exception:
                print(traceback.format_exception(*sys.exc_info()))

        P0 = P0.T
        P0 = P0.T
        dshape = P0.shape
        cts.stepsnb = dshape[0]

        Vrep = cts.vrep  # in kV
        elow = 0.01 + cts.cur_Ip
        ehigh = 3.078 * Vrep + cts.cur_Ip

        cts.delay_vect = np.linspace(0, cts.scanstep_nm * 2 / cts.C * cts.stepsnb * 1e-9, cts.stepsnb,
                                     endpoint=False)
        nbsteps_E = dshape[1]
        cts.energy_vect = np.linspace(cts.elow, cts.ehigh, nbsteps_E)
        cts.rabbit_mat_P0 = P0

    def import_P2_matrix(self):
        """ Used to load VMI P2 matrices already energy to radius converted"""
        print(' P2 function OK')
        fname = QFileDialog.getOpenFileName(self, "Import P2 RABBIT matrix")
        f = fname[0]
        if f:
            cts.path = f
            try:
                P2 = np.loadtxt(f)
                print(f)
            except Exception:
                print(traceback.format_exception(*sys.exc_info()))

        P2 = P2.T
        P2 = P2.T
        dshape = P2.shape
        cts.stepsnb = dshape[0]
        cts.delay_vect = np.linspace(0, cts.scanstep_nm * 2 / cts.C * cts.stepsnb * 1e-9, cts.stepsnb,
                                     endpoint=False)
        # nbsteps_E = (cts.ehigh - cts.elow) / cts.dE + 1
        # cts.energy_vect = np.linspace(cts.elow, cts.ehigh, nbsteps_E)
        cts.rabbit_mat_P2 = P2

    def import_P4_matrix(self):
        """ Used to load VMI P2 matrices already energy to radius converted"""
        print(' P4 function OK')
        fname = QFileDialog.getOpenFileName(self, "Import P4 RABBIT matrix")
        f = fname[0]
        if f:
            cts.path = f
            try:
                P4 = np.loadtxt(f)
                print(f)
            except Exception:
                print(traceback.format_exception(*sys.exc_info()))

        P4 = P4.T
        P4 = P4.T
        dshape = P4.shape
        cts.stepsnb = dshape[0]

        Vrep = cts.vrep  # in kV
        elow = 0.01 + cts.cur_Ip
        ehigh = 3.078 * Vrep + cts.cur_Ip

        cts.delay_vect = np.linspace(0, cts.scanstep_nm * 2 / cts.C * cts.stepsnb * 1e-9, cts.stepsnb,
                                     endpoint=False)
        # nbsteps_E = (cts.ehigh - cts.elow) / cts.dE + 1
        # cts.energy_vect = np.linspace(cts.elow, cts.ehigh, nbsteps_E)
        cts.rabbit_mat_P4 = P4

    def import_P0_Rainbow(self):
        """ Used to load VMI P0 matrices already energy to radius converted"""
        print(' P0 function OK')
        fname = QFileDialog.getOpenFileName(self, "Import P0 2w Rainbow RABBIT analysis")
        f = fname[0]
        if f:
            cts.path = f
            try:
                P0_2w = np.loadtxt(f)
                print(f)
            except Exception:
                print(traceback.format_exception(*sys.exc_info()))
        cts.Rainbow_2w_P0 = P0_2w
        self.importVMI_P2_Rainbow_btn.setEnabled(True)



    def import_P2_Rainbow(self):
        """ Used to load VMI P0 matrices already energy to radius converted"""
        print(' P2 function OK')
        fname = QFileDialog.getOpenFileName(self, "Import P2 2w Rainbow RABBIT analysis")
        f = fname[0]
        if f:
            cts.path = f
            try:
                P2_2w = np.loadtxt(f)
                print(f)
            except Exception:
                print(traceback.format_exception(*sys.exc_info()))
        cts.Rainbow_2w_P2 = P2_2w
        self.importVMI_P4_Rainbow_btn.setEnabled(True)

    def import_P4_Rainbow(self):
        """ Used to load VMI P0 matrices already energy to radius converted"""
        print(' P4 function OK')
        fname = QFileDialog.getOpenFileName(self, "Import P4 2w Rainbow RABBIT analysis")
        f = fname[0]
        if f:
            cts.path = f
            try:
                P4_2w = np.loadtxt(f)
                print(f)
            except Exception:
                print(traceback.format_exception(*sys.exc_info()))
        cts.Rainbow_2w_P4 = P4_2w
        self.plot_Rainbow_Rab_btn.setEnabled(True)
        self.plot_Rainbow3D_Rab_btn.setEnabled(True)



    def import_P0_std(self):
        """ Used to load VMI P0 2w standard RABBIT analysis results"""
        print(' P0 function OK')
        fname = QFileDialog.getOpenFileName(self, "Import P0 2w Normal RABBIT analysis")
        f = fname[0]
        if f:
            cts.path = f
            try:
                P0_2w = np.loadtxt(f)
                print(f)
            except Exception:
                print(traceback.format_exception(*sys.exc_info()))
        cts.std_2w_P0 = P0_2w
        self.importVMI_P2_std_btn.setEnabled(True)

    def import_P2_std(self):
        """ Used to load VMI P2 2w standard RABBIT analysis results"""
        print(' P2 function OK')
        fname = QFileDialog.getOpenFileName(self, "Import P2 2w Normal RABBIT analysis")
        f = fname[0]
        if f:
            cts.path = f
            try:
                P2_2w = np.loadtxt(f)
                print(f)
            except Exception:
                print(traceback.format_exception(*sys.exc_info()))
        cts.std_2w_P2 = P2_2w
        self.importVMI_P4_std_btn.setEnabled(True)

    def import_P4_std(self):
        """ Used to load VMI P4 2w standard RABBIT analysis results"""
        print(' P4 function OK')
        fname = QFileDialog.getOpenFileName(self, "Import P4 2w Normal RABBIT analysis")
        f = fname[0]
        if f:
            cts.path = f
            try:
                P4_2w = np.loadtxt(f)
                print(f)
            except Exception:
                print(traceback.format_exception(*sys.exc_info()))
        cts.std_2w_P4 = P4_2w
        # print(cts.std_2w_P4)


    def import_angle_list(self):
        """ Used to load list of angles at which the user desired to get "angularly integrated" spectra.
        The angle list are the inferior limit of the intervals"""
        # print(' angle list function OK')
        fname = QFileDialog.getOpenFileName(self, "Import list of angles where the integration intervals start")
        f = fname[0]
        if f:
            cts.path = f
            try:
                list = np.loadtxt(f)
                # print(f)
            except Exception:
                print(traceback.format_exception(*sys.exc_info()))
        cts.angle_list = list
        # print(cts.angle_list)

    def import2w_std_ang(self):
        data = []
        angles = []
        # w_IR = 2 * np.pi * scipy.constants.speed_of_light / 800e-9
        # sb_order = []
        fname = QFileDialog.getOpenFileName(self, "Import std RABBIT table of data at different angle intervals")
        for i in cts.angle_list:
            f = fname[0]
            print(i)
            print(str(cts.angle_list[0])+'_'+ str(cts.angle_list[0] + cts.angle_width)+ '_deg')
            print(str((i)) + '_' + str((i) + 5) + '_deg')
            f = f.replace(str(cts.angle_list[0])+'_'+ str(cts.angle_list[0] + cts.angle_width)+ '_deg', str((i)) + '_' + str((i) + 5) + '_deg')
            print(f)
            if f:
                cts.path = f
                try:
                    d_SB = np.loadtxt(f)
                    # print(f)
                except Exception:
                    print(traceback.format_exception(*sys.exc_info()))
            data.append(d_SB)
            angles.append(i)
        cts.data_2w_std_ang = np.array(data)
        print('cts.data_2w_std_ang')
        print(cts.data_2w_std_ang)
        print(np.shape(cts.data_2w_std_ang))



    def angles_for_plot(self):
        """ Used to load list of angles at which the user desired to get "angularly integrated" spectra.
        The angle list are the inferior limit of the intervals"""
        # print(' angle list function OK')
        fname = QFileDialog.getOpenFileName(self, "Import list of angles at which you want to plot")
        f = fname[0]
        if f:
            cts.path = f
            try:
                list = np.loadtxt(f)
                # print(f)
            except Exception:
                print(traceback.format_exception(*sys.exc_info()))
        cts.angles_for_plots = list
        # print(cts.angle_list)

    def plot_Rainbow3D_Rab(self):
        Phase_offset = cts.phaseshift_for_3D_plots
        c00_2w_P0 = cts.Rainbow_2w_P0
        c00_2w_P2 = cts.Rainbow_2w_P2
        c00_2w_P4 = cts.Rainbow_2w_P4
        istart = 3
        istop = np.shape(c00_2w_P0)[0]
        N_c = 1

        energy = c00_2w_P0[istart:istop, 0]
        theta = np.linspace(0, np.pi / 2, 360,
                            endpoint=False)  # sampling of emission angle. It goes from 0 to 90°, there are 360 points.

        ee, tt = np.meshgrid(energy, theta)

        A0 = c00_2w_P0[istart:istop, 1]
        A2 = c00_2w_P2[istart:istop, 1]
        A4 = c00_2w_P4[istart:istop, 1]

        Phi0 = c00_2w_P0[istart:istop, 2]
        Phi2 = c00_2w_P2[istart:istop, 2]
        Phi4 = c00_2w_P4[istart:istop, 2]

        A0 = np.convolve(A0, np.ones((N_c,)) / N_c, mode='same')  # N_c = 1 : just changes column to vector
        A2 = np.convolve(A2, np.ones((N_c,)) / N_c, mode='same')
        A4 = np.convolve(A4, np.ones((N_c,)) / N_c, mode='same')

        Phi0 = np.convolve(Phi0, np.ones((N_c,)) / N_c, mode='same')
        Phi2 = np.convolve(Phi2, np.ones((N_c,)) / N_c, mode='same')
        Phi4 = np.convolve(Phi4, np.ones((N_c,)) / N_c, mode='same')

        alpha = A0 * np.cos(Phi0) * sp.eval_legendre(0, np.cos(tt)) + \
                A2 * np.cos(Phi2) * sp.eval_legendre(2, np.cos(tt)) + \
                A4 * np.cos(Phi4) * sp.eval_legendre(4, np.cos(tt))

        beta = A0 * np.sin(Phi0) * sp.eval_legendre(0, np.cos(tt)) + \
               A2 * np.sin(Phi2) * sp.eval_legendre(2, np.cos(tt)) + \
               A4 * np.sin(Phi4) * sp.eval_legendre(4, np.cos(tt))

        Phi = np.zeros(np.shape(alpha))
        for j in range(energy.shape[0]):
            for i in range(0, theta.shape[0]):
                Phi[i, j] = math.atan2(beta[i, j], alpha[i, j]) + Phase_offset
        #
        # # these loops are tricks to fold the phases of the arctan function (like wrap2pmpi but the arctan(beta/alpha) is pi-periodiq
        # #if from an angle to the next the phase jumps more than a certain amount (+/- arbitrary), we change the phase. Gives smooth phase evolution / theta
        for j in range(energy.shape[0]):
            if A0[j] < 0.005 * max(
                    A0):  # if te amplitude is to small, the phase is put to 0 as it has no meaning anyways
                Phi[:, j] = 0
            else:
                for i in range(1, theta.shape[0]):
                    if Phi[i, j] - Phi[i - 1, j] > (np.pi / 2 - 0.8):
                        while Phi[i, j] - Phi[i - 1, j] > (np.pi / 2 - 0.8):
                            Phi[i, j] -= np.pi
                    elif Phi[i, j] - Phi[i - 1, j] < -1 * (np.pi / 2 - 0.8):
                        while Phi[i, j] - Phi[i - 1, j] < -1 * (np.pi / 2 - 0.8):
                            Phi[i, j] += np.pi
                    else:
                        pass

        Ampl = np.sqrt(alpha ** 2 + beta ** 2)

        cts.Phi_Rainbow = np.array(Phi)
        cts.Ampl_Rainbow = np.array(Ampl)

        n_min = 3
        n_max = np.shape(energy)[0]
        if cts.energy_min_for_3D in energy:
            n_min = energy.index(cts.energy_min_for_3D)
        else:
            for k in range(0, len(energy)):
                if energy[k] > cts.energy_min_for_3D:
                    n_min = k
                    break
        if cts.energy_max_for_3D in energy:
            n_max = energy.index(cts.energy_max_for_3D)
        else:
            for k in range(0, len(energy)):
                if energy[k] > cts.energy_max_for_3D:
                    n_max = k
                    break

        thetamin = int(cts.theta_min_for_3D * 360 / 90)
        thetamax = int(cts.theta_max_for_3D * 360 / 90)
        cts.X = ee[thetamin:thetamax, n_min:n_max]
        cts.Y = tt[thetamin:thetamax, n_min:n_max] * 180 / np.pi
        cts.Z_ampl = cts.Ampl_Rainbow[thetamin:thetamax,n_min:n_max]
        if self.phasewrap_cb.isChecked():
            cts.Z = af.wrap2pmpi(cts.Phi_Rainbow[thetamin:thetamax, n_min:n_max])
        else:
            cts.Z = cts.Phi_Rainbow[thetamin:thetamax, n_min:n_max]
        try:
            w = pl3D.plot_3D_phase_angle_energy_Win(self)  # new class defined in separate file
        except Exception:
            print(traceback.format_exception(*sys.exc_info()))

        try:
            w = imA.imshow_2w_ampl_Win(self)  # new class defined in another file
        except Exception:
            print(traceback.format_exception(*sys.exc_info()))

        try:
            w = imP.imshow_2w_phase_Win(self)  # new class defined below
        except Exception:
            print(traceback.format_exception(*sys.exc_info()))
        #

    def plot_phVSangle(self):
        P0 = cts.std_2w_P0
        P2 = cts.std_2w_P2
        P4 = cts.std_2w_P4
        Nb_SB = np.shape(P0)[0]
        print(Nb_SB)
        cts.sb_order =[cts.SBi + 2*k for k in range(0, Nb_SB)]
        print(cts.sb_order)
        SB_i =cts.sb_order.index(cts.SBi_choice)
        print(SB_i)
        tt = cts.tt_angles

        A_l = np.array([P0[SB_i, 2], P2[SB_i, 2], P4[SB_i, 2]])
        DA_l = A_l * 0.05  # maybe wrong, but I saw that the influence on the total error was negligible
        Phi_l = np.array([P0[SB_i, 3], P2[SB_i, 3], P4[SB_i, 3]])
        DPhi_l = np.array([P0[SB_i, 4], P2[SB_i, 4], P4[SB_i, 4]])

        alpha = np.array([A_l[i] * np.cos(Phi_l[i]) * sp.eval_legendre(2 * i, np.cos(tt))
                          for i in range(3)]).sum(axis=0)

        beta = np.array([A_l[i] * np.sin(Phi_l[i]) * sp.eval_legendre(2 * i, np.cos(tt))
                         for i in range(3)]).sum(axis=0)

        Phi = np.zeros(np.shape(alpha))
        for i in range(0, tt.shape[0]):
            Phi[i] = af.wrap2pmpi(np.arctan2(beta[i], alpha[i]) )
        Ampl = np.zeros(np.shape(alpha))
        for i in range(0, tt.shape[0]):
            Ampl[i] = math.sqrt(beta[i]**2 + alpha[i]**2)

        # error estimation
        sum = np.array([np.abs(sp.eval_legendre(2 * i, np.cos(tt)) *
                               ((np.sin(Phi_l[i]) * alpha - np.cos(Phi_l[i]) * beta))) * DA_l[i] + \
                        np.abs(A_l[i] * (np.cos(Phi_l[i]) * alpha + np.sin(Phi_l[i]) * beta)) * DPhi_l[i] / 2 \
                        for i in range(3)]).sum(axis=0)

        DPhi = 1 / (alpha ** 2 + beta ** 2) * sum

        cts.Phi = Phi
        cts.DPhi = DPhi
        cts.Ampl = Ampl
        if self.angl_intg_cb.isChecked():
            cts.Add_angl_intg = True
        if self.sign_change_cb.isChecked():
            cts.Change_Sign = True

        if not self.angl_intg_cb.isChecked():
            cts.Add_angl_intg = False
        if not self.sign_change_cb.isChecked():
            cts.Change_Sign = False
        print('OKOK')

        try:
            w = plSB.plot_SBphase_VS_angle_Win(self)  # new class defined in another file
        except Exception:
            print(traceback.format_exception(*sys.exc_info()))



        #

    def plot_Rainbow_Rab(self):
            Phase_offset = cts.phaseshift_for_3D_plots
            c00_2w_P0 = cts.Rainbow_2w_P0
            c00_2w_P2 = cts.Rainbow_2w_P2
            c00_2w_P4 = cts.Rainbow_2w_P4
            istart = 3
            istop = np.shape(c00_2w_P0)[0]
            N_c = 1

            energy = c00_2w_P0[istart:istop, 0]
            theta = np.linspace(0, np.pi / 2, 360,
                                endpoint=False)  # sampling of emission angle. It goes from 0 to 90°, there are 360 points.

            ee, tt = np.meshgrid(energy, theta)

            A0 = c00_2w_P0[istart:istop, 1]
            A2 = c00_2w_P2[istart:istop, 1]
            A4 = c00_2w_P4[istart:istop, 1]

            Phi0 = c00_2w_P0[istart:istop, 2]
            Phi2 = c00_2w_P2[istart:istop, 2]
            Phi4 = c00_2w_P4[istart:istop, 2]

            A0 = np.convolve(A0, np.ones((N_c,)) / N_c, mode='same')  # N_c = 1 : just changes column to vector
            A2 = np.convolve(A2, np.ones((N_c,)) / N_c, mode='same')
            A4 = np.convolve(A4, np.ones((N_c,)) / N_c, mode='same')

            Phi0 = np.convolve(Phi0, np.ones((N_c,)) / N_c, mode='same')
            Phi2 = np.convolve(Phi2, np.ones((N_c,)) / N_c, mode='same')
            Phi4 = np.convolve(Phi4, np.ones((N_c,)) / N_c, mode='same')

            alpha = A0 * np.cos(Phi0) * sp.eval_legendre(0, np.cos(tt)) + \
                    A2 * np.cos(Phi2) * sp.eval_legendre(2, np.cos(tt)) + \
                    A4 * np.cos(Phi4) * sp.eval_legendre(4, np.cos(tt))

            beta = A0 * np.sin(Phi0) * sp.eval_legendre(0, np.cos(tt)) + \
                   A2 * np.sin(Phi2) * sp.eval_legendre(2, np.cos(tt)) + \
                   A4 * np.sin(Phi4) * sp.eval_legendre(4, np.cos(tt))

            Phi = np.zeros(np.shape(alpha))
            for j in range(energy.shape[0]):
                for i in range(0, theta.shape[0]):
                    Phi[i, j] = math.atan2(beta[i, j], alpha[i, j]) + Phase_offset
            #
            # # these loops are tricks to fold the phases of the arctan function (like wrap2pmpi but the arctan(beta/alpha) is pi-periodiq
            # #if from an angle to the next the phase jumps more than a certain amount (+/- arbitrary), we change the phase. Gives smooth phase evolution / theta
            for j in range(energy.shape[0]):
                if A0[j] < 0.005 * max(
                        A0):  # if te amplitude is to small, the phase is put to 0 as it has no meaning anyways
                    Phi[:, j] = 0
                else:
                    for i in range(1, theta.shape[0]):
                        if Phi[i, j] - Phi[i - 1, j] > (np.pi / 2 - 0.8):
                            while Phi[i, j] - Phi[i - 1, j] > (np.pi / 2 - 0.8):
                                Phi[i, j] -= np.pi
                        elif Phi[i, j] - Phi[i - 1, j] < -1 * (np.pi / 2 - 0.8):
                            while Phi[i, j] - Phi[i - 1, j] < -1 * (np.pi / 2 - 0.8):
                                Phi[i, j] += np.pi
                        else:
                            pass

            Ampl = np.sqrt(alpha ** 2 + beta ** 2)

            cts.Phi_Rainbow = np.array(Phi)
            cts.Ampl_Rainbow = np.array(Ampl)


            self.phase_ax.cla()
            self.phase_ax.set_xlabel("Photon Energy [eV]")
            self.phase_ax.set_ylabel("2w Phase [rad]")
            self.FT_ax.cla()

            self.FT_ax.set_xlabel("Photon Energy [eV]")
            self.FT_ax.set_ylabel("2w amplitude [arb. u.]")

            for theta_k in cts.angles_for_plots:  # full range 0 to 360, step of 40 => 10° steps
                theta_k_360 = int(theta_k *360/90)
                ampl_theta = Ampl[theta_k_360, :]
                if self.phasewrap_cb.isChecked():
                    Phi_theta = af.wrap2pmpi(cts.Phi_Rainbow[theta_k_360, :])
                else:
                    Phi_theta = cts.Phi_Rainbow[theta_k_360, :]
                self.phase_ax.plot(energy, Phi_theta,markersize=4)
                self.FT_ax.plot(energy, ampl_theta, label='2w ampl. at angle '+str(theta_k)+'°')

                # # if keep_lims:
                # self.phase_ax.set_xlim(xmin_ph, xmax_ph)
                # self.phase_ax.set_ylim(ymin_ph, ymax_ph)
                # self.FT_ax.set_xlim(xmin_FT, xmax_FT)
                # self.FT_ax.set_ylim(ymin_FT, ymax_FT)

                self.FT_ax.legend(fontsize=10)
                self.phase_fc.draw()
                self.FT_fc.draw()
