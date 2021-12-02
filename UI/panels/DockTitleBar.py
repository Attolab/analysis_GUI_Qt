from PySide6 import QtGui, QtCore
from PySide6.QtWidgets import QWidget


class DockTitleBar(QWidget):
    def __init__(self, dockWidget):
        super(DockTitleBar, self).__init__(dockWidget)

        boxLayout = QtGui.QHBoxLayout(self)
        boxLayout.setSpacing(1)
        boxLayout.setMargin(1)

        self.titleLabel = QtGui.QLabel(self)
        self.titleEdit = QtGui.QLineEdit(self)
        self.titleEdit.hide()
        self.titleEdit.editingFinished.connect(self.finishEdit)

        iconSize = QtGui.QApplication.style().standardIcon(
            QtGui.QStyle.SP_TitleBarNormalButton).actualSize(
                QtCore.QSize(100, 100))
        buttonSize = iconSize + QtCore.QSize(4, 4)

        self.dockButton = QtGui.QToolButton(self)
        self.dockButton.setIcon(QtGui.QApplication.style().standardIcon(
            QtGui.QStyle.SP_TitleBarNormalButton))
        self.dockButton.setMaximumSize(buttonSize)
        self.dockButton.setAutoRaise(True)
        self.dockButton.clicked.connect(self.toggleFloating)

        self.closeButton = QtGui.QToolButton(self)
        self.closeButton.setMaximumSize(buttonSize)
        self.closeButton.setAutoRaise(True)
        self.closeButton.setIcon(QtGui.QApplication.style().standardIcon(
            QtGui.QStyle.SP_DockWidgetCloseButton))
        self.closeButton.clicked.connect(self.closeParent)

        boxLayout.addSpacing(2)
        boxLayout.addWidget(self.titleLabel)
        boxLayout.addWidget(self.titleEdit)
        boxLayout.addStretch()
        boxLayout.addSpacing(5)
        boxLayout.addWidget(self.dockButton)
        boxLayout.addWidget(self.closeButton)

        dockWidget.featuresChanged.connect(self.onFeaturesChanged)

        self.onFeaturesChanged(dockWidget.features())
        self.setTitle(dockWidget.windowTitle())

        dockWidget.installEventFilter(self)

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.WindowTitleChange:
            self.setTitle(source.windowTitle())
        return super(DockTitleBar, self).eventFilter(source, event)

    def startEdit(self):
        self.titleLabel.hide()
        self.titleEdit.show()
        self.titleEdit.setFocus()

    def finishEdit(self):
        self.titleEdit.hide()
        self.titleLabel.show()
        self.parent().setWindowTitle(self.titleEdit.text())

    def onFeaturesChanged(self, features):
        if not features & QtGui.QDockWidget.DockWidgetVerticalTitleBar:
            self.closeButton.setVisible(
                features & QtGui.QDockWidget.DockWidgetClosable)
            self.dockButton.setVisible(
                features & QtGui.QDockWidget.DockWidgetFloatable)
        else:
            raise ValueError('vertical title bar not supported')

    def setTitle(self, title):
        self.titleLabel.setText(title)
        self.titleEdit.setText(title)

    def toggleFloating(self):
        self.parent().setFloating(not self.parent().isFloating())

    def closeParent(self):
        self.parent().toggleViewAction().setChecked(False)
        self.parent().hide()

    def mouseDoubleClickEvent(self, event):
        if event.pos().x() <= self.titleLabel.width():
            self.startEdit()
        else:
            # this keeps the normal double-click behaviour
            super(DockTitleBar, self).mouseDoubleClickEvent(event)

    def mouseReleaseEvent(self, event):
        event.ignore()

    def mousePressEvent(self, event):
        event.ignore()

    def mouseMoveEvent(self, event):
        event.ignore()