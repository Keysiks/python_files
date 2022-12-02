import sys
import random

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLineEdit, QPushButton
from PIL import ImageDraw, Image


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Координаты')
        self.wrong_coords = []
        self.button1 = QPushButton(self)
        self.button1.move(610, 0)
        self.button1.resize(191, 51)
        for i in range(610, 610 + 192):
            for j in range(0, 52):
                self.wrong_coords.append((i, j))
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.mouse_coords = (event.x(), event.y())
        if self.mouse_coords in self.wrong_coords:
            a, b = random.randint(0, 609), random.randint(0, 500)
            self.button1.move(a, b)
            self.wrong_coords = []
            for i in range(a, a + 192):
                for j in range(b, 52 + b):
                    self.wrong_coords.append((i, j))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())