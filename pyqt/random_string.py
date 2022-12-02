import sys
import random

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLineEdit


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('random_file.ui', self)  # Загружаем дизайн
        with open("lines.txt", "r") as file:
            self.lines = file.readlines()
        self.pushButton.clicked.connect(self.button)

    def button(self):
        self.lineEdit.setText(random.choice(self.lines))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())