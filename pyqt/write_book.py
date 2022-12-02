import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLineEdit


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('write_book.ui', self)  # Загружаем дизайн
        self.button_add.clicked.connect(self.button)
        self.write_book = []

    def button(self):
        name = self.name_input.text()
        phone = self.phone_input.text()
        self.write_book.append([name, phone])
        self.listwidget.setText("\n".join([" ".join(i) for i in self.write_book]))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())