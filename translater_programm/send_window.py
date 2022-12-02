import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLineEdit, QPushButton


class Send_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('send_window.ui', self)
        self.start_button.clicked.connect(self.start)

    def start(self):
        pass

    def klient(self):
        pass

    def server(self):
        pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Send_Window()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())