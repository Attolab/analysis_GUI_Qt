
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QPushButton, QSizePolicy, QToolButton,
    QVBoxLayout, QWidget,QTableWidgetItem,QFileDialog,QDockWidget,QMainWindow,QHeaderView)
from .ui.tableSel_panel_ui import Ui_tableSel_panel

class TableSelPanel(QWidget,Ui_tableSel_panel):
    tableSel_ComboBox_changed = Signal(int,int)
    tableSel_doubleclicked = Signal(object)

    # tableSel_ComboBox_changed = Signal(object)

    def __init__(self,parent=None):
        super(TableSelPanel, self).__init__(parent)
        self.setupUi(self)  


    def comboBox_change_fn(self,index,row):
        self.tableSel_ComboBox_changed.emit(index,row)     
    def tablesel_doubleclicked_fn(self,object):
        self.tableSel_doubleclicked.emit(object)

    # def tablewidget_change(self,row,col):
    #     self.tablewidget_change.emit(row,col)        

    def new_table_entry(self,type,path,imagenumber):
        index = self.add_row_table()
        type_item = QTableWidgetItem(f'{type}')
        path_item = QTableWidgetItem(f'{path}')
        imagenumber_item = QTableWidgetItem(f'{imagenumber}')
        # status_item = QComboBox('Open')
        # status_item.setStyleSheet('QPushButton {background-color: green; color: black;}')

        status_item = QComboBox()
        status_item.addItems(["Open", "Close", "Delete"])
        # status_item.currentIndexChanged.connect(self.comboBox_change_fn)
        # status_item = QPushButton('Open')

        type_item.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
        path_item.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
        imagenumber_item.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
        imagenumber_item.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )

        self.tableWidget.setItem(index,0, type_item)
        self.tableWidget.setCellWidget(index,1, status_item) 
        self.tableWidget.setItem(index,2, imagenumber_item) 
        self.tableWidget.setItem(index,3, path_item)      

        # self.tableWidget.cellChanged.connect(self.tablewidget_change)
        # Detect if dropbox value is changed
        self.tableWidget.cellWidget(index,1).currentIndexChanged.connect( lambda i, a=index: self.comboBox_change_fn(i, a) )
        self.tableWidget.doubleClicked.connect(self.tablesel_doubleclicked_fn )
        # self.tableWidget.mouseDoubleClickEvent.connect(self.tablesel_doubleclicked_fn)    
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
        self.tableWidget.cellWidget(index,1).setCurrentIndex(1)
        # self.tableWidget.cellWidget(index,1).setText('Closed')
        print('table is updated')
        # self.tableWidget.CellWidget(index,1, status_item) 


def main():
    import sys
    app = QApplication([])
    test = TableSelPanel()
    test.show()
    app.exec()
if __name__=="__main__":
    main()