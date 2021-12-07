
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
from .ui.VMI_panel_ui_new import Ui_VMI_panel
from .ui.VMI_toolbox_panel_ui import Ui_VMI_toolbox_panel
import pyqtgraph as pg
from skimage.transform import rotate
import sys, traceback
import h5py
import numpy as np
from .ui.VMI_toolbox_panel_ui import Ui_VMI_toolbox_panel



class VMIToolBoxPanel(QWidget,Ui_VMI_toolbox_panel):
    changingRange = Signal(object)
    def __init__(self, parent=None, index=0, path=None):
        super(VMIToolBoxPanel, self).__init__(parent)
        #Load UI
        self.setupUi(self)  
        #Connect Signal
        self.Rmin_spinbox.valueChanged.connect(self.changeRange)
        self.Rmax_spinbox.valueChanged.connect(self.changeRange)
        self.RminDisk_plot = QGraphicsEllipseItem()  
        self.RminDisk_plotradius = 10
        self.center_plot.setPen(pg.mkPen('r', width=3, style=Qt.DashLine))     
        self.RmaxDisk_plot = QGraphicsEllipseItem()  
        self.RmaxDisk_plotradius = 10
        self.center_plot.setPen(pg.mkPen('r', width=3, style=Qt.DashLine))    
    def changeRange(self):
        # self.RmaxDisk_plot.setRect()
        print(self.Rmin_spinbox.value())
        print(self.Rmax_spinbox.value())



    def showRange(self):



    # def showRange()
