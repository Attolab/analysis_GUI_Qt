# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calibration_panel.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QSplitter, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_Calibration_Panel(object):
    def setupUi(self, Calibration_Panel):
        if not Calibration_Panel.objectName():
            Calibration_Panel.setObjectName(u"Calibration_Panel")
        Calibration_Panel.resize(864, 655)
        self.groupBox_2 = QGroupBox(Calibration_Panel)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(30, 50, 521, 131))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.horizontalLayoutWidget_2 = QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 20, 181, 64))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.t0_label = QLabel(self.horizontalLayoutWidget_2)
        self.t0_label.setObjectName(u"t0_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.t0_label.sizePolicy().hasHeightForWidth())
        self.t0_label.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.t0_label)

        self.kE_label = QLabel(self.horizontalLayoutWidget_2)
        self.kE_label.setObjectName(u"kE_label")
        sizePolicy1.setHeightForWidth(self.kE_label.sizePolicy().hasHeightForWidth())
        self.kE_label.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.kE_label)

        self.kV_label = QLabel(self.horizontalLayoutWidget_2)
        self.kV_label.setObjectName(u"kV_label")
        sizePolicy1.setHeightForWidth(self.kV_label.sizePolicy().hasHeightForWidth())
        self.kV_label.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.kV_label)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetMaximumSize)
        self.t0_value = QLineEdit(self.horizontalLayoutWidget_2)
        self.t0_value.setObjectName(u"t0_value")
        sizePolicy.setHeightForWidth(self.t0_value.sizePolicy().hasHeightForWidth())
        self.t0_value.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.t0_value)

        self.kE_value = QLineEdit(self.horizontalLayoutWidget_2)
        self.kE_value.setObjectName(u"kE_value")
        sizePolicy.setHeightForWidth(self.kE_value.sizePolicy().hasHeightForWidth())
        self.kE_value.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.kE_value)

        self.kV_value = QLineEdit(self.horizontalLayoutWidget_2)
        self.kV_value.setObjectName(u"kV_value")
        sizePolicy.setHeightForWidth(self.kV_value.sizePolicy().hasHeightForWidth())
        self.kV_value.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.kV_value)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(260, 40, 239, 25))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.closeButton = QPushButton(self.layoutWidget)
        self.closeButton.setObjectName(u"closeButton")

        self.horizontalLayout.addWidget(self.closeButton)

        self.applyButton = QPushButton(self.layoutWidget)
        self.applyButton.setObjectName(u"applyButton")

        self.horizontalLayout.addWidget(self.applyButton)

        self.saveButton = QPushButton(self.layoutWidget)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout.addWidget(self.saveButton)

        self.kE_label_2 = QLabel(self.groupBox_2)
        self.kE_label_2.setObjectName(u"kE_label_2")
        self.kE_label_2.setGeometry(QRect(270, 10, 171, 16))
        self.splitter = QSplitter(Calibration_Panel)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(30, 190, 521, 384))
        self.splitter.setOrientation(Qt.Vertical)
        self.ToF_axis = PlotWidget(self.splitter)
        self.ToF_axis.setObjectName(u"ToF_axis")
        sizePolicy.setHeightForWidth(self.ToF_axis.sizePolicy().hasHeightForWidth())
        self.ToF_axis.setSizePolicy(sizePolicy)
        self.splitter.addWidget(self.ToF_axis)

        self.retranslateUi(Calibration_Panel)

        QMetaObject.connectSlotsByName(Calibration_Panel)
    # setupUi

    def retranslateUi(self, Calibration_Panel):
        Calibration_Panel.setWindowTitle(QCoreApplication.translate("Calibration_Panel", u"Form", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Calibration_Panel", u"Calibration Parameters", None))
        self.t0_label.setText(QCoreApplication.translate("Calibration_Panel", u"t0", None))
        self.kE_label.setText(QCoreApplication.translate("Calibration_Panel", u"kE", None))
        self.kV_label.setText(QCoreApplication.translate("Calibration_Panel", u"kV", None))
        self.closeButton.setText(QCoreApplication.translate("Calibration_Panel", u"Close", None))
        self.applyButton.setText(QCoreApplication.translate("Calibration_Panel", u"Apply", None))
        self.saveButton.setText(QCoreApplication.translate("Calibration_Panel", u"Save as...", None))
        self.kE_label_2.setText(QCoreApplication.translate("Calibration_Panel", u"t = t0 +  kE/sqrt(E) + kV/sqrt(E-V)", None))
    # retranslateUi

