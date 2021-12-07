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

class Ui_VMI_panel(object):

    def setupUi(self, VMI_panel):
        if not VMI_panel.objectName():
            VMI_panel.setObjectName(u"VMI_panel")

        self.central_widget = dockarea.DockArea()
        self.control_dock = dockarea.Dock("", size=(150, 600))
        # self.control_dock.hideTitleBar()

        self.controls_layout = pg.LayoutWidget()
        self.controls_layout_function()


        self.direct_image_dock = dockarea.Dock("Direct Image", size=(600, 600))
        self.central_widget.addDock(self.control_dock, 'left')
        self.central_widget.addDock(self.direct_image_dock, 'right', self.control_dock)


    def controls_layout_function(self):
        #Create buttons
        self.dataset_label = QLabel('Dataset')
        self.dataset_value = QLabel('')
        self.imageNumber_label = QLabel('Number of images')        
        self.imageNumber_value = QLabel('')
        self.imageSel_value = QSpinBox()
        self.imageSel_label = QLabel('Image selected')
        self.imageCentX_label = QLabel('CenterX')
        self.imageCentY_label = QLabel('CenterY')
        self.imageCentX_value = QDoubleSpinBox()
        self.imageCentY_value = QDoubleSpinBox()
        self.showAxis_checkBox = QCheckBox('ShowAxis') 
        self.showAxis_checkBox.setChecked(True)
        self.showCenter_checkBox = QCheckBox('ShowCenter')  
        self.showCenter_checkBox.setChecked(True)
        self.imageRot_label = QLabel('Image rotation')
        self.imageRot_value = QDoubleSpinBox()      
        self.apply_button = QPushButton('Apply')
        self.close_button = QPushButton('Close')
        self.toolbox_button = QPushButton('Toolbox')

        #Remove keyboard tracking from spin box
        self.imageRot_value.setKeyboardTracking(False)
        self.imageCentX_value.setKeyboardTracking(False)
        self.imageCentY_value.setKeyboardTracking(False)
        self.imageSel_value.setKeyboardTracking(False)
        # Limit conditions for spin box
        self.imageRot_value.setMinimum(-360.000000000000000)
        self.imageRot_value.setMaximum(360.000000000000000)  




        n = 0
        self.controls_layout.addWidget(self.dataset_label, n, 0)
        self.controls_layout.addWidget(self.dataset_value, n, 1)
        n = n + 1        
        self.controls_layout.addWidget(self.imageSel_label, n, 0)
        self.controls_layout.addWidget(self.imageSel_value, n, 1)
        n = n + 1        
        self.controls_layout.addWidget(self.imageCentX_label, n, 0)
        self.controls_layout.addWidget(self.imageCentX_value, n, 1)
        n = n + 1                
        self.controls_layout.addWidget(self.imageCentY_label, n, 0)
        self.controls_layout.addWidget(self.imageCentY_value, n, 1)         
        n = n + 1        
        self.controls_layout.addWidget(self.showAxis_checkBox, n, 0)    
        self.controls_layout.addWidget(self.showCenter_checkBox, n, 1)              
        n = n + 1        
        self.controls_layout.addWidget(self.imageRot_label, n, 0)
        self.controls_layout.addWidget(self.imageRot_value, n, 1)
        n = n + 1         
        self.controls_layout.addWidget(self.toolbox_button, n, 0, 1, 2)                
        n = n + 1        
        self.coords_lb = QLabel("")  # gives x, y and value where the mouse is
        self.controls_layout.addWidget(self.coords_lb, n, 0, 1, 2)                
        n = n + 1        
        # self.stat_lb = QLabel("")  # gives max and integrate of the image        
        # self.controls_layout.addWidget(self.stat_lb, n, 1)                
        # n = n + 1        
        verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding) 
        self.controls_layout.layout.addItem(verticalSpacer,n,0,1,2)
        n = n + 1
        horizontalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding) 
        self.controls_layout.layout.addItem(horizontalSpacer,0,2,n,1)
        # self.layout = QGridLayout()
        self.control_dock.addWidget(self.controls_layout)
        # self.control_dock.addWidget(verticalSpacer)


        # self.central_widget.addDock(self.control_dock, 'left')
        # self.central_widget.addDock(self.direct_image_dock, 'right', self.control_dock)            
        # VMI_panel.setEnabled(True)
        # VMI_panel.resize(813, 522)
        # sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(VMI_panel.sizePolicy().hasHeightForWidth())
        # VMI_panel.setSizePolicy(sizePolicy)
        # VMI_panel.setMinimumSize(QSize(0, 0))
        # self.VMI_axis_layout = GraphicsLayoutWidget(VMI_panel)
        # self.VMI_axis_layout.setObjectName(u"VMI_axis_layout")
        # self.VMI_axis_layout.setGeometry(QRect(230, 0, 561, 511))
        # sizePolicy.setHeightForWidth(self.VMI_axis_layout.sizePolicy().hasHeightForWidth())
        # self.VMI_axis_layout.setSizePolicy(sizePolicy)
        # self.verticalLayoutWidget = QWidget(VMI_panel)
        # self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        # self.verticalLayoutWidget.setGeometry(QRect(0, 0, 211, 521))
        # self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        # self.verticalLayout.setObjectName(u"verticalLayout")
        # self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        # self.horizontalLayout = QHBoxLayout()
        # self.horizontalLayout.setObjectName(u"horizontalLayout")
        # self.dataset_label = QLabel(self.verticalLayoutWidget)
        # self.dataset_label.setObjectName(u"dataset_label")

        # self.horizontalLayout.addWidget(self.dataset_label)

        # self.datasetSel_label = QLabel(self.verticalLayoutWidget)
        # self.datasetSel_label.setObjectName(u"datasetSel_label")

        # self.horizontalLayout.addWidget(self.datasetSel_label)


        # self.verticalLayout.addLayout(self.horizontalLayout)

        # self.horizontalLayout_2 = QHBoxLayout()
        # self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        # self.imageNumber_label = QLabel(self.verticalLayoutWidget)
        # self.imageNumber_label.setObjectName(u"imageNumber_label")

        # self.horizontalLayout_2.addWidget(self.imageNumber_label)

        # self.imageNumber_value = QLabel(self.verticalLayoutWidget)
        # self.imageNumber_value.setObjectName(u"imageNumber_value")

        # self.horizontalLayout_2.addWidget(self.imageNumber_value)


        # self.verticalLayout.addLayout(self.horizontalLayout_2)

        # self.horizontalLayout_4 = QHBoxLayout()
        # self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        # self.ImageSel_label = QLabel(self.verticalLayoutWidget)
        # self.ImageSel_label.setObjectName(u"ImageSel_label")
        # sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        # sizePolicy1.setHorizontalStretch(0)
        # sizePolicy1.setVerticalStretch(0)
        # sizePolicy1.setHeightForWidth(self.ImageSel_label.sizePolicy().hasHeightForWidth())
        # self.ImageSel_label.setSizePolicy(sizePolicy1)

        # self.horizontalLayout_4.addWidget(self.ImageSel_label)

        # self.imageSel_value = QSpinBox(self.verticalLayoutWidget)
        # self.imageSel_value.setObjectName(u"imageSel_value")
        # sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        # sizePolicy2.setHorizontalStretch(0)
        # sizePolicy2.setVerticalStretch(0)
        # sizePolicy2.setHeightForWidth(self.imageSel_value.sizePolicy().hasHeightForWidth())
        # self.imageSel_value.setSizePolicy(sizePolicy2)

        # self.horizontalLayout_4.addWidget(self.imageSel_value)


        # self.verticalLayout.addLayout(self.horizontalLayout_4)

        # self.ImageList_table = QTableWidget(self.verticalLayoutWidget)
        # if (self.ImageList_table.columnCount() < 2):
        #     self.ImageList_table.setColumnCount(2)
        # __qtablewidgetitem = QTableWidgetItem()
        # self.ImageList_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        # __qtablewidgetitem1 = QTableWidgetItem()
        # self.ImageList_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        # self.ImageList_table.setObjectName(u"ImageList_table")
        # self.ImageList_table.setEnabled(True)
        # sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        # sizePolicy3.setHorizontalStretch(0)
        # sizePolicy3.setVerticalStretch(0)
        # sizePolicy3.setHeightForWidth(self.ImageList_table.sizePolicy().hasHeightForWidth())
        # self.ImageList_table.setSizePolicy(sizePolicy3)
        # self.ImageList_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.ImageList_table.horizontalHeader().setVisible(True)
        # self.ImageList_table.verticalHeader().setVisible(False)

        # self.verticalLayout.addWidget(self.ImageList_table)

        # self.horizontalLayout_3 = QHBoxLayout()
        # self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        # self.ImageRot_label = QLabel(self.verticalLayoutWidget)
        # self.ImageRot_label.setObjectName(u"ImageRot_label")
        # sizePolicy1.setHeightForWidth(self.ImageRot_label.sizePolicy().hasHeightForWidth())
        # self.ImageRot_label.setSizePolicy(sizePolicy1)

        # self.horizontalLayout_3.addWidget(self.ImageRot_label)

        # self.imageRot_value = QSpinBox(self.verticalLayoutWidget)
        # self.imageRot_value.setObjectName(u"imageRot_value")

        # self.horizontalLayout_3.addWidget(self.imageRot_value)


        # self.verticalLayout.addLayout(self.horizontalLayout_3)


        # self.retranslateUi(VMI_panel)

        # QMetaObject.connectSlotsByName(VMI_panel)
    # setupUi

    def retranslateUi(self, VMI_panel):
        VMI_panel.setWindowTitle(QCoreApplication.translate("VMI_panel", u"Form", None))
        self.dataset_label.setText(QCoreApplication.translate("VMI_panel", u"Dataset", None))
        self.datasetSel_label.setText(QCoreApplication.translate("VMI_panel", u"TextLabel", None))
        self.imageNumber_label.setText(QCoreApplication.translate("VMI_panel", u"Number of images", None))
        self.imageNumber_value.setText(QCoreApplication.translate("VMI_panel", u"TextLabel", None))
        self.ImageSel_label.setText(QCoreApplication.translate("VMI_panel", u"Image selected", None))
        self.imageSel_value.setPrefix("")
        ___qtablewidgetitem = self.ImageList_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("VMI_panel", u"Image index", None));
        ___qtablewidgetitem1 = self.ImageList_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("VMI_panel", u"Parameter", None));
        self.ImageRot_label.setText(QCoreApplication.translate("VMI_panel", u"Image rotation", None))
        self.imageRot_value.setPrefix("")
    # retranslateUi

