
from PyQt5.QtCore import center
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, QRectF,
    QSize, QTime, QUrl, Qt,Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform,QPen)
from PySide6.QtWidgets import (QApplication, QGraphicsEllipseItem, QPushButton, QSizePolicy, QToolButton,
    QVBoxLayout, QWidget,QTableWidgetItem,QFileDialog,QDockWidget,QMainWindow,QGraphicsItem)
from .ui.VMI_toolbox_panel_ui import Ui_VMI_toolbox_panel
import pyqtgraph as pg
from skimage.transform import rotate
import numpy as np
from .ui.VMI_toolbox_panel_ui import Ui_VMI_toolbox_panel



class VMIToolBoxPanel(QWidget,Ui_VMI_toolbox_panel):
    changingRange_signal = Signal(float,float)
    changingCenter_signal = Signal(float,float)
    changingRadialBin_signal = Signal(object)
    changingAngularBin_signal = Signal(object)
    changingAngle_signal = Signal(float)
    showingRange_signal = Signal(bool)
    showingCenter_signal = Signal(bool)
    showingAxis_signal = Signal(bool)
    def __init__(self, parent=None, index=0, path=None):
        super(VMIToolBoxPanel, self).__init__(parent)
        #Load UI
        self.setupUi(self)  
        #Connect Signal
        self.connectSignal()

    def connectSignal(self):
        self.Rmin_spinbox.valueChanged.connect(self.changeRange)
        self.Rmax_spinbox.valueChanged.connect(self.changeRange)
        self.imageCentX_value.valueChanged.connect(self.changeCenter)
        self.imageCentY_value.valueChanged.connect(self.changeCenter)
        self.imageRot_value.valueChanged.connect(self.changeAngle)
        self.showRange_checkBox.stateChanged.connect(self.showRange)
        self.showAxis_checkBox.stateChanged.connect(self.showAxis)
        self.showCenter_checkBox.stateChanged.connect(self.showCenter)
        self.dR_value.valueChanged.connect(self.changeRadialBin)
        self.dTheta_value.valueChanged.connect(self.changeAngularBin)
        # self.abel_inversion_pushbutton.buttonclicked.connect(self.)

    # def abel_inversion_pushbutton
    def changeRange(self):        
        self.changingRange_signal.emit(self.Rmin_spinbox.value(),self.Rmax_spinbox.value())
    def changeCenter(self):        
        self.changingCenter_signal.emit(self.imageCentX_value.value(),self.imageCentY_value.value())        
    def changeAngle(self):        
        self.changingAngle_signal.emit(self.imageRot_value.value())        
    def changeRadialBin(self):
        self.changingRadialBin_signal.emit(self.dR_value.value())
    def changeAngularBin(self):
        self.changingAngularBin_signal.emit(self.dTheta_value.value()*np.pi/180)        

    def showRange(self):
        self.showingRange_signal.emit(self.showRange_checkBox.isChecked())
    def showAxis(self):
        self.showingAxis_signal.emit(self.showAxis_checkBox.isChecked())
    def showCenter(self):
        self.showingCenter_signal.emit(self.showCenter_checkBox.isChecked())

    def updateCenter(self,Cx,Cy):
        self.imageCentX_value.setValue(Cx)
        self.imageCentY_value.setValue(Cy)        

        

