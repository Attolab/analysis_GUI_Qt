
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QToolButton,
    QVBoxLayout, QWidget)
from .ui.calibration_panel_ui import Ui_Calibration_Panel
import pyqtgraph as pg
from random import randint
import numpy as np
from functools import partial


class CalibrationPanel(QWidget,Ui_Calibration_Panel):
    def __init__(self,parent=None):
        super(CalibrationPanel, self).__init__(parent)
        self.x = np.arange(100)*1.0  # 100 time points
        self.y = 2*self.x  # 100 data point        
        self.coeff_TOF = np.array([0 , 0 , 0])
        self.setupUi(self)
        self.setupWidgets()
        self.connectButtons()
        self.makeGraph()
        self.updateGraph()


    def connectButtons(self):
        self.closeButton.clicked.connect(self.closeButton_func)
        self.applyButton.clicked.connect(self.applyButton_func)
        self.saveButton.clicked.connect(self.saveButton_func)
        self.t0_value.textEdited.connect(partial(self.updateCoeff,0))
        self.kE_value.textEdited.connect(partial(self.updateCoeff,1))
        self.kV_value.textEdited.connect(partial(self.updateCoeff,2))
        

    
    def updateCoeff(self,ind,text):
        self.coeff_TOF[ind] = float(text)
        self.updateGraph()

        # print(f'coeff = { self.coeff_TOF}')
    def closeButton_func(self):
        self.close() 
    def applyButton_func(self):
        self.updateGraph()
    def saveButton_func(self):
        return None    

    def setupWidgets(self):
        styles = {'color':'r', 'font-size':'10px'}
        self.ToF_axis.setBackground('w')
        self.ToF_axis.setLabel('left', 'Counts', **styles)
        self.ToF_axis.setLabel('bottom', 'Energy (eV)', **styles)
        self.ToF_axis.setLabel('top', 'Time (ns)', **styles)
    def makeGraph(self):
        self.pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  self.ToF_axis.plot(self.x, self.y, pen=self.pen,labels = self.x)

    def updateGraph(self):
        self.data_line.setData((self.x - self.coeff_TOF[0])*self.coeff_TOF[1], self.y) 
        # ax_b=self.ToF_axis.getAxis('bottom')
        # spacing = 10
        
        # E_labels = [
        #     # Generate a list of tuples (x_value, x_label)
        #     (m , str(2*m))
        #     for m in self.x[0::spacing]
        # ]        
        # ax_b.setTicks([E_labels])



def main():
    app = QApplication([])
    tof = CalibrationPanel()
    tof.show()

    app.exec()
if __name__=="__main__":
    main()