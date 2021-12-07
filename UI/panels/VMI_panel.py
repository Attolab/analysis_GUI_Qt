
from PyQt5.QtCore import center
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, QRectF,
    QSize, QTime, QUrl, Qt,Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform,QPen)
from PySide6.QtWidgets import (QApplication, QGraphicsEllipseItem,QGraphicsLineItem, QPushButton, QSizePolicy, QToolButton,
    QVBoxLayout, QWidget,QTableWidgetItem,QFileDialog,QDockWidget,QMainWindow)
from .ui.VMI_panel_ui_new import Ui_VMI_panel
import pyqtgraph as pg
from skimage.transform import rotate
from panels.VMI_toolbox_panel import VMIToolBoxPanel
import pyqtgraph  as pg  
from pyqtgraph import dockarea
import sys, traceback
import h5py
import numpy as np
import pathlib
from functions.useful_functions import MyStringAxis
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
        self.center_x = 0
        self.center_y = 0
        self.rot_angle = 0
        #Initialize some widgets
        self.image = pg.ImageItem()
        self.center_plot = QGraphicsEllipseItem()  
        self.center_plotradius = 10
        self.center_plot.setPen(pg.mkPen('r', width=3, style=Qt.DashLine))     


        # self.straightlines_plot = QPainter()
        # self.straightlines_plot.drawLine(-1024,0,1024,0)
        # self.straightlines_plot.drawLine(0,-1024,0,1024)
        # self.straightlines_plot.setPen(pg.mkPen('w', width=3, style=Qt.DotLine))                      
        self.x_line_plot = QGraphicsLineItem()
        self.x_line_plot.setPen(pg.mkPen('w', width=3, style=Qt.DotLine)) 
        self.y_line_plot = QGraphicsLineItem()
        self.y_line_plot.setPen(pg.mkPen('w', width=3, style=Qt.DotLine))    

        # self.x_line_plot.set  
        # self.pa
        # self.straightlines_plot = 100
        # self.straightlines_plot.setPen(pg.mkPen('w', width=3, style=Qt.DotLine))                      

        #Open File
        self.openFile()
        #Load File
        self.VMI_load_func()
        #Connect signals
        self.connectVMISignal()


    def image_selection(self, input=0):
        self.image_index = int(input)        
        # self.imageSel_value.setValue(self.image_index)
        self.updateImage()
    def update_centers(self):
        self.center_x = self.imageCentX_value.value()
        self.center_y = self.imageCentY_value.value()
        self.center_plot.setRect(self.center_x-self.center_plotradius, self.center_y-self.center_plotradius, 2*self.center_plotradius, 2*self.center_plotradius)        
        self.update_axis()

    def update_axis(self):
        line_x = np.array([-1024,0,1024,0])
        line_y = np.array([0,-1024,0,1024])
        line_x[0::2] = line_x[0::2] + self.center_x
        line_y[0::2] = line_y[0::2] + self.center_x
        line_x[1::2] = line_x[1::2] + self.center_y
        line_y[1::2] = line_y[1::2] + self.center_y
        self.x_line_plot.setLine(line_x[0],line_x[1],line_x[2],line_x[3])
        self.y_line_plot.setLine(line_y[0],line_y[1],line_y[2],line_y[3])

        self.showCenter(self.showCenter_checkBox.isChecked())
    def update_angle(self):
        self.rot_angle = self.imageRot_value.value()
        self.updateImage()

    def connectVMISignal(self):
        self.imageCentX_value.valueChanged.connect(self.update_centers)        
        self.imageCentY_value.valueChanged.connect(self.update_centers)        
        self.imageRot_value.valueChanged.connect(self.update_angle)        
        self.imageSel_value.valueChanged.connect(self.image_selection)     
        self.image_view.scene.sigMouseMoved.connect(self.mouse_moved)
        self.showCenter_checkBox.stateChanged.connect(self.showCenter)
        self.showCenter_checkBox.stateChanged.connect(self.showCenter)
        self.showAxis_checkBox.stateChanged.connect(self.showAxisLine)
        self.toolbox_button.clicked.connect(self.createToolBox)

        # self.close_button.clicked.connect(self.close_panel_VMI)
    def createToolBox(self):
        #Create Widget
        self.toolbox = VMIToolBoxPanel()
        #Create Layout for Widget
        self.toolbox_layout = pg.LayoutWidget()        
        self.toolbox_layout.addWidget(self.toolbox)
        #Create Dock for Layout
        self.toolbox_dock = dockarea.Dock('Toolbox',size = (271,300))
        self.toolbox_dock.addWidget(self.toolbox_layout)

        # self.toolbox_dock.
        #Implement in central_widget
        self.central_widget.addDock(self.toolbox_dock, 'bottom',relativeTo= self.control_dock)
        self.central_widget.floatDock(self.toolbox_dock)


    def updateImage(self): 
        self.readFile(self.image_index)        
        self.image.setImage(self.im)  # set image to display, used only for tests
        # self.image_view.view.axes['left']['item'].setTicks(self.y_array[0], self.y_array[-1], self.im.shape[1])
        # x = ["%.2f" % i for i in self.x_array]
        # y = ["%.2f" % i for i in self.y_array]        
        # xdict = dict(enumerate(x))
        # stringaxis_x = MyStringAxis(dict(enumerate(x)), orientation='bottom')
        # stringaxis_y = MyStringAxis(dict(enumerate(y)), orientation='bottom')
        # self.image_view.view.axes['bottom']['item'].setTicks(stringaxis_x)
        # self.image_view.view.axes['left']['item'].setTicks(stringaxis_y)
        # plot = win.addPlot(axisItems={'bottom': stringaxis})
        # curve = plot.plot(list(xdict.keys()),y)
        # self.image_view.view.setXRange(self.x_array[0], self.x_array[-1])
        # self.image_view.view.setYRange(self.x_array[0], self.x_array[-1])
        # setAxisItems(axisItems=None)

    def meanCenter(self):              
        self.imageCentX_value.setValue((self.im.mean(axis = 1)*np.arange(self.im.shape[1])).sum()/self.im.mean(axis = 1).sum())
        self.imageCentY_value.setValue((self.im.mean(axis = 0)*np.arange(self.im.shape[0])).sum()/self.im.mean(axis = 0).sum())                
        self.update_centers()

    # def read_h5file(self):
    #     with h5py.File(self.path, 'r') as file:                          
    #         self.raw_datas = file['Raw_datas']            

    # def read_npyfile(self):
    #     with open(self.path,'r') as file:
    #         np.load(file)

    def openFile(self):            
        
        if self.path is None:
            self.path = str(QFileDialog.getOpenFileName(self, 'Import image','Q:\LIDyL\Atto\ATTOLAB\SE1\SlowRABBIT')[0])    
            # self.path = str(QFileDialog.getOpenFileName(self, 'Import image','D:\\Work\\Saclay\\Git\\analysis_GUI_Qt')[0])        
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
                    self.im = np.asarray(self.raw_datas[self.path2][0]).T
                    self.meanCenter()                    
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
                self.im = rotate(self.im,self.imageRot_value.value(), resize=False,center= [self.imageCentY_value.value(),self.imageCentX_value.value()])                
        except Exception:
            print(traceback.format_exception(*sys.exc_info())) 

    def VMI_load_func(self):
        self.image_index = 0
        self.readFile()
        #LABELS + LINE EDITS
        self.imageSel_value.setSuffix('/'+f'{self.image_number}')
        self.imageSel_value.setMaximum(self.image_number)
        self.imageSel_value.setValue(self.image_index)
        self.dataset_value.setText(f'{self.path_object.stem }')    
        self.image.setImage(self.im)  # set image to display, used only for tests
        self.image_view = pg.ImageView(imageItem=self.image, view=pg.PlotItem())        
        self.image_view.view.invertY(False)
        self.image_view.setColorMap(self.colormap())    
        self.image_view.view.addItem(self.center_plot)   
        self.image_view.view.addItem(self.x_line_plot)   
        self.image_view.view.addItem(self.y_line_plot)   
        self.direct_image_dock.addWidget(self.image_view)

        self.updateImage()

    def colormap(self):
        # doing a custom colormap (trying to make it close to the Labview one)
        pos = np.array([0.0, 0.01, 0.2, 0.4, 0.5, 0.8, 0.99, 1.0])
        color = np.array([[0, 0, 0, 255], [128, 0, 255, 255], [0, 0, 255, 255],
                        [0, 255, 255, 255], [0, 255, 0, 255],
                        [255, 255, 0, 255], [255, 0, 0, 255], [255, 255, 255, 255]],
                        dtype=np.ubyte)
        return pg.ColorMap(pos, color)  
    def close_panel_VMI(self, index):
        self.signal_VMI_panel_destruction.emit(self.panel_index)
        print(f'Close event: VMI panel {self.panel_index} is now closed')  
        
        
        


    def mouse_moved(self, view_pos):
        try:
            data = self.im
            n_rows, n_cols = data.shape
            scene_pos = self.image_view.getImageItem().mapFromScene(view_pos)

            row, col = int(scene_pos.x()), int(scene_pos.y())  # I inverted x and y

            if (0 <= row < n_rows) and (0 <= col < n_cols):
                value = data[row, col]
                self.coords_lb.setText('x = {:d}, y = {:d}\n value = {:}'.format(row, col, value))
                self.coords_lb.repaint()
            else:
                self.coords_lb.setText('')
            #time.sleep(0.1)        
        except AttributeError:  # when no image is displayed yet
            print(traceback.format_exception(*sys.exc_info()))    

    def showCenter(self,status):
        self.center_plot.setVisible(status)   
    def showAxisLine(self,status):
        self.x_line_plot.setVisible(status)
        self.y_line_plot.setVisible(status)
        


                
        # self.image_view.scene.addItem()


        # view.addItem(QGraphicsEllipseItem(QRectF(center[0], center[1], 10, 10)))

        # painter = QPainter(self.direct_image_dock)
        # painter.setPen(pg.mkPen('y', width=3, style=Qt.DashLine) )
        # painter.drawArc(QRect(center[0], center[1], 10, 10), 0, 5760)
        # painter.drawText(150, 250, 'Hellow world!')


    # def doAbel(self,parameters):
    #     if remove_bkg:
    #         data = data - data[0:200, 0:200].mean()
    #         if i == 0:
    #         abel_obj = Abel_object(self.im, self.center, center_y, d_alpha_deg, dr, N, Rmax)
    #             abel_obj.precalculate()
    #         else:
    #             abel_obj.set_data(data)
    #         abel_obj.invert()

    #         if save_betas:
    #             for index,f in enumerate(filename_beta[:,1]):
    #                 np.save(f, abel_obj.F[index])    
    #     self.close()





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