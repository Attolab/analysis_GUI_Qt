import sys, traceback
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QGridLayout, QHBoxLayout, QVBoxLayout, QGroupBox, QLabel
from PyQt5.QtWidgets import QLineEdit, QSplitter, QFrame, QCheckBox, QButtonGroup, QRadioButton
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT
from matplotlib.figure import Figure
import numpy as np

# Homemade modules
import glob_var as cts
import other_widgets as ow
import _import_export as ie
from VMI_analysis import _VMI_functions as VMIf
from VMI_analysis import plot_3D_phase_angle_energy_win as pl3D
# from VMI_analysis import plot_SBphase_VS_angle_win as plSB


class VmiWin(QWidget, ie.Imp_Exp_Mixin, VMIf.VMI_functions_mixin):
    """ Rabbit window

        For the names of the children widgets, I tried to put suffixes that indicate clearly their types:
        *_btn -> QPushButton,
        *_le -> QLineEdit,
        *_lb -> QLabel,
        *layout -> QHBoxLayout, QVBoxLayout or QGridLayout,
        *_box -> QGroupBox,
        *_cb -> QCheckBox,
        *_rb -> QRadioButton

        The functions that are connected to a widget's event have the suffix _lr (for 'listener'). For example,
        a button named test_btn will be connected to a function test_lr.
        Some functions may be connected to widgets but without the suffix _lr in their names. It means that they
        are not only called when interacting with the widget.

        In this file are defined the graphical objects and a few simple functions. The other functions
        (like the analysis ones) are defined in the "_Rabbit_functions.py" file
        """

    ##################################################################################
    ############################ Widget Initialization ###############################

    def __init__(self, parent=None):
        """Initialization of the window

                the main layout is called mainLayout. It is divided in two:
                    - graphLayout: the left part, contains all the figures
                    - commandLayout: the right part, contains all the buttons, fields, checkboxes...
                Both graphLayout and commandLayout are divided into sub-layouts.

                This function calls several functions to initialize each part of the window.
                The name of these functions has the shape 'init_*layout'."""
        super(VmiWin, self).__init__(parent=parent)
        self.setWindowTitle("RABBIT")
        self.mainlayout = QHBoxLayout()
        self.graphlayout = QVBoxLayout()
        self.commandLayout = QVBoxLayout()
        self.commandLayout.setSpacing(10)

        self.init_importlayout()
        self.init_anglechoice()
        self.init_rainbowlayout()
        self.init_phase_per_SB()
        self.init_graphlayout()

        self.mainlayout.addWidget(self.splitter2)
        self.mainlayout.addLayout(self.commandLayout)
        self.setLayout(self.mainlayout)
        self.show()


    def init_importlayout(self):
        ''' In commandLayout - Initialization of the "Import" section'''
        Importlayout = QGridLayout()
        Importlayout.setSpacing(10)

        Import_box = QGroupBox(self)
        Import_box.setTitle("Import")
        Import_box.setFixedSize(300, 160)

        self.importVMI_P0_btn = QPushButton("P0 matrix", self)
        self.importVMI_P2_btn = QPushButton("P2 matrix", self)
        self.importVMI_P4_btn = QPushButton("P4 matrix", self)


        self.importVMI_P0_Rainbow_btn = QPushButton("P0 2w Rainbow", self)
        self.importVMI_P2_Rainbow_btn = QPushButton("P2 2w Rainbow", self)
        self.importVMI_P4_Rainbow_btn = QPushButton("P4 2w Rainbow", self)

        self.importVMI_P0_std_btn = QPushButton("P0 2w Normal", self)
        self.importVMI_P2_std_btn = QPushButton("P2 2w Normal", self)
        self.importVMI_P4_std_btn = QPushButton("P4 2w Normal", self)

        self.import2w_std_ang_btn = QPushButton("2w Std ang intg.", self)


        # self.vrep_le = QLineEdit(str(cts.vrep), self)
        self.ang_filenametype_le = QLineEdit(str(cts.ang_filenametype), self)

        self.importVMI_P0_btn.clicked.connect(self.import_P0_matrix)
        self.importVMI_P2_btn.clicked.connect(self.import_P2_matrix)
        self.importVMI_P4_btn.clicked.connect(self.import_P4_matrix)

        self.importVMI_P0_Rainbow_btn.clicked.connect(self.import_P0_Rainbow)
        self.importVMI_P2_Rainbow_btn.clicked.connect(self.import_P2_Rainbow)
        self.importVMI_P4_Rainbow_btn.clicked.connect(self.import_P4_Rainbow)

        self.importVMI_P0_std_btn.clicked.connect(self.import_P0_std)
        self.importVMI_P2_std_btn.clicked.connect(self.import_P2_std)
        self.importVMI_P4_std_btn.clicked.connect(self.import_P4_std)

        self.import2w_std_ang_btn.clicked.connect(self.import2w_std_ang)
        # self.vrep_le.returnPressed.connect(self.update_vrep)

        Importlayout.addWidget(self.importVMI_P0_btn, 0, 0)
        Importlayout.addWidget(self.importVMI_P2_btn, 0, 1)
        Importlayout.addWidget(self.importVMI_P4_btn, 0, 2)

        Importlayout.addWidget(self.importVMI_P0_Rainbow_btn, 1, 0)
        Importlayout.addWidget(self.importVMI_P2_Rainbow_btn, 1, 1)
        Importlayout.addWidget(self.importVMI_P4_Rainbow_btn, 1, 2)

        Importlayout.addWidget(self.importVMI_P0_std_btn, 2, 0)
        Importlayout.addWidget(self.importVMI_P2_std_btn, 2, 1)
        Importlayout.addWidget(self.importVMI_P4_std_btn, 2, 2)

        Importlayout.addWidget(QLabel("ang. filenametype:"), 3, 0)
        Importlayout.addWidget(self.ang_filenametype_le, 3, 1)
        Importlayout.addWidget(self.import2w_std_ang_btn, 3, 2)


        Import_box.setLayout(Importlayout)
        self.commandLayout.addWidget(Import_box)

        for widget in Import_box.children():
            if isinstance(widget, QPushButton):
                widget.setSizePolicy(0, 0)
                widget.setEnabled(False)

        self.ang_filenametype_le.setSizePolicy(0, 0)
        self.ang_filenametype_le.setFixedSize(80, 20)

        for widget in Import_box.children():
            if isinstance(widget, QPushButton):
                widget.setSizePolicy(0, 0)
                widget.setEnabled(False)


        self.importVMI_P0_btn.setEnabled(True)
        self.importVMI_P2_btn.setEnabled(True)
        self.importVMI_P4_btn.setEnabled(True)
        self.importVMI_P0_Rainbow_btn.setEnabled(True)
        self.importVMI_P0_std_btn.setEnabled(True)
        self.import2w_std_ang_btn.setEnabled(True)


        self.ang_filenametype_le.returnPressed.connect(self.update_ang_filenametype)


    def init_anglechoice(self):
        ''' In anglechoice - Choice of angles and intervals of desired 'angle integrated' points'''
        anglechoicelayout = QGridLayout()
        anglechoicelayout.setSpacing(10)

        anglechoice_box = QGroupBox(self)
        anglechoice_box.setTitle("Angular integration (default : 0°, 10°,20°...,80°)")
        anglechoice_box.setFixedSize(300, 100)



        self.import_angle_list_btn = QPushButton("Start of intervals (°)", self)
        self.exportS3D_btn = QPushButton("Save ang. intg. matrices", self)
        self.angle_width_le = QLineEdit("{:.2f}".format(cts.angle_width), self)

        self.angle_width_le.returnPressed.connect(self.update_angle_width_fn)
        self.exportS3D_btn.clicked.connect(self.exportS3D_lr)
        self.import_angle_list_btn.clicked.connect(self.import_angle_list)

        anglechoicelayout.addWidget(self.import_angle_list_btn, 0, 0)
        anglechoicelayout.addWidget(self.exportS3D_btn, 1, 0)
        anglechoicelayout.addWidget(QLabel("Interval width (°)"), 0, 1)
        anglechoicelayout.addWidget(self.angle_width_le, 0, 2)

        anglechoice_box.setLayout(anglechoicelayout)
        self.commandLayout.addWidget(anglechoice_box)

        for widget in anglechoice_box.children():
            if isinstance(widget, QPushButton):
                widget.setSizePolicy(0, 0)
                widget.setEnabled(False)


        self.import_angle_list_btn.setEnabled(True)
        self.exportS3D_btn.setEnabled(True)

    def init_rainbowlayout(self):
        ''' In commandLayout - Initialization of the "Rainbow rabbit plots" section'''
        rabbitlayout = QGridLayout()
        rabbit_box = QGroupBox("Rainbow RABBIT plots", self)
        rabbit_box.setFixedSize(300, 250)

        self.angles_for_plot_btn = QPushButton("Angles for plot", self)
        self.phasewrap_cb = QCheckBox("Wrap phase", self)
        self.set_phaseshift_le = QLineEdit("0", self)
        self.smoothfactor_le = QLineEdit("{:.2f}".format(cts.smoothfactor), self)
        self.energy_min_le = QLineEdit("{:.2f}".format(cts.energy_min_for_3D), self)
        self.energy_max_le = QLineEdit("{:.2f}".format(cts.energy_max_for_3D), self)
        self.theta_min_le = QLineEdit("{:.2f}".format(cts.theta_min_for_3D), self)
        self.theta_max_le = QLineEdit("{:.2f}".format(cts.theta_max_for_3D), self)
        self.plot_Rainbow_Rab_btn = QPushButton("2w Rainbow", self)
        self.plot_Rainbow3D_Rab_btn = QPushButton("2w phase 3D", self)

        self.angles_for_plot_btn.clicked.connect(self.angles_for_plot)
        self.plot_Rainbow_Rab_btn.clicked.connect(self.plot_Rainbow_Rab)
        self.plot_Rainbow3D_Rab_btn.clicked.connect(self.plot_Rainbow3D_Rab)
        self.set_phaseshift_le.returnPressed.connect(self.update_phaseshift_fn)
        self.smoothfactor_le.returnPressed.connect(self.update_smoothfactor_fn)
        self.energy_min_le.returnPressed.connect(self.update_energy_min_fn)
        self.energy_max_le.returnPressed.connect(self.update_energy_max_fn)
        self.theta_min_le.returnPressed.connect(self.update_theta_min_fn)
        self.theta_max_le.returnPressed.connect(self.update_theta_max_fn)


        rabbitlayout.addWidget(self.angles_for_plot_btn, 0, 0)
        rabbitlayout.addWidget(self.phasewrap_cb, 1, 0)
        rabbitlayout.addWidget(QLabel("Cst shift (rad)"), 0, 1)
        rabbitlayout.addWidget(self.set_phaseshift_le, 1, 1)
        rabbitlayout.addWidget(QLabel("Smooth factor"), 0, 2)
        rabbitlayout.addWidget(self.smoothfactor_le, 1, 2)
        rabbitlayout.addWidget(QLabel("2D plot :"), 2, 0)
        rabbitlayout.addWidget(self.plot_Rainbow_Rab_btn, 2, 1)
        rabbitlayout.addWidget(QLabel("3D plot :"), 3, 0)
        rabbitlayout.addWidget(QLabel("Energy min (eV)"), 4, 0)
        rabbitlayout.addWidget(QLabel("Energy max (eV)"), 4, 1)
        rabbitlayout.addWidget(self.energy_min_le, 5, 0)
        rabbitlayout.addWidget(self.energy_max_le, 5, 1)
        rabbitlayout.addWidget(QLabel("Theta min (°)"), 6, 0)
        rabbitlayout.addWidget(QLabel("Theta max (°)"), 6, 1)
        rabbitlayout.addWidget(self.theta_min_le, 7, 0)
        rabbitlayout.addWidget(self.theta_max_le, 7, 1)
        rabbitlayout.addWidget(self.plot_Rainbow3D_Rab_btn, 7, 2)

        rabbit_box.setLayout(rabbitlayout)

        for widget in rabbit_box.children():
            if isinstance(widget, QPushButton):
                widget.setSizePolicy(0, 0)
                widget.setEnabled(False)

        self.angles_for_plot_btn.setEnabled(True)
        self.commandLayout.addWidget(rabbit_box)



    def init_phase_per_SB(self):
        ''' In phase_per_SB - plots the SB phase evolytion as a function of the em angle '''
        phase_per_SBlayout = QGridLayout()
        phase_per_SBlayout.setSpacing(10)

        phase_per_SB_box = QGroupBox(self)
        phase_per_SB_box.setTitle("Standard RABBIT Phase VS angle")
        phase_per_SB_box.setFixedSize(300, 150)

        self.plot_phVSangle_btn = QPushButton("Plot", self)
        self.save_phVSangle_btn = QPushButton("Save", self)
        self.angl_intg_cb = QCheckBox("Angle intg", self)

        self.SBi_le = QLineEdit(str(cts.first_harm + 1), self)
        self.SBi_le.returnPressed.connect(self.SBi_lr)
        self.SBi_choice_le = QLineEdit(str(cts.first_harm + 1), self)
        self.SBi_choice_le.returnPressed.connect(self.SBi_choice_lr)
        self.plot_phVSangle_btn.clicked.connect(self.plot_phVSangle)
        self.save_phVSangle_btn.clicked.connect(self.save_phVSangle)
        self.sign_change_cb = QCheckBox("Change phase sign", self)

        phase_per_SBlayout.addWidget(QLabel("first SB:"), 0, 0)
        phase_per_SBlayout.addWidget(self.SBi_le, 0, 1)
        phase_per_SBlayout.addWidget(QLabel("SB of choice:"), 1, 0)
        phase_per_SBlayout.addWidget(self.SBi_choice_le, 1, 1)
        phase_per_SBlayout.addWidget(self.sign_change_cb, 1, 2)
        phase_per_SBlayout.addWidget(self.plot_phVSangle_btn, 2, 0)
        phase_per_SBlayout.addWidget(self.save_phVSangle_btn, 2, 1)
        phase_per_SBlayout.addWidget(self.angl_intg_cb, 0, 2)

        phase_per_SB_box.setLayout(phase_per_SBlayout)
        self.commandLayout.addWidget(phase_per_SB_box)
        #
        # for widget in phase_per_SB_box.children():
        #     if isinstance(widget, QPushButton):
        #         widget.setSizePolicy(0, 0)
        #         widget.setEnabled(False)



    def init_graphlayout(self):
        ''' In graphLayout - Initialization of the 3 figures'''
        self.splitter1 = QSplitter(Qt.Horizontal)
        self.splitter2 = QSplitter(Qt.Vertical)

        self.rab_widget = ow.plot3DWidget(self) # new class defined in other_widgets.py
        # self.rab_widget.fc.mpl_connect('button_press_event', self.onclick)
        self.rab_widget.xlabel = "E [eV]"
        self.rab_widget.ylabel = "t [fs]"

        self.phaselayout = QVBoxLayout()
        self.phase_frame = QFrame()
        self.phase_frame.setLayout(self.phaselayout)

        phase_fig = Figure(figsize=(2, 2), dpi=100)
        self.phase_fc = FigureCanvas(phase_fig)
        self.phase_fc.setSizePolicy(1, 1)
        # self.phase_fc.mpl_connect('button_press_event', self.onclick)
        self.phase_ax = self.phase_fc.figure.add_subplot(111)
        self.phase_ax.tick_params(labelsize = 10)
        nav = NavigationToolbar2QT(self.phase_fc, self)
        nav.setStyleSheet("QToolBar { border: 0px }")
        self.phaselayout.addWidget(self.phase_fc)
        self.phaselayout.addWidget(nav)
        self.phase_fc.draw()

        self.FTlayout = QVBoxLayout()
        self.FT_frame = QFrame()
        self.FT_frame.setLayout(self.FTlayout)
        FT_fig = Figure(figsize=(2, 2), dpi=100)
        self.FT_fc = FigureCanvas(FT_fig)
        self.FT_fc.setSizePolicy(1, 1)
        # self.FT_fc.mpl_connect('button_press_event', self.onclick)
        self.FT_ax = self.FT_fc.figure.add_subplot(111)
        self.FT_ax.tick_params(labelsize = 10)
        nav2 = NavigationToolbar2QT(self.FT_fc, self)
        nav2.setStyleSheet("QToolBar { border: 0px }")
        self.FTlayout.addWidget(self.FT_fc)
        self.FTlayout.addWidget(nav2)
        self.int_rab_cb = QCheckBox("Delay integrated trace")
        self.int_rab_cb.setEnabled(False)
        self.int_rab_cb.stateChanged.connect(self.int_rab_lr)
        self.FTlayout.addWidget(self.int_rab_cb)
        self.FT_fc.draw()

        self.splitter1.addWidget(self.phase_frame)
        self.splitter1.addWidget(self.FT_frame)

        self.splitter2.addWidget(self.rab_widget)
        self.splitter2.addWidget(self.splitter1)

#################################################################################
############################ Other methods ######################################


    def update_ang_filenametype(self):
        cts.ang_filenametype = self.ang_filenametype_le.text()

    # def update_angle_list(self):
    #     cts.angle_list = self.angle_list_le.text()

    def update_angle_width_fn(self):
        cts.angle_width = float(self.angle_width_le.text())

    def update_phaseshift_fn(self):
        cts.phaseshift_for_3D_plots = float(self.set_phaseshift_le.text())

    def update_smoothfactor_fn(self):
        cts.smoothfactor = int(self.smoothfactor_le.text())

    def update_energy_min_fn(self):
        cts.energy_min_for_3D = float(self.energy_min_le.text())

    def update_energy_max_fn(self):
        cts.energy_max_for_3D = float(self.energy_max_le.text())

    def update_theta_min_fn(self):
        cts.theta_min_for_3D = float(self.theta_min_le.text())

    def update_theta_max_fn(self):
        cts.theta_max_for_3D = float(self.theta_max_le.text())


    def int_rab_lr(self):
        self.refreshplot(keep_lims=True)

    def bandsnb_lr(self):
        ''' called when pressing enter in the bandsnb_le object'''
        try:
            cts.bandsnb = int(self.bandsnb_le.text())
            self.window().updateglobvar_fn()
            cts.bands_vect = np.zeros([cts.bandsnb, 2])
        except ValueError:
            self.window().statusBar().showMessage("Number of bands must be an integer")

    def SBi_lr(self):
        try:
            cts.SBi = float(self.SBi_le.text())
        except ValueError:
            self.window().statusBar().showMessage("SBi must be a number")

    def SBi_choice_lr(self):
        try:
            cts.SBi_choice = float(self.SBi_choice_le.text())
        except ValueError:
            self.window().statusBar().showMessage("SBi must be a number")


    def plotSBvsdelay_lr(self):
        ''' "[plot] SB vs delay" button listener. Opens a new window'''
        try:
            w = sbdw.SBvsDelayWin(self) # new class defined below
        except Exception:
            print(traceback.format_exception(*sys.exc_info()))

    def plot_3D_phase_angle_energy_lr(self):
        ''' "[plot] SB vs delay" button listener. Opens a new window'''
        try:
            w = pl3D.plot_3D_phase_angle_energy_Win(self) # new class defined in separate file
        except Exception:
            print(traceback.format_exception(*sys.exc_info()))



    def reset_btn(self):
        ''' "Reset" button listener. Resets the widgets, not the variables'''
        self.importXUV_btn.setEnabled(False)
        self.importdata_btn.setEnabled(False)
        self.importVMI_P2_Rainbow_btn.setEnabled(False)
        self.importVMI_P4_Rainbow_btn.setEnabled(False)

        self.normalrab_btn.setEnabled(False)
        self.rainbowrab_btn.setEnabled(False)
        self.exportrab_btn.setEnabled(False)
        self.plotSBvsdelay_btn.setEnabled(False)

        self.rab_widget.colorauto_cb.setEnabled(False)
        self.rab_widget.logscale_cb.setEnabled(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VmiWin()
    sys.exit(app.exec_())












