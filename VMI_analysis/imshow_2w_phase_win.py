# # Plot_SB_vs_angle_win

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QCheckBox, QGridLayout
from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT
from PyQt5.QtWidgets import QTableWidgetItem, QTableView, QTableWidget
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy import optimize as opt
import matplotlib
import glob_var as cts


class imshow_2w_phase_Win(QDialog):
    ''' created when clicking on the "[plot] SB vs delay" button'''
    def __init__(self, parent): # parent=RabbitWin

        self.init_var()
        self.init_graphlayout()
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
        # self.parent().window().updateglobvar_fn()

    def init_graphlayout(self) -> None:
        fig = matplotlib.pyplot.figure()
        matplotlib.pyplot.imshow(self.Z2, cmap='jet', aspect='auto', extent = (self.X[0,0], self.X[0,-1], self.Y[-1,0], self.Y[0,0]))
        cbar = matplotlib.pyplot.colorbar()
        cbar.set_label('Phase [rad]')
        matplotlib.pyplot.xlabel('Energy [eV]')
        matplotlib.pyplot.ylabel('Emission angle [°]')
        matplotlib.pyplot.title('2w phase as a function of energy and emission angle')
