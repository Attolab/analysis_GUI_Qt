from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,Signal)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform, QWindow)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QTabWidget, QWidget,QDockWidget,QFileDialog,QTableWidgetItem,QHBoxLayout)
import pyqtgraph as pg
from form_ui import Ui_MainWindow
from panels.calibration_panel import CalibrationPanel
from panels.VMI_panel import VMIPanel
from panels.tableSel_panel import TableSelPanel
from panels.DockTitleBar import DockTitleBar
import sys, traceback
import h5py
import numpy as np

class MainPanel(QMainWindow,Ui_MainWindow):
    
    def __init__(self,parent=None):
        super(MainPanel, self).__init__(parent)
        self.setCentralWidget(None)
        self.setupUi(self)        
        self.setupWindows()
        self.connectSignal()
        # self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.panelIndex = 0

    def setupWindows(self):
        self._tableSel_panel = TableSelPanel()
        self._dock_tableSel = QDockWidget('Table Selection',self)
        self._dock_tableSel.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)
        self._dock_tableSel.toggleViewAction()
        self._dock_tableSel.setWidget(self._tableSel_panel)
        self.addDockWidget(Qt.LeftDockWidgetArea,self._dock_tableSel)  

    def addVMIWidget(self,index = 0):
        #VMI panel
        self._VMI_panel = VMIPanel(index = self.panelIndex)
        #Create Doc
        self._dock_VMI = QDockWidget(f'VMI_{self.panelIndex}',self)
        self._dock_VMI.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)
        self._dock_VMI.toggleViewAction()
        self._dock_VMI.setWidget(self._VMI_panel.central_widget)
        self.addDockWidget(Qt.RightDockWidgetArea,self._dock_VMI)          
        self._tableSel_panel.new_table_entry('VMI',self._VMI_panel.path,self._VMI_panel.image_number)        
        self._VMI_panel.signal_VMI_panel_destruction.connect(self._tableSel_panel.updateTable)
        # self._VMI_panel.signal_VMI_panel_destruction.connect(self._VMI_panel.closeEvent)
        self._VMI_panel.signal_VMI_panel_destruction.connect(self.closeEventVMI)
        self.panelIndex += 1

    def connectSignal(self):    
        self.VMI_action.triggered.connect(self.addVMIWidget)
    # def closeEvent(self, event):
        #  self.emit(Signal("closed(PyQt_PyObject)"), self)


    def closeEventVMI(self, event):        
        print('Panel is removed')

    # def closeEvent(self):
    #     print('I got closed)')        
        
    
    # def openFile(self):
    #     self.path = str(QFileDialog.getOpenFileName(self, 'Import image','Q:\LIDyL\Atto\ATTOLAB\SE1\SlowRABBIT')[0])                
    #     try:
    #         with h5py.File(self.path, 'r') as file:                     
    #             scan = '000'  # vérifier dans hdfview
    #             path2 = ''.join(['Scan',self.scan,'/Detector000/Data2D/Ch000/Data'])     
    #             raw_datas = file['Raw_datas']
    #             image_number = self.raw_datas[self.path2].shape[0]          
    #     except Exception:
    #         print(traceback.format_exception(*sys.exc_info()))   
                  
# Qt.dockwi
def main():
    import sys
    app = QApplication([])
    tof = MainPanel()
    tof.show()
    app.exec()
if __name__=="__main__":
    main()