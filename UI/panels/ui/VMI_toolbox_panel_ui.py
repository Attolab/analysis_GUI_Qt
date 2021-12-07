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
    QHBoxLayout, QLabel, QProgressBar, QPushButton,
    QSizePolicy, QSlider, QVBoxLayout, QWidget)

class Ui_VMI_toolbox_panel(object):
    def setupUi(self, VMI_toolbox_panel):
        if not VMI_toolbox_panel.objectName():
            VMI_toolbox_panel.setObjectName(u"VMI_toolbox_panel")
        VMI_toolbox_panel.resize(271, 297)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VMI_toolbox_panel.sizePolicy().hasHeightForWidth())
        VMI_toolbox_panel.setSizePolicy(sizePolicy)
        VMI_toolbox_panel.setMinimumSize(QSize(271, 297))
        self.center_type_combobox = QComboBox(VMI_toolbox_panel)
        self.center_type_combobox.addItem("")
        self.center_type_combobox.addItem("")
        self.center_type_combobox.addItem("")
        self.center_type_combobox.setObjectName(u"center_type_combobox")
        self.center_type_combobox.setGeometry(QRect(50, 100, 91, 22))
        self.abel_inversion_sel_combobox = QComboBox(VMI_toolbox_panel)
        self.abel_inversion_sel_combobox.addItem("")
        self.abel_inversion_sel_combobox.addItem("")
        self.abel_inversion_sel_combobox.addItem("")
        self.abel_inversion_sel_combobox.addItem("")
        self.abel_inversion_sel_combobox.addItem("")
        self.abel_inversion_sel_combobox.addItem("")
        self.abel_inversion_sel_combobox.addItem("")
        self.abel_inversion_sel_combobox.setObjectName(u"abel_inversion_sel_combobox")
        self.abel_inversion_sel_combobox.setGeometry(QRect(80, 170, 91, 20))
        self.progressBar = QProgressBar(VMI_toolbox_panel)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 260, 231, 21))
        self.progressBar.setValue(24)
        self.pushButton = QPushButton(VMI_toolbox_panel)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(70, 230, 111, 23))
        self.center_type_label = QLabel(VMI_toolbox_panel)
        self.center_type_label.setObjectName(u"center_type_label")
        self.center_type_label.setGeometry(QRect(0, 100, 47, 16))
        self.abel_inversion_sel_label = QLabel(VMI_toolbox_panel)
        self.abel_inversion_sel_label.setObjectName(u"abel_inversion_sel_label")
        self.abel_inversion_sel_label.setGeometry(QRect(20, 170, 47, 13))
        self.data_filter_label = QLabel(VMI_toolbox_panel)
        self.data_filter_label.setObjectName(u"data_filter_label")
        self.data_filter_label.setGeometry(QRect(20, 200, 47, 13))
        self.data_filter_slider = QSlider(VMI_toolbox_panel)
        self.data_filter_slider.setObjectName(u"data_filter_slider")
        self.data_filter_slider.setGeometry(QRect(70, 200, 101, 22))
        self.data_filter_slider.setOrientation(Qt.Horizontal)
        self.findcenter_button = QPushButton(VMI_toolbox_panel)
        self.findcenter_button.setObjectName(u"findcenter_button")
        self.findcenter_button.setGeometry(QRect(170, 100, 81, 23))
        self.checkBox = QCheckBox(VMI_toolbox_panel)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(70, 60, 91, 17))
        self.widget = QWidget(VMI_toolbox_panel)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 0, 180, 54))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Rmin_label = QLabel(self.widget)
        self.Rmin_label.setObjectName(u"Rmin_label")

        self.horizontalLayout_2.addWidget(self.Rmin_label)

        self.Rmin_spinbox = QDoubleSpinBox(self.widget)
        self.Rmin_spinbox.setObjectName(u"Rmin_spinbox")
        self.Rmin_spinbox.setKeyboardTracking(False)

        self.horizontalLayout_2.addWidget(self.Rmin_spinbox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.Rmin_slider = QSlider(self.widget)
        self.Rmin_slider.setObjectName(u"Rmin_slider")
        self.Rmin_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.Rmin_slider)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Rmax_label = QLabel(self.widget)
        self.Rmax_label.setObjectName(u"Rmax_label")

        self.horizontalLayout.addWidget(self.Rmax_label)

        self.Rmax_spinbox = QDoubleSpinBox(self.widget)
        self.Rmax_spinbox.setObjectName(u"Rmax_spinbox")
        self.Rmax_spinbox.setKeyboardTracking(False)

        self.horizontalLayout.addWidget(self.Rmax_spinbox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.Rmax_slider = QSlider(self.widget)
        self.Rmax_slider.setObjectName(u"Rmax_slider")
        self.Rmax_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.Rmax_slider)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.retranslateUi(VMI_toolbox_panel)

        QMetaObject.connectSlotsByName(VMI_toolbox_panel)
    # setupUi

    def retranslateUi(self, VMI_toolbox_panel):
        VMI_toolbox_panel.setWindowTitle(QCoreApplication.translate("VMI_toolbox_panel", u"Form", None))
        self.center_type_combobox.setItemText(0, QCoreApplication.translate("VMI_toolbox_panel", u"Fixed center", None))
        self.center_type_combobox.setItemText(1, QCoreApplication.translate("VMI_toolbox_panel", u"Mean center", None))
        self.center_type_combobox.setItemText(2, QCoreApplication.translate("VMI_toolbox_panel", u"Simplex center", None))

        self.abel_inversion_sel_combobox.setItemText(0, QCoreApplication.translate("VMI_toolbox_panel", u"Abel Davis", None))
        self.abel_inversion_sel_combobox.setItemText(1, QCoreApplication.translate("VMI_toolbox_panel", u"Basex", None))
        self.abel_inversion_sel_combobox.setItemText(2, QCoreApplication.translate("VMI_toolbox_panel", u"Dasch", None))
        self.abel_inversion_sel_combobox.setItemText(3, QCoreApplication.translate("VMI_toolbox_panel", u"Direct", None))
        self.abel_inversion_sel_combobox.setItemText(4, QCoreApplication.translate("VMI_toolbox_panel", u"Hansenlaw", None))
        self.abel_inversion_sel_combobox.setItemText(5, QCoreApplication.translate("VMI_toolbox_panel", u"Linbasex", None))
        self.abel_inversion_sel_combobox.setItemText(6, QCoreApplication.translate("VMI_toolbox_panel", u"Onion peeling", None))

        self.pushButton.setText(QCoreApplication.translate("VMI_toolbox_panel", u"Try me!", None))
        self.center_type_label.setText(QCoreApplication.translate("VMI_toolbox_panel", u"Center", None))
        self.abel_inversion_sel_label.setText(QCoreApplication.translate("VMI_toolbox_panel", u"Algorithm", None))
        self.data_filter_label.setText(QCoreApplication.translate("VMI_toolbox_panel", u"Filtering", None))
        self.findcenter_button.setText(QCoreApplication.translate("VMI_toolbox_panel", u"Find Center!", None))
        self.checkBox.setText(QCoreApplication.translate("VMI_toolbox_panel", u"Show Range", None))
        self.Rmin_label.setText(QCoreApplication.translate("VMI_toolbox_panel", u"Rmin", None))
        self.Rmax_label.setText(QCoreApplication.translate("VMI_toolbox_panel", u"Rmax", None))
    # retranslateUi

