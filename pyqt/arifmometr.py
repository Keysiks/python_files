import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLineEdit


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('arifmometr.ui', self)  # Загружаем дизайн
        self.pushButton1.clicked.connect(self.button)
        self.pushButton2.clicked.connect(self.button)
        self.pushButton3.clicked.connect(self.button)

    def button(self):
        text = self.sender().text()
        if text == "+":
            self.label2.setText(str(int(self.input1.text()) + int(self.input2.text())))
        elif text == "*":
            self.label2.setText(str(int(self.input1.text()) * int(self.input2.text())))
        else:
            self.label2.setText(str(int(self.input1.text()) - int(self.input2.text())))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())