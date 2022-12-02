import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt


class MyWidget(QMainWindow):
    def __init__(self, name):
        super().__init__()
        self.user_name = name
        uic.loadUi('terminal.ui', self)
        icon = QIcon("icon.png")
        self.setWindowIcon(icon)
        self.setWindowTitle("Terminal")
        self.comand_field.setFrameStyle(False)
        self.start_text = f"Напишите /help и Маруся поможет Вам\n \n{self.user_name}:\\comand>"
        self.local_text = self.start_text
        self.comand_field.setText(self.start_text)
        text = self.comand_field.toPlainText()
        self.line = 3
        print(text.split("\n"))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter:
            text = self.comand_field.toPlainText()
            self.local_text = text
            text = text.split("\n")
            comand = text[self.line - 1].split(">")[1]
            self.line += 1
            if comand == "/help":
                print("+")
                self.local_text += "\n"
                self.local_text += "Маруся поможет Вам! Вот список команд:"
                self.comand_field.setText(self.local_text)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget("Kirill")
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())