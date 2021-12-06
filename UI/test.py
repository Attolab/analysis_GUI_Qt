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
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.numberofPanel = 0
        self.isPanelopen = []
        # self.panelIndex = 0
        self._docks_VMI = []

    def setupWindows(self):
        self._tableSel_panel = TableSelPanel()
        self._dock_tableSel = QDockWidget('Table Selection',self)
        self._dock_tableSel.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)
        self._dock_tableSel.toggleViewAction()
        self._dock_tableSel.setWidget(self._tableSel_panel)
        self.addDockWidget(Qt.LeftDockWidgetArea,self._dock_tableSel)  
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
        # self._VMI_panel.signal_VMI_panel_destruction.connect(self._tableSel_panel.updateTable)
        # self._VMI_panel.signal_VMI_panel_destruction.connect(self.closeEventVMI)        
        # Create Dock to store panel
        # if self.isPanelopen[index] == False:
        self._docks_VMI.append(DataPanel(f'VMI_{index}', panel_type='VMI', index=index, status=True))
            # self._docks_VMI[index] = QDockWidget(f'VMI_{index}',self)
        # else:
        # self._docks_VMI.append(QDockWidget(f'VMI_{index}',self))
        self._docks_VMI[index].setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetClosable)
        self._docks_VMI[index].toggleViewAction()
        self._docks_VMI[index].setWidget(self._VMI_panel.central_widget)
        # Attach VMI panel to Dock
        self.addDockWidget(Qt.RightDockWidgetArea,self._docks_VMI[index])          


    def connectSignal(self):    
        self.VMI_action.triggered.connect(self.create_newPanel)


    def table_selChange(self, index, row):        
        if index == 0:
            print(f'Opening Panel {row}')  
            self._docks_VMI[row].show()
            self.isPanelopen[row] = True
                # self.addVMIWidget(index=row, path=self._tableSel_panel.tableWidget.item(index,3).text())
        elif index == 1:
            print(f'Closing Panel {row}')
            # self._docks_VMI[row].close()
            self._docks_VMI[row].hide()
            self.isPanelopen[row] = False
        elif index == 2:
            print(f'Deleting Panel {row}')
            self._docks_VMI[row].close()
            self._docks_VMI.pop(row)
            self._tableSel_panel.tableWidget.removeRow(row)
            self.isPanelopen.pop(row)
            self.numberofPanel -= 1
    
    def table_sel_doubleclicked(self,object):
        print(object)


    def closeEventVMI(self, index):        
        print('Panel is removed')
        self._dock_VMI.close()

class DataPanel(QDockWidget):
    def __init__(self,parent=None,  panel_type='VMI', index=0, status = True):
        super(DataPanel, self).__init__(parent)
        self.parameters = {'Type': panel_type, 'Index': index, 'Status': status}        
        # self._docks_VMI[index] = QDockWidget(f'VMI_{index}',self)

    
def main():
    import sys
    app = QApplication([])
    tof = MainPanel()
    tof.show()
    app.exec()
if __name__=="__main__":
    main()