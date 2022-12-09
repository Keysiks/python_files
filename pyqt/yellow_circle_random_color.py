import sys
import random

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLineEdit, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QPoint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('yellow_circle.ui', self)
        self.button.clicked.connect(self.paint)
        self.do_paint = False
        self.colors = ["yellow", "red", "blue", "green", "brown", "black"]

    def paintEvent(self, event):
        if self.do_paint is True:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        qp.setBrush(QColor(random.choice(self.colors)))
        r = random.randint(100, 300)
        qp.drawEllipse(QPoint(random.randint(200, 600), random.randint(200, 600)), r, r)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
