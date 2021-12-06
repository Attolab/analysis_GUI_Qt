
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QToolButton,
    QVBoxLayout, QWidget,QTableWidgetItem,QFileDialog,QDockWidget,QMainWindow)
from .ui.VMI_panel_ui_new import Ui_VMI_panel
import pyqtgraph as pg
from skimage.transform import rotate
import sys, traceback
import h5py
import numpy as np
import pathlib
# P = QtCore.Qt.WA_DeleteOnClose
class VMIPanel(QWidget,Ui_VMI_panel):
    signal_VMI_panel_creation = Signal(object)
    signal_VMI_panel_destruction = Signal(object)

    def __init__(self, parent=None, index=0, path=None):
        super(VMIPanel, self).__init__(parent)
        #Load UI
        self.setupUi(self)  
        #Initialize parameters
        self.panel_index = index
        self.path = path
        #Open File
        self.openFile()
        #Load File
        self.VMI_load_func()
        #Connect signals
        self.connectVMISignal()


    def image_selection(self, input=0):
        # print(input)
        # self.image_sel_changed.emit(input)
        self.image_index = int(input)        
        self.imageSel_value.setValue(self.image_index)
        self.updateGUI()
 
    def connectVMISignal(self):
        self.imageCentX_value.valueChanged.connect(self.updateGUI)        
        self.imageCentY_value.valueChanged.connect(self.updateGUI)        
        self.imageRot_value.valueChanged.connect(self.updateGUI)        
        self.imageSel_value.valueChanged.connect(self.image_selection)        
        self.apply_button.clicked.connect(self.updateGUI)
        self.close_button.clicked.connect(self.closeEvent2)
        self.destroyed.connect(self.closeEvent2)

    def updateGUI(self): 
        self.readFile(self.image_index)        
        self.image.setImage(self.im)  # set image to display, used only for tests
    def meanCenter(self):                
                self.imageCentX_value.setValue((self.im.mean(axis = 0)*np.arange(self.im.shape[0])).sum()/self.im.mean(axis = 0).sum())
                self.imageCentY_value.setValue((self.im.mean(axis = 1)*np.arange(self.im.shape[1])).sum()/self.im.mean(axis = 1).sum())                
    # def read_h5file(self):
    #     with h5py.File(self.path, 'r') as file:                          
    #         self.raw_datas = file['Raw_datas']            

    # def read_npyfile(self):
    #     with open(self.path,'r') as file:
    #         np.load(file)

    def openFile(self):            
        
        if self.path is None:
            # self.path = str(QFileDialog.getOpenFileName(self, 'Import image','Q:\LIDyL\Atto\ATTOLAB\SE1\SlowRABBIT')[0])    
            self.path = str(QFileDialog.getOpenFileName(self, 'Import image','D:\\Work\\Saclay\\Git\\analysis_GUI_Qt')[0])        
        self.path_object = pathlib.Path(self.path)             
        try:
            h5file = True
            if h5file:
                self.scan = '000'  # vérifier dans hdfview
                self.path2 = ''.join(['Scan',self.scan,'/Detector000/Data2D/Ch000/Data'])
                with h5py.File(self.path, 'r') as file:                          
                    self.raw_datas = file['Raw_datas']   
                    self.image_number = self.raw_datas[self.path2].shape[0]  
                    self.imageCentX_value.setMaximum(self.raw_datas[self.path2].shape[1])
                    self.imageCentY_value.setMaximum(self.raw_datas[self.path2].shape[2])    
                # self.open_h5file()
            # self.open_npyfile()           
        except Exception:
            print(traceback.format_exception(*sys.exc_info()))   
        self.signal_VMI_panel_creation.emit(['VMI',self.path])

    def readFile(self, index=0):
        try:
            with h5py.File(self.path, 'r') as file:                          
                self.raw_datas = file['Raw_datas']     
                self.im = np.asarray(self.raw_datas[self.path2][index]).T
                if self.autoCenter_checkBox.isChecked:
                    self.meanCenter()                    
                self.im = rotate(self.im,self.imageRot_value.value(), resize=False,center= [self.imageCentX_value.value(),self.imageCentY_value.value()])                
        except Exception:
            print(traceback.format_exception(*sys.exc_info())) 


    def VMI_load_func(self):
        self.image_index = 0
        self.readFile()
        #LABELS + LINE EDITS
        self.imageNumber_value.setText(f'{self.image_number}')
        # string = f'{self.image_number}'.join('/')
        self.imageSel_value.setSuffix('/'+f'{self.image_number}')
        self.imageSel_value.setMaximum(self.image_number)
        # filename =           

        self.imageSel_value.setValue(self.image_index)
        self.dataset_value.setText(f'{self.path_object.stem }')
        self.image = pg.ImageItem()
        self.image.setImage(self.im)  # set image to display, used only for tests
        # self.image_view = pg.ImageView(parent=self.dock_direct_image,imageItem=self.image)        
        self.image_view = pg.ImageView(imageItem=self.image)        
        self.image_view.view.invertY(False)
        self.image_view.setColorMap(self.colormap())
        self.dock_direct_image.addWidget(self.image_view)
    def colormap(self):
        # doing a custom colormap (trying to make it close to the Labview one)
        pos = np.array([0.0, 0.01, 0.2, 0.4, 0.5, 0.8, 0.99, 1.0])
        color = np.array([[0, 0, 0, 255], [128, 0, 255, 255], [0, 0, 255, 255],
                        [0, 255, 255, 255], [0, 255, 0, 255],
                        [255, 255, 0, 255], [255, 0, 0, 255], [255, 255, 255, 255]],
                        dtype=np.ubyte)
        return pg.ColorMap(pos, color)  
    def closeEvent2(self, index):
        self.signal_VMI_panel_destruction.emit(self.panel_index)
        print(f'Close event: VMI panel {self.panel_index} is now closed')  
                


        # self.close()


def main():

    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle('PCO Acquisition by Dom')

    pco_ui = VMIPanel(parent=None)
    window.setCentralWidget(pco_ui.central_widget)
    window.resize(1000, 500)
    window.show()
    sys.exit(app.exec_())    

if __name__=="__main__":
    main()