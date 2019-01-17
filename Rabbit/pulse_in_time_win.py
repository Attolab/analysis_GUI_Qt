# pulse_in_time_win

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QCheckBox, QGridLayout
from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT
from PyQt5.QtWidgets import QTableWidgetItem, QTableView, QTableWidget
from matplotlib.figure import Figure

import numpy as np
import glob_var as cts

class PulseInTimeWin(QDialog):
    ''' created when clicking on the "Pulse in Time" button'''
    def __init__(self, parent): # parent=RabbitWin
        super(PulseInTimeWin, self).__init__(parent)
        self.setGeometry(300, 300, 1000, 500)
        self.setWindowFlags(Qt.Window)

        self.par = parent
        self.mainlayout = QHBoxLayout()

        self.init_graphlayout()
        self.refreshplot_fn()

        self.setLayout(self.mainlayout)
        self.show()

    def init_graphlayout(self) -> None:
        self.graphlayout = QVBoxLayout()

        fig = Figure(figsize=(4, 3), dpi=100)
        self.fc = FigureCanvas(fig)
        self.ax = self.fc.figure.add_subplot(111)
        self.fc.draw()

        self.graphlayout.addWidget(self.fc)

        self.mainlayout.addLayout(self.graphlayout)

    def refreshplot_fn(self) -> None:
        time_axis = np.arange(0, 5e-15, 1e-18)

        try:
            self.ax.cla()
            self.ax.set_xlabel("Time", fontsize=10)
            self.ax.set_ylabel("Intensity", fontsize=10)

            self.ax.plot(time_axis, self.temporal_profile_fn(time_axis))

            self.fc.draw()

        except Exception:
           print(traceback.format_exception(*sys.exc_info()))

    # This fonction calculates the intensity of the pulse. It uses cts.peak_phase
    # which contains the spectral dephasings between two consecutive harmonics
    # We suppose that it has the form cts.peak_phase = [phase_SB_14, phase_SB_16, …]
    def temporal_profile_fn(self, time):

        harmonics_spectral_phases = []

        # In this loop we calculate the harmonics spectral phases.
        # The first harmonic phase is zero by convention.
        # We suppose that phase_SB_q+1 = phase_q - phase_q+2.
        for i in range(cts.bandsnb + 1):
            spectral_phase = 0.0

            for j in range(i):
                spectral_phase -= cts.peak_phase[j]

            harmonics_spectral_phases.append(spectral_phase)

        # Construct the amplitudes of the harmonics
        h_nu = cts.HEV * cts.cur_nu
        harmonics_amplitudes = []

        for i in range(cts.bandsnb + 1):
            harmonic_energy_argument = np.argmin(abs(cts.energy_vect - (cts.first_harm + 2 * i) * h_nu))
            # harmonics_energy_arguments.append(harmonic_energy_argument)
            # harmonics_energies.append(cts.energy_vect[harmonic_energy_argument])
            # We take arbitrarily the amplitudes of the harmonics at delay zero
            harmonics_amplitudes.append(cts.rabbit_mat[0, harmonic_energy_argument])

        print(harmonics_amplitudes)

        # fields_sum is the sum of the fields of each harmonic
        fields_sum = 0.0

        for i in range(cts.bandsnb + 1):
            fields_sum += harmonics_amplitudes[i] * np.exp(- 2 * 1j * np.pi * (cts.first_harm + 2*i) * cts.cur_nu * time + harmonics_spectral_phases[i])

        # Return the calculated field
        return np.real(fields_sum)
