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
            self.ax.set_ylabel("XUV", fontsize=10)

            self.ax.plot(time_axis, self.temporal_profile_fn(time_axis, "Field"), label="Field")
            self.ax.plot(time_axis, self.temporal_profile_fn(time_axis, "Intensity"), label="Intensity")

            self.ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=7, mode="expand", borderaxespad=0.)

            self.fc.draw()

        except Exception:
           print(traceback.format_exception(*sys.exc_info()))

    # This fonction calculates the field of the pulse. It uses cts.peak_phase
    # which contains the spectral dephasings between two consecutive harmonics
    # We suppose that it has the form cts.peak_phase = [phase_SB_14, phase_SB_16, …]
    def temporal_profile_fn(self, time, representation):

        harmonics_spectral_phases = []

        ### In this loop we calculate the harmonics spectral phases.

        # The intensity of the sidebands is given by I_SB_2q = A + B cos (2*omega*tau + phase_SB_2q)
        # We suppose phase_SB_2q = - phase_harm_2q+1 + phase_harm_2q-1 and neglect the atomic phase.
        # The first harmonic phase is said to be zero and give a phase reference.
        for k in range(cts.bandsnb + 1):
            spectral_phase = 0.0

            for l in range(k):
                spectral_phase -= cts.peak_phase[l]

            harmonics_spectral_phases.append(spectral_phase)

        ### In this loop we calculate the amplitudes of the harmonics

        h_nu = cts.HEV * cts.cur_nu # Energy of an IR photon in eV
        harmonics_amplitudes = []

        for k in range(cts.bandsnb + 1):
            # Find the argument of energy_vect which corresponds to the closest value of the harmonic energy
            harmonic_energy_argument = np.argmin(abs(cts.energy_vect - (cts.first_harm + 2*k)*h_nu))
            # We take the mean value of the harmonic amplitude over the delay and take the square root
            harmonics_amplitudes.append(
                np.sqrt(
                    np.mean(
                        cts.rabbit_mat[:, harmonic_energy_argument]
                    )
                )
            )

        ### In this loop we calculate the XUV field

        # XUV field is the sum of the fields of each harmonic
        XUV_field = 0.0

        for k in range(cts.bandsnb + 1):
            XUV_field += harmonics_amplitudes[k]*np.exp(1j*(
                2*np.pi*cts.cur_nu*(cts.first_harm + 2*k)*time
                + harmonics_spectral_phases[k]
            ))

        if representation == "Field":
            # Return the XUV field
            return np.real(XUV_field)

        elif representation == "Intensity":
            # Return the XUV intensity
            return np.abs(XUV_field)
