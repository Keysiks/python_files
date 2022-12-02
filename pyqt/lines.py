import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLineEdit, QPushButton


class MyWidget(QMainWindow):
    def __init__(self):
        self.f, self.change = 1, 0
        super().__init__()
        uic.loadUi('lines.ui', self)  # Загружаем дизайн
        with open("lines.txt", "r") as f:
            self.file = f.readlines()
        self.output_button.clicked.connect(self.button)
        print(self.file)

    def button(self):
        if self.f == 1:
            self.output.setText('\n'.join([self.file[i] for i in range(1, len(self.file), 2)]))
            print('\n'.join([self.file[i] for i in range(1, len(self.file), 2)]))
        else:
            self.output.setText(''.join([self.file[i] for i in range(0, len(self.file), 2)]))
            print('\n'.join([self.file[i] for i in range(0, len(self.file), 2)]))
        self.f, self.change = self.change, self.f


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())