
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QToolButton,
    QVBoxLayout, QWidget,QTableWidgetItem,QFileDialog,QDockWidget,QMainWindow,QHeaderView)
from .ui.tableSel_panel_ui import Ui_tableSel_panel
import pyqtgraph as pg
from skimage.transform import rotate
import sys, traceback
import h5py
import numpy as np


class TableSelPanel(QWidget,Ui_tableSel_panel):
    def __init__(self,parent=None):
        super(TableSelPanel, self).__init__(parent)
        self.setupUi(self)  

    def new_table_entry(self,type,path,imagenumber):
        index = self.add_row_table()
        type_item = QTableWidgetItem(f'{type}')
        path_item = QTableWidgetItem(f'{path}')
        imagenumber_item = QTableWidgetItem(f'{imagenumber}')
        status_item = QPushButton('Open')
        status_item.setStyleSheet('QPushButton {background-color: green; color: black;}')

        type_item.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
        path_item.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
        imagenumber_item.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
        imagenumber_item.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )

        self.tableWidget.setItem(index,0, type_item)
        self.tableWidget.setCellWidget(index,1, status_item) 
        self.tableWidget.setItem(index,2, imagenumber_item) 
        self.tableWidget.setItem(index,3, path_item)         
        self.check_columnwidth()
    def check_columnwidth(self):
        header = self.tableWidget.horizontalHeader()    
        # for i in ran   
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)  
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)  

    def add_row_table(self):  
        rowNumber = self.tableWidget.rowCount()      
        self.tableWidget.insertRow(rowNumber)
        return rowNumber
    def updateTable(self,index):
        self.tableWidget.cellWidget(index,1).setStyleSheet('QPushButton {background-color: red; color: black;}')
        self.tableWidget.cellWidget(index,1).setText('Closed')
        print('table is updated')
        # self.tableWidget.CellWidget(index,1, status_item) 


        # # self.image.setImage(self.im, autoLevels=True)
        # for i in range(imagenumber):
        #     index = QTableWidgetItem(f'{i}')
        #     parameter = QTableWidgetItem(f'{i}')
        #     index.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
        #     parameter.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )

# Qt.dockwi
def main():
    import sys
    app = QApplication([])
    test = TableSelPanel()
    test.show()
    app.exec()
if __name__=="__main__":
    main()