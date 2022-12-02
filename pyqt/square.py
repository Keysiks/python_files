import sys

from PyQt5 import uic  # Импортируем uic
from PIL import Image, ImageDraw
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('square.ui', self)  # Загружаем дизайн_
        self.button.clicked.connect(self.draw)

    def draw(self):
        self.side = int(self.line_side.text())
        self.k = float(self.line_k.text())
        self.n = int(self.line_n.text())
        picture = Image.new("RGB", (self.side, self.side), (0, 0, 0))
        drawer = ImageDraw.Draw(picture)
        x = self.side
        picture.setPen(QColor(255, 0, 0))
        for i in range(self.n):
            drawer.rectangle(((abs(x - self.side), abs(x - self.side)), (x, x)))
            x *= self.k
        picture.save("picta.jpeg")

        im = QPixmap("picta.jpeg")
        self.image.setPixmap(im)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
