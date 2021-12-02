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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QPlainTextEdit,
    QPushButton, QSizePolicy, QWidget)

from pyqtgraph import PlotWidget

class Ui_Calibration_Panel(object):
    def setupUi(self, Calibration_Panel):
        if not Calibration_Panel.objectName():
            Calibration_Panel.setObjectName(u"Calibration_Panel")
        Calibration_Panel.resize(639, 548)
        self.layoutWidget = QWidget(Calibration_Panel)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(380, 40, 239, 25))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.tof_view = PlotWidget(Calibration_Panel)
        self.tof_view.setObjectName(u"tof_view")
        self.tof_view.setGeometry(QRect(0, 290, 631, 121))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tof_view.sizePolicy().hasHeightForWidth())
        self.tof_view.setSizePolicy(sizePolicy)
        self.tof_view_2 = PlotWidget(Calibration_Panel)
        self.tof_view_2.setObjectName(u"tof_view_2")
        self.tof_view_2.setGeometry(QRect(0, 410, 631, 131))
        sizePolicy.setHeightForWidth(self.tof_view_2.sizePolicy().hasHeightForWidth())
        self.tof_view_2.setSizePolicy(sizePolicy)
        self.groupBox = QGroupBox(Calibration_Panel)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 60, 251, 141))
        self.plainTextEdit_6 = QPlainTextEdit(self.groupBox)
        self.plainTextEdit_6.setObjectName(u"plainTextEdit_6")
        self.plainTextEdit_6.setGeometry(QRect(100, 100, 81, 21))
        self.plainTextEdit_4 = QPlainTextEdit(self.groupBox)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setGeometry(QRect(100, 60, 81, 21))
        self.plainTextEdit_3 = QPlainTextEdit(self.groupBox)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setEnabled(False)
        self.plainTextEdit_3.setGeometry(QRect(30, 100, 71, 21))
        self.plainTextEdit_3.setReadOnly(True)
        self.plainTextEdit = QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QRect(30, 60, 71, 21))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit_2 = QPlainTextEdit(self.groupBox)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setEnabled(False)
        self.plainTextEdit_2.setGeometry(QRect(30, 80, 71, 21))
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_5 = QPlainTextEdit(self.groupBox)
        self.plainTextEdit_5.setObjectName(u"plainTextEdit_5")
        self.plainTextEdit_5.setGeometry(QRect(100, 80, 81, 21))

        self.retranslateUi(Calibration_Panel)

        QMetaObject.connectSlotsByName(Calibration_Panel)
    # setupUi

    def retranslateUi(self, Calibration_Panel):
        Calibration_Panel.setWindowTitle(QCoreApplication.translate("Calibration_Panel", u"Form", None))
        self.pushButton_3.setText(QCoreApplication.translate("Calibration_Panel", u"Close", None))
        self.pushButton_2.setText(QCoreApplication.translate("Calibration_Panel", u"Apply", None))
        self.pushButton.setText(QCoreApplication.translate("Calibration_Panel", u"Save as...", None))
        self.groupBox.setTitle(QCoreApplication.translate("Calibration_Panel", u"GroupBox", None))
        self.plainTextEdit_6.setPlainText("")
        self.plainTextEdit_4.setPlainText("")
        self.plainTextEdit_3.setPlainText(QCoreApplication.translate("Calibration_Panel", u"kV", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("Calibration_Panel", u"t0", None))
        self.plainTextEdit_2.setPlainText(QCoreApplication.translate("Calibration_Panel", u"kE", None))
        self.plainTextEdit_5.setPlainText("")
    # retranslateUi

