# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VMI_toolbox.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QGridLayout, QHBoxLayout, QLabel, QProgressBar,
    QPushButton, QSizePolicy, QSlider, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_VMI_toolbox_panel(object):
    def setupUi(self, VMI_toolbox_panel):
        if not VMI_toolbox_panel.objectName():
            VMI_toolbox_panel.setObjectName(u"VMI_toolbox_panel")
        VMI_toolbox_panel.resize(423, 435)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VMI_toolbox_panel.sizePolicy().hasHeightForWidth())
        VMI_toolbox_panel.setSizePolicy(sizePolicy)
        VMI_toolbox_panel.setMinimumSize(QSize(271, 297))
        self.data_filter_label = QLabel(VMI_toolbox_panel)
        self.data_filter_label.setObjectName(u"data_filter_label")
        self.data_filter_label.setGeometry(QRect(90, 320, 47, 13))
        self.data_filter_slider = QSlider(VMI_toolbox_panel)
        self.data_filter_slider.setObjectName(u"data_filter_slider")
        self.data_filter_slider.setGeometry(QRect(140, 320, 101, 22))
        self.data_filter_slider.setOrientation(Qt.Horizontal)
        self.widget = QWidget(VMI_toolbox_panel)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(21, 11, 329, 117))
        self.horizontalLayout_9 = QHBoxLayout(self.widget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.imageCentX_label = QLabel(self.widget)
        self.imageCentX_label.setObjectName(u"imageCentX_label")

        self.horizontalLayout_5.addWidget(self.imageCentX_label)

        self.imageCentX_value = QDoubleSpinBox(self.widget)
        self.imageCentX_value.setObjectName(u"imageCentX_value")
        self.imageCentX_value.setKeyboardTracking(False)
        self.imageCentX_value.setMinimum(-1500.000000000000000)
        self.imageCentX_value.setMaximum(1500.000000000000000)

        self.horizontalLayout_5.addWidget(self.imageCentX_value)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.imageCentY_label = QLabel(self.widget)
        self.imageCentY_label.setObjectName(u"imageCentY_label")

        self.horizontalLayout_6.addWidget(self.imageCentY_label)

        self.imageCentY_value = QDoubleSpinBox(self.widget)
        self.imageCentY_value.setObjectName(u"imageCentY_value")
        self.imageCentY_value.setKeyboardTracking(False)
        self.imageCentY_value.setMinimum(-1500.000000000000000)
        self.imageCentY_value.setMaximum(1500.000000000000000)
        self.imageCentY_value.setValue(0.000000000000000)

        self.horizontalLayout_6.addWidget(self.imageCentY_value)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_6)


        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.center_type_combobox = QComboBox(self.widget)
        self.center_type_combobox.addItem("")
        self.center_type_combobox.addItem("")
        self.center_type_combobox.addItem("")
        self.center_type_combobox.setObjectName(u"center_type_combobox")

        self.horizontalLayout_8.addWidget(self.center_type_combobox)

        self.findcenter_button = QPushButton(self.widget)
        self.findcenter_button.setObjectName(u"findcenter_button")

        self.horizontalLayout_8.addWidget(self.findcenter_button)


        self.gridLayout.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Rmin_label = QLabel(self.widget)
        self.Rmin_label.setObjectName(u"Rmin_label")

        self.horizontalLayout_2.addWidget(self.Rmin_label)

        self.Rmin_spinbox = QDoubleSpinBox(self.widget)
        self.Rmin_spinbox.setObjectName(u"Rmin_spinbox")
        self.Rmin_spinbox.setKeyboardTracking(False)
        self.Rmin_spinbox.setMaximum(1500.000000000000000)

        self.horizontalLayout_2.addWidget(self.Rmin_spinbox)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Rmax_label = QLabel(self.widget)
        self.Rmax_label.setObjectName(u"Rmax_label")

        self.horizontalLayout.addWidget(self.Rmax_label)

        self.Rmax_spinbox = QDoubleSpinBox(self.widget)
        self.Rmax_spinbox.setObjectName(u"Rmax_spinbox")
        self.Rmax_spinbox.setKeyboardTracking(False)
        self.Rmax_spinbox.setMaximum(1500.000000000000000)
        self.Rmax_spinbox.setValue(500.000000000000000)

        self.horizontalLayout.addWidget(self.Rmax_spinbox)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.imageRot_label = QLabel(self.widget)
        self.imageRot_label.setObjectName(u"imageRot_label")

        self.horizontalLayout_7.addWidget(self.imageRot_label)

        self.imageRot_value = QDoubleSpinBox(self.widget)
        self.imageRot_value.setObjectName(u"imageRot_value")
        self.imageRot_value.setKeyboardTracking(False)
        self.imageRot_value.setMinimum(-360.000000000000000)
        self.imageRot_value.setMaximum(360.000000000000000)

        self.horizontalLayout_7.addWidget(self.imageRot_value)


        self.gridLayout.addLayout(self.horizontalLayout_7, 3, 0, 1, 1)


        self.horizontalLayout_9.addLayout(self.gridLayout)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.showAxis_checkBox = QCheckBox(self.widget)
        self.showAxis_checkBox.setObjectName(u"showAxis_checkBox")
        self.showAxis_checkBox.setChecked(True)

        self.verticalLayout_5.addWidget(self.showAxis_checkBox)

        self.showCenter_checkBox = QCheckBox(self.widget)
        self.showCenter_checkBox.setObjectName(u"showCenter_checkBox")
        self.showCenter_checkBox.setChecked(True)

        self.verticalLayout_5.addWidget(self.showCenter_checkBox)

        self.showRange_checkBox = QCheckBox(self.widget)
        self.showRange_checkBox.setObjectName(u"showRange_checkBox")
        self.showRange_checkBox.setChecked(True)

        self.verticalLayout_5.addWidget(self.showRange_checkBox)


        self.horizontalLayout_9.addLayout(self.verticalLayout_5)

        self.widget1 = QWidget(VMI_toolbox_panel)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(70, 210, 193, 77))
        self.horizontalLayout_15 = QHBoxLayout(self.widget1)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.matrix_checkBox = QCheckBox(self.widget1)
        self.matrix_checkBox.setObjectName(u"matrix_checkBox")

        self.verticalLayout_2.addWidget(self.matrix_checkBox)

        self.calculatematrix_pushbutton = QPushButton(self.widget1)
        self.calculatematrix_pushbutton.setObjectName(u"calculatematrix_pushbutton")

        self.verticalLayout_2.addWidget(self.calculatematrix_pushbutton)

        self.progressBar = QProgressBar(self.widget1)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout_2.addWidget(self.progressBar)


        self.horizontalLayout_15.addLayout(self.verticalLayout_2)

        self.abel_inversion_pushbutton_2 = QPushButton(self.widget1)
        self.abel_inversion_pushbutton_2.setObjectName(u"abel_inversion_pushbutton_2")

        self.horizontalLayout_15.addWidget(self.abel_inversion_pushbutton_2)

        self.widget2 = QWidget(VMI_toolbox_panel)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(21, 141, 258, 57))
        self.verticalLayout = QVBoxLayout(self.widget2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.abel_inversion_sel_label = QLabel(self.widget2)
        self.abel_inversion_sel_label.setObjectName(u"abel_inversion_sel_label")

        self.horizontalLayout_13.addWidget(self.abel_inversion_sel_label)

        self.abel_inversion_sel_combobox = QComboBox(self.widget2)
        self.abel_inversion_sel_combobox.addItem("")
        self.abel_inversion_sel_combobox.addItem("")
        self.abel_inversion_sel_combobox.addItem("")
        self.abel_inversion_sel_combobox.addItem("")
        self.abel_inversion_sel_combobox.addItem("")
        self.abel_inversion_sel_combobox.addItem("")
        self.abel_inversion_sel_combobox.addItem("")
        self.abel_inversion_sel_combobox.setObjectName(u"abel_inversion_sel_combobox")

        self.horizontalLayout_13.addWidget(self.abel_inversion_sel_combobox)

        self.abel_inversion_pushbutton = QPushButton(self.widget2)
        self.abel_inversion_pushbutton.setObjectName(u"abel_inversion_pushbutton")

        self.horizontalLayout_13.addWidget(self.abel_inversion_pushbutton)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.abel_inversion_NPhotons_label = QLabel(self.widget2)
        self.abel_inversion_NPhotons_label.setObjectName(u"abel_inversion_NPhotons_label")

        self.horizontalLayout_10.addWidget(self.abel_inversion_NPhotons_label)

        self.abel_inversion_NPhotons_value = QSpinBox(self.widget2)
        self.abel_inversion_NPhotons_value.setObjectName(u"abel_inversion_NPhotons_value")
        self.abel_inversion_NPhotons_value.setSingleStep(0)
        self.abel_inversion_NPhotons_value.setValue(2)

        self.horizontalLayout_10.addWidget(self.abel_inversion_NPhotons_value)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.dTheta_label = QLabel(self.widget2)
        self.dTheta_label.setObjectName(u"dTheta_label")

        self.horizontalLayout_11.addWidget(self.dTheta_label)

        self.dTheta_value = QDoubleSpinBox(self.widget2)
        self.dTheta_value.setObjectName(u"dTheta_value")
        self.dTheta_value.setKeyboardTracking(False)
        self.dTheta_value.setMaximum(360.000000000000000)

        self.horizontalLayout_11.addWidget(self.dTheta_value)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.dR_label = QLabel(self.widget2)
        self.dR_label.setObjectName(u"dR_label")

        self.horizontalLayout_12.addWidget(self.dR_label)

        self.dR_value = QDoubleSpinBox(self.widget2)
        self.dR_value.setObjectName(u"dR_value")
        self.dR_value.setKeyboardTracking(False)
        self.dR_value.setMaximum(1.000000000000000)
        self.dR_value.setValue(1.000000000000000)

        self.horizontalLayout_12.addWidget(self.dR_value)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_12)


        self.verticalLayout.addLayout(self.horizontalLayout_14)


        self.retranslateUi(VMI_toolbox_panel)

        QMetaObject.connectSlotsByName(VMI_toolbox_panel)
    # setupUi

    def retranslateUi(self, VMI_toolbox_panel):
        VMI_toolbox_panel.setWindowTitle(QCoreApplication.translate("VMI_toolbox_panel", u"Form", None))
        self.data_filter_label.setText(QCoreApplication.translate("VMI_toolbox_panel", u"Filtering", None))
        self.imageCentX_label.setText(QCoreApplication.translate("VMI_toolbox_panel", u"CenterX", None))
        self.imageCentY_label.setText(QCoreApplication.translate("VMI_toolbox_panel", u"CenterY", None))
        self.center_type_combobox.setItemText(0, QCoreApplication.translate("VMI_toolbox_panel", u"Fixed center", None))
        self.center_type_combobox.setItemText(1, QCoreApplication.translate("VMI_toolbox_panel", u"Mean center", None))
        self.center_type_combobox.setItemText(2, QCoreApplication.translate("VMI_toolbox_panel", u"Simplex center", None))

        self.findcenter_button.setText(QCoreApplication.translate("VMI_toolbox_panel", u"Find Center!", None))
        self.Rmin_label.setText(QCoreApplication.translate("VMI_toolbox_panel", u"Rmin", None))
        self.Rmax_label.setText(QCoreApplication.translate("VMI_toolbox_panel", u"Rmax", None))
        self.imageRot_label.setText(QCoreApplication.translate("VMI_toolbox_panel", u"Image rotation", None))
        self.showAxis_checkBox.setText(QCoreApplication.translate("VMI_toolbox_panel", u"Show Axis", None))
        self.showCenter_checkBox.setText(QCoreApplication.translate("VMI_toolbox_panel", u"Show Center", None))
        self.showRange_checkBox.setText(QCoreApplication.translate("VMI_toolbox_panel", u"Show Range", None))
        self.matrix_checkBox.setText(QCoreApplication.translate("VMI_toolbox_panel", u"Matrix exist?", None))
        self.calculatematrix_pushbutton.setText(QCoreApplication.translate("VMI_toolbox_panel", u"Precalculate matrix", None))
        self.abel_inversion_pushbutton_2.setText(QCoreApplication.translate("VMI_toolbox_panel", u"Try me!", None))
        self.abel_inversion_sel_label.setText(QCoreApplication.translate("VMI_toolbox_panel", u"Algorithm", None))
        self.abel_inversion_sel_combobox.setItemText(0, QCoreApplication.translate("VMI_toolbox_panel", u"Abel Davis", None))
        self.abel_inversion_sel_combobox.setItemText(1, QCoreApplication.translate("VMI_toolbox_panel", u"Basex", None))
        self.abel_inversion_sel_combobox.setItemText(2, QCoreApplication.translate("VMI_toolbox_panel", u"Dasch", None))
        self.abel_inversion_sel_combobox.setItemText(3, QCoreApplication.translate("VMI_toolbox_panel", u"Direct", None))
        self.abel_inversion_sel_combobox.setItemText(4, QCoreApplication.translate("VMI_toolbox_panel", u"Hansenlaw", None))
        self.abel_inversion_sel_combobox.setItemText(5, QCoreApplication.translate("VMI_toolbox_panel", u"Linbasex", None))
        self.abel_inversion_sel_combobox.setItemText(6, QCoreApplication.translate("VMI_toolbox_panel", u"Onion peeling", None))

        self.abel_inversion_pushbutton.setText(QCoreApplication.translate("VMI_toolbox_panel", u"Invert image", None))
        self.abel_inversion_NPhotons_label.setText(QCoreApplication.translate("VMI_toolbox_panel", u"Nphtons", None))
        self.dTheta_label.setText(QCoreApplication.translate("VMI_toolbox_panel", u"dTheta", None))
        self.dR_label.setText(QCoreApplication.translate("VMI_toolbox_panel", u"dR", None))
    # retranslateUi

