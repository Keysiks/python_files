import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLineEdit, QPushButton


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('text_flag.ui', self)
        self.make_button.clicked.connect(self.enter_flag)

    def enter_flag(self):
        self.result_label.setText(f"Цвета: {self.group_1.checkedButton().text()}, "
                                  f"{self.group_2.checkedButton().text()}, "
                                  f"{self.group_3.checkedButton().text()}")


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())