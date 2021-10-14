# Plot_3D_win

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QCheckBox, QGridLayout
from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT
from PyQt5.QtWidgets import QTableWidgetItem, QTableView, QTableWidget
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy import optimize as opt

import glob_var as cts


class plot_3D_phase_angle_energy_Win(QDialog):
    ''' created when clicking on the "[plot] SB vs delay" button'''
    def __init__(self, parent): # parent=RabbitWin
        super(plot_3D_phase_angle_energy_Win, self).__init__(parent)
        self.setGeometry(300, 300, 1000, 500)
        self.setWindowFlags(Qt.Window)
        self.par = parent
        self.mainlayout = QHBoxLayout()
        self.init_var()
        self.init_graphlayout()
        self.setLayout(self.mainlayout)
        self.show()

    def init_var(self):
        self.X = cts.X
        self.Y = cts.Y
        self.Z = cts.Z
        self.N_c = cts.smoothfactor
        self.Z2 = np.zeros(np.shape(self.Z))
        for k in range(0, np.shape(self.Z)[0]):
            self.Line = self.Z[k, :]
            self.Line2 = np.convolve(self.Line, np.ones((self.N_c,)) / self.N_c, mode='same')
            self.Z2[k, :] = self.Line2
        self.parent().window().updateglobvar_fn()

    def init_graphlayout(self) -> None:

        self.graphlayout = QVBoxLayout()
        fig = Figure(figsize=(4, 3), dpi=100)
        self.fc = FigureCanvas(fig)
        self.ax = Axes3D(fig)
        self.fc.draw()
        nav = NavigationToolbar2QT(self.fc, self)
        nav.setStyleSheet("QToolBar { border: 0px }")
        self.surf = self.ax.plot_surface(self.X, self.Y, self.Z2, cmap='jet', vmin = -np.pi, vmax = np.pi)
        fig.colorbar(self.surf, shrink=0.5, aspect=5, label='Phase [rad]')
        self.ax.set_xlabel('Energy [eV]')
        self.ax.set_ylabel('Angle [°]')
        self.ax.set_zlabel('Phase [rad]')

        print('OK init_graphlayout')
        self.graphlayout.addWidget(self.fc)
        self.graphlayout.addWidget(nav)
        self.mainlayout.addLayout(self.graphlayout)

