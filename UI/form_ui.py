# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionCreate = QAction(MainWindow)
        self.actionCreate.setObjectName(u"actionCreate")
        self.actionGenerate = QAction(MainWindow)
        self.actionGenerate.setObjectName(u"actionGenerate")
        self.actionLoad = QAction(MainWindow)
        self.actionLoad.setObjectName(u"actionLoad")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_2 = QAction(MainWindow)
        self.actionSave_2.setObjectName(u"actionSave_2")
        self.actionClose_2 = QAction(MainWindow)
        self.actionClose_2.setObjectName(u"actionClose_2")
        self.actionErase = QAction(MainWindow)
        self.actionErase.setObjectName(u"actionErase")
        self.VMI_new = QAction(MainWindow)
        self.VMI_new.setObjectName(u"VMI_new")
        self.VMI_load = QAction(MainWindow)
        self.VMI_load.setObjectName(u"VMI_load")
        self.VMI_save = QAction(MainWindow)
        self.VMI_save.setObjectName(u"VMI_save")
        self.ToF_new = QAction(MainWindow)
        self.ToF_new.setObjectName(u"ToF_new")
        self.ToF_load = QAction(MainWindow)
        self.ToF_load.setObjectName(u"ToF_load")
        self.ToF_save = QAction(MainWindow)
        self.ToF_save.setObjectName(u"ToF_save")
        self.actionVMI_2 = QAction(MainWindow)
        self.actionVMI_2.setObjectName(u"actionVMI_2")
        self.actionMagnetic_Bottle_2 = QAction(MainWindow)
        self.actionMagnetic_Bottle_2.setObjectName(u"actionMagnetic_Bottle_2")
        self.VMI_new_3 = QAction(MainWindow)
        self.VMI_new_3.setObjectName(u"VMI_new_3")
        self.VMI_action = QAction(MainWindow)
        self.VMI_action.setObjectName(u"VMI_action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuAnalysis_GUI = QMenu(self.menubar)
        self.menuAnalysis_GUI.setObjectName(u"menuAnalysis_GUI")
        self.menuNew_session = QMenu(self.menuAnalysis_GUI)
        self.menuNew_session.setObjectName(u"menuNew_session")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAnalysis_GUI.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menuAnalysis_GUI.addAction(self.menuNew_session.menuAction())
        self.menuAnalysis_GUI.addAction(self.actionClose)
        self.menuNew_session.addAction(self.VMI_action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionCreate.setText(QCoreApplication.translate("MainWindow", u"New...", None))
        self.actionGenerate.setText(QCoreApplication.translate("MainWindow", u"Load...", None))
        self.actionLoad.setText(QCoreApplication.translate("MainWindow", u"Load...", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close GUI", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save...", None))
        self.actionSave_2.setText(QCoreApplication.translate("MainWindow", u"Save...", None))
        self.actionClose_2.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionErase.setText(QCoreApplication.translate("MainWindow", u"Erase", None))
        self.VMI_new.setText(QCoreApplication.translate("MainWindow", u"New...", None))
        self.VMI_load.setText(QCoreApplication.translate("MainWindow", u"Load...", None))
        self.VMI_save.setText(QCoreApplication.translate("MainWindow", u"Save...", None))
        self.ToF_new.setText(QCoreApplication.translate("MainWindow", u"New...", None))
        self.ToF_load.setText(QCoreApplication.translate("MainWindow", u"Load...", None))
        self.ToF_save.setText(QCoreApplication.translate("MainWindow", u"Save...", None))
        self.actionVMI_2.setText(QCoreApplication.translate("MainWindow", u"VMI", None))
        self.actionMagnetic_Bottle_2.setText(QCoreApplication.translate("MainWindow", u"Magnetic Bottle", None))
        self.VMI_new_3.setText(QCoreApplication.translate("MainWindow", u"VMI", None))
        self.VMI_action.setText(QCoreApplication.translate("MainWindow", u"VMI", None))
        self.menuAnalysis_GUI.setTitle(QCoreApplication.translate("MainWindow", u"Analysis GUI", None))
        self.menuNew_session.setTitle(QCoreApplication.translate("MainWindow", u"New session...", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
    # retranslateUi

