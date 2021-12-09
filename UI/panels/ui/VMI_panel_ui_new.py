# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VMI_panel.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QDoubleSpinBox, QHBoxLayout, QHeaderView,
    QLabel, QSizePolicy, QSpinBox, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget,QPushButton,QSpacerItem,QSizePolicy,QGridLayout)
import pyqtgraph  as pg  
from pyqtgraph import dockarea
# from .panels.ui.VMI_toolbox_panel_ui import Ui_VMI_toolbox_panel
# from panels.ui.VMI_toolbox_panel_ui import Ui_VMI_toolbox_panel
from panels.VMI_toolbox_panel import VMIToolBoxPanel

class Ui_VMI_panel(object):

    def setupUi(self, VMI_panel):
        if not VMI_panel.objectName():
            VMI_panel.setObjectName(u"VMI_panel")

        self.central_widget = dockarea.DockArea()
        self.control_dock = dockarea.Dock("Image Selection", size=(150, 600))
        self.toolbox_dock = dockarea.Dock("Toolbox", size=(271, 300))
        
        # #Create Widget        
        self.controls_layout = pg.LayoutWidget()
        self.controls_layout_function()
        self.control_dock.addWidget(self.controls_layout)

        self.toolbox = VMIToolBoxPanel()
        self.toolbox_layout = pg.LayoutWidget()     
        self.toolbox_layout.addWidget(VMIToolBoxPanel())
        self.toolbox_dock.addWidget(self.toolbox)

        self.central_widget.addDock(self.control_dock, 'left')
        self.central_widget.addDock(self.toolbox_dock, 'bottom', self.control_dock)
        


    def controls_layout_function(self):
        #Create buttons
        self.dataset_label = QLabel('Dataset')
        self.dataset_value = QLabel('')
        self.imageNumber_label = QLabel('Number of images')        
        self.imageNumber_value = QLabel('')
        self.imageSel_value = QSpinBox()
        self.imageSel_label = QLabel('Image selected')
        self.imageSel_value.setKeyboardTracking(False)
        n = 0
        self.controls_layout.addWidget(self.dataset_label, n, 0)
        self.controls_layout.addWidget(self.dataset_value, n, 1)
        n = n + 1        
        self.controls_layout.addWidget(self.imageSel_label, n, 0)
        self.controls_layout.addWidget(self.imageSel_value, n, 1)
        n = n + 1        
        self.coords_lb = QLabel("")  # gives x, y and value where the mouse is
        self.controls_layout.addWidget(self.coords_lb, n, 0, 1, 2)                
        n = n + 1        
        self.stat_lb = QLabel("")  # gives max and integrate of the image        
        self.controls_layout.addWidget(self.stat_lb, n, 1)                
        n = n + 1        
        verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding) 
        self.controls_layout.layout.addItem(verticalSpacer,n,0,1,2)
        n = n + 1
        horizontalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding) 
        self.controls_layout.layout.addItem(horizontalSpacer,0,2,n,1)

