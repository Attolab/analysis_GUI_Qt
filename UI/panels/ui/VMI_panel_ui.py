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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QDoubleSpinBox,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QPushButton, QSizePolicy, QSpinBox,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

from pyqtgraph import GraphicsLayoutWidget

class Ui_VMI_panel(object):
    def setupUi(self, VMI_panel):
        if not VMI_panel.objectName():
            VMI_panel.setObjectName(u"VMI_panel")
        VMI_panel.setEnabled(True)
        VMI_panel.resize(830, 609)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VMI_panel.sizePolicy().hasHeightForWidth())
        VMI_panel.setSizePolicy(sizePolicy)
        VMI_panel.setMinimumSize(QSize(0, 0))
        self.horizontalLayoutWidget_5 = QWidget(VMI_panel)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(0, 10, 791, 601))
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.dataset_label = QLabel(self.horizontalLayoutWidget_5)
        self.dataset_label.setObjectName(u"dataset_label")

        self.horizontalLayout.addWidget(self.dataset_label)

        self.datasetSel_label = QLabel(self.horizontalLayoutWidget_5)
        self.datasetSel_label.setObjectName(u"datasetSel_label")

        self.horizontalLayout.addWidget(self.datasetSel_label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.imageNumber_label = QLabel(self.horizontalLayoutWidget_5)
        self.imageNumber_label.setObjectName(u"imageNumber_label")

        self.horizontalLayout_2.addWidget(self.imageNumber_label)

        self.imageNumber_value = QLabel(self.horizontalLayoutWidget_5)
        self.imageNumber_value.setObjectName(u"imageNumber_value")

        self.horizontalLayout_2.addWidget(self.imageNumber_value)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.ImageSel_label = QLabel(self.horizontalLayoutWidget_5)
        self.ImageSel_label.setObjectName(u"ImageSel_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ImageSel_label.sizePolicy().hasHeightForWidth())
        self.ImageSel_label.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.ImageSel_label)

        self.imageSel_value = QSpinBox(self.horizontalLayoutWidget_5)
        self.imageSel_value.setObjectName(u"imageSel_value")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.imageSel_value.sizePolicy().hasHeightForWidth())
        self.imageSel_value.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.imageSel_value)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.ImageList_table = QTableWidget(self.horizontalLayoutWidget_5)
        if (self.ImageList_table.columnCount() < 2):
            self.ImageList_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.ImageList_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.ImageList_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.ImageList_table.setObjectName(u"ImageList_table")
        self.ImageList_table.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ImageList_table.sizePolicy().hasHeightForWidth())
        self.ImageList_table.setSizePolicy(sizePolicy3)
        self.ImageList_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ImageList_table.horizontalHeader().setVisible(True)
        self.ImageList_table.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.ImageList_table)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.ImageCentY_label = QLabel(self.horizontalLayoutWidget_5)
        self.ImageCentY_label.setObjectName(u"ImageCentY_label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.ImageCentY_label.sizePolicy().hasHeightForWidth())
        self.ImageCentY_label.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.ImageCentY_label, 0, 1, 1, 1)

        self.imageCentX_value = QDoubleSpinBox(self.horizontalLayoutWidget_5)
        self.imageCentX_value.setObjectName(u"imageCentX_value")
        self.imageCentX_value.setMaximum(2048.000000000000000)

        self.gridLayout.addWidget(self.imageCentX_value, 1, 0, 1, 1)

        self.imageCentY_value = QDoubleSpinBox(self.horizontalLayoutWidget_5)
        self.imageCentY_value.setObjectName(u"imageCentY_value")
        self.imageCentY_value.setMaximum(2048.000000000000000)

        self.gridLayout.addWidget(self.imageCentY_value, 1, 1, 1, 1)

        self.ImageCentX_label = QLabel(self.horizontalLayoutWidget_5)
        self.ImageCentX_label.setObjectName(u"ImageCentX_label")
        sizePolicy4.setHeightForWidth(self.ImageCentX_label.sizePolicy().hasHeightForWidth())
        self.ImageCentX_label.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.ImageCentX_label, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.autoCenter_checkBox = QCheckBox(self.horizontalLayoutWidget_5)
        self.autoCenter_checkBox.setObjectName(u"autoCenter_checkBox")
        self.autoCenter_checkBox.setChecked(False)

        self.verticalLayout.addWidget(self.autoCenter_checkBox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ImageRot_label = QLabel(self.horizontalLayoutWidget_5)
        self.ImageRot_label.setObjectName(u"ImageRot_label")
        sizePolicy1.setHeightForWidth(self.ImageRot_label.sizePolicy().hasHeightForWidth())
        self.ImageRot_label.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.ImageRot_label)

        self.imageRot_value = QDoubleSpinBox(self.horizontalLayoutWidget_5)
        self.imageRot_value.setObjectName(u"imageRot_value")
        sizePolicy2.setHeightForWidth(self.imageRot_value.sizePolicy().hasHeightForWidth())
        self.imageRot_value.setSizePolicy(sizePolicy2)
        self.imageRot_value.setMinimum(-360.000000000000000)
        self.imageRot_value.setMaximum(360.000000000000000)

        self.horizontalLayout_3.addWidget(self.imageRot_value)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.ApplyButton = QPushButton(self.horizontalLayoutWidget_5)
        self.ApplyButton.setObjectName(u"ApplyButton")

        self.verticalLayout.addWidget(self.ApplyButton)


        self.horizontalLayout_10.addLayout(self.verticalLayout)

        self.VMI_axis_layout = GraphicsLayoutWidget(self.horizontalLayoutWidget_5)
        self.VMI_axis_layout.setObjectName(u"VMI_axis_layout")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.VMI_axis_layout.sizePolicy().hasHeightForWidth())
        self.VMI_axis_layout.setSizePolicy(sizePolicy5)

        self.horizontalLayout_10.addWidget(self.VMI_axis_layout)

        self.horizontalLayout_10.setStretch(1, 5)

        self.retranslateUi(VMI_panel)

        QMetaObject.connectSlotsByName(VMI_panel)
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
        self.ImageCentY_label.setText(QCoreApplication.translate("VMI_panel", u"CenterY", None))
        self.ImageCentX_label.setText(QCoreApplication.translate("VMI_panel", u"CenterX", None))
        self.autoCenter_checkBox.setText(QCoreApplication.translate("VMI_panel", u"AutoCenter", None))
        self.ImageRot_label.setText(QCoreApplication.translate("VMI_panel", u"Image rotation", None))
        self.ApplyButton.setText(QCoreApplication.translate("VMI_panel", u"PushButton", None))
    # retranslateUi

