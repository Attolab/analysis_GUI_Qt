import numpy as np
import pyqtgraph as pg
from PySide6.QtWidgets import (QLabel)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform,QPen)
from PySide6.QtCore import (Qt)

class MyStringAxis(pg.AxisItem):
        def __init__(self, xdict, *args, **kwargs):
            pg.AxisItem.__init__(self, *args, **kwargs)
            self.x_values = np.asarray(xdict.keys())
            self.x_strings = xdict.values()

        def tickStrings(self, values, scale, spacing):
            strings = []
            for v in values:
                # vs is the original tick value
                vs = v * scale
                # if we have vs in our values, show the string
                # otherwise show nothing
                if vs in self.x_values:
                    # Find the string with x_values closest to vs
                    vstr = self.x_strings[np.abs(self.x_values-vs).argmin()]
                else:
                    vstr = ""
                strings.append(vstr)
            return strings
# class Label_onimage(QLabel):
#     def __init__(self):
#         super().__init__()

#     def paintEvent(self, text ='Hello World', image = ):
#         qp = QPainter()
#         qp.begin(self)

#         image  = QImage('im.png')
#         qp.drawImage(QPoint(), image)

#         pen = QPen(Qt.red)
#         pen.setWidth(2)
#         qp.setPen(pen)        

#         font = QFont()
#         font.setFamily('Times')
#         font.setBold(True)
#         font.setPointSize(24)
#         qp.setFont(font)

#         qp.drawText(150, 250, text)

#         qp.end()            