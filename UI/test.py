from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,Signal)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform, QWindow,QCloseEvent)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QTabWidget, QWidget,QDockWidget,QFileDialog,QTableWidgetItem,QHBoxLayout)
import pyqtgraph as pg
from form_ui import Ui_MainWindow
from panels.calibration_panel import CalibrationPanel
from panels.VMI_panel import VMIPanel
from panels.tableSel_panel import TableSelPanel
# from panels.DockTitleBar import DockTitleBar
from panels.VMI_toolbox_panel import VMIToolBoxPanel
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
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.numberofPanel = 0
        self.isPanelopen = []
        self._docks_VMI = []

    def setupWindows(self):
        self._tableSel_panel = TableSelPanel()

        self.setCentralWidget(self._tableSel_panel)
        self._tableSel_panel.tableSel_ComboBox_changed.connect(self.table_selChange)
        self._tableSel_panel.tableSel_doubleclicked.connect(self.table_sel_doubleclicked)



    def create_newPanel(self, index=0, path=None):
        self.addVMIWidget(index=self.numberofPanel, path=path)
        if index <= self.numberofPanel:
            self._tableSel_panel.new_table_entry('VMI',self._VMI_panel.path,self._VMI_panel.image_number)        
            self.isPanelopen.append(True)
            self.numberofPanel += 1        


    # def addDockWidget(self, index=0, path=None)
    def addVMIWidget(self, index=0, path=None):
        # VMI panel
        self._VMI_panel = VMIPanel(index=self.numberofPanel, path=path)
        # Create signals
        # self._VMI_panel.signal_VMI_panel_destruction.connect(self._tableSel_panel.comboBox_change_fn)
        # self._VMI_panel.signal_VMI_panel_destruction.connect(self.closeEventVMI)        
        # Create Dock to store panel
        self._docks_VMI.append(DataPanel(f'VMI_{index}', panel_type='VMI', index=index, status=True))
        self._docks_VMI[index].setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetClosable)
        self._docks_VMI[index].toggleViewAction()
        self._docks_VMI[index].setWidget(self._VMI_panel.central_widget)
        # self._docks_VMI[index].dock_closing_signal.connect(self.table_selChange)
        self._docks_VMI[index].dock_closing_signal.connect(self._tableSel_panel.comboBox_change_fn)

        # Attach VMI panel to Dock
        self.addDockWidget(Qt.BottomDockWidgetArea,self._docks_VMI[index])          

    def connectSignal(self):    
        self.VMI_action.triggered.connect(self.create_newPanel)


    def table_selChange(self, index, row):        
        if index == 0:
            print(f'Opening Panel {row}')  
            self._docks_VMI[row].show()
            self.isPanelopen[row] = True
            # self._tableSel_panel.tableWidget.cellWidget(row,1).setStyleSheet("QComboBox"
            #                             "{background-color: lightgreen;}")
        elif index == 1:
            print(f'Closing Panel {row}')
            # self._docks_VMI[row].close()
            self._docks_VMI[row].hide()
            self.isPanelopen[row] = False
            # self._tableSel_panel.tableWidget.cellWidget(row,1).setStyleSheet("QComboBox"
            #                             "{background-color: #FF7276;}")
        elif index == 2:
            print(f'Deleting Panel {row}')
            self._docks_VMI[row].close()
            self._docks_VMI.pop(row)
            self._tableSel_panel.tableWidget.removeRow(row)
            self.isPanelopen.pop(row)
            self.numberofPanel -= 1
    
    def table_sel_doubleclicked(self,object):
        print(object)

class DataPanel(QDockWidget):
    dock_closing_signal = Signal(int,int)
    def __init__(self,parent=None,  panel_type='VMI', index=0, status = True):
        super(DataPanel, self).__init__(parent)
        self.parameters = {'Type': panel_type, 'Index': index, 'Status': status}        
        # self._docks_VMI[index] = QDockWidget(f'VMI_{index}',self)
    def closeEvent(self, event: QCloseEvent):
        self.parameters['Status'] = False
        self.dock_closing_signal.emit(1,self.parameters['Index'])

    
def main():
    import sys
    app = QApplication([])
    tof = MainPanel()
    tof.show()
    app.exec()
if __name__=="__main__":
    main()