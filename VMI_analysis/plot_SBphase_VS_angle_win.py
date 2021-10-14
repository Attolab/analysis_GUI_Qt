# # Plot_SB_vs_angle_win

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QCheckBox, QGridLayout
from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT
from PyQt5.QtWidgets import QTableWidgetItem, QTableView, QTableWidget
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize as opt

import glob_var as cts


class plot_SBphase_VS_angle_Win(QDialog):
    ''' created when clicking on the "[plot] SB vs delay" button'''
    def __init__(self, parent): # parent=RabbitWin
        super(plot_SBphase_VS_angle_Win, self).__init__(parent)
        self.setGeometry(300, 300, 500, 500)
        self.setWindowFlags(Qt.Window)
        self.par = parent
        self.mainlayout = QHBoxLayout()
        self.init_var()
        self.init_graphlayout()
        self.setLayout(self.mainlayout)
        self.show()

    def init_var(self):
        self.tt = cts.tt_angles*180/np.pi
        self.angles_width = cts.angle_width
        self.angles = [cts.angle_list[k] + self.angles_width / 2 for k in range(0, len(cts.angle_list))]

        self.Phi = cts.Phi
        self.DPhi = cts.DPhi
        self.SB_i = cts.sb_order.index(cts.SBi_choice)
        if cts.Add_angl_intg:
            self.Phi_rec = cts.data_2w_std_ang[:, int(self.SB_i), 3]
            if cts.Change_Sign:
                self.Phi_rec = - cts.data_2w_std_ang[:, int(self.SB_i), 3]
            self.Phi_rec_err = cts.data_2w_std_ang[:, int(self.SB_i), 4]
        self.parent().window().updateglobvar_fn()

    def init_graphlayout(self) -> None:
        self.graphlayout = QVBoxLayout()

        fig = Figure(figsize=(4, 3), dpi=100)
        self.fc = FigureCanvas(fig)
        self.ax = self.fc.figure.add_subplot(111)
        self.fc.draw()
        nav = NavigationToolbar2QT(self.fc, self)
        nav.setStyleSheet("QToolBar { border: 0px }")
        self.ax.fill_between(self.tt, (self.Phi- self.Phi[0]-self.DPhi), (self.Phi - self.Phi[0] + self.DPhi), alpha=0.3)
        # self.ax.fill_between(self.tt, (- self.DPhi), ( self.DPhi),
        #                      alpha=0.3)
        self.ax.plot(self.tt, self.Phi - self.Phi[0])
        if cts.Add_angl_intg:
            print(np.shape(self.angles))
            print(np.shape(self.Phi_rec))
            self.ax.errorbar(self.angles, self.Phi_rec - self.Phi_rec[0] , xerr=[self.angles_width for k in range(0, len(self.angles))], yerr=self.Phi_rec_err,fmt='s', markersize=7, elinewidth=2)
        self.ax.set_xlabel('Angle [°]')
        self.ax.set_ylabel('Phase [rad]')
        print('OK init_graphlayout')
        self.graphlayout.addWidget(self.fc)
        self.graphlayout.addWidget(nav)
        self.mainlayout.addLayout(self.graphlayout)

