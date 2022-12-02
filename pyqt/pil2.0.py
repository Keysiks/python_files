import sys

from PyQt5 import uic  # Импортируем uic
from PIL import Image
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLineEdit, QFileDialog, QLabel
from PyQt5.QtGui import QPixmap


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('pil2.0.ui', self)  # Загружаем дизайн
        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.start_picture = QPixmap(fname)
        self.now_picture = self.start_picture
        self.picture.setPixmap(self.start_picture)
        self.Button_All.clicked.connect(self.setcolor)
        self.Button_left.clicked.connect(self.setcolor)

    def setcolor(self):
        sender = self.sender().text()
        if sender == "ALL":
            self.picture.setPixmap(self.start_picture)
            self.now_picture = self.start_picture
        elif sender.lower() == "против часовой стрелки":
            img = Image.open(self.now_picture)
            img = img.transpose(Image.ROTATE_90)
            img.save(self.now_picture)
            self.now_picture = QPixmap(self.now_picture)
            self.picture.setPixmap(self.now_picture)
        elif sender.lower() == "по часовой стрелке":
            self.now_picture.rotate(-90)
            self.picture.setPixmap(self.now_picture)

    def for_set_color(self):
        pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())