import sys
import random

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLineEdit, QLabel, QPushButton, QLCDNumber


class MyWidget(QMainWindow, QLineEdit, QLabel, QPushButton, QLCDNumber):
    def __init__(self):
        super().__init__()
        uic.loadUi('num.ui', self)  # Загружаем дизайн
        self.num_plus = random.randint(1, 100)
        self.num_minus = random.randint(1, 100)
        self.motions1 = 10
        self.num = random.randint(1, 100)
        self.motions.display(self.motions1)
        self.now_number.display(self.num)
        self.button_plus.setText(str(self.num_plus))
        self.button_minus.setText(str(-self.num_minus))
        self.button_plus.clicked.connect(self.button)
        self.button_minus.clicked.connect(self.button)

    def button(self):
        sender = self.sender().text()
        if int(sender) == self.num_plus:
            self.num += self.num_plus
        else:
            self.num -= self.num_minus
        self.motions1 -= 1
        self.motions.display(self.motions1)
        self.now_number.display(self.num)
        if self.num == 0:
            self.win()
        if self.motions1 == 0:
            self.motion_0()
        self.label.setText("")

    def motion_0(self):
        #self.label.setText("Вы проиграли, начните игру заново")
        self.num_plus = random.randint(1, 100)
        self.num_minus = random.randint(1, 100)
        self.motions1 = 10
        self.num = random.randint(1, 100)
        self.motions.display(self.motions1)
        self.now_number.display(self.num)
        self.button_plus.setText(str(self.num_plus))
        self.button_minus.setText(str(-self.num_minus))
        self.button_plus.clicked.connect(self.button)
        self.button_minus.clicked.connect(self.button)

    def win(self):
        #self.label.setText("Вы выиграли, начните игру заново")
        self.num_plus = random.randint(1, 100)
        self.num_minus = random.randint(1, 100)
        self.motions1 = 10
        self.num = random.randint(1, 100)
        self.motions.display(self.motions1)
        self.now_number.display(self.num)
        self.button_plus.setText(str(self.num_plus))
        self.button_minus.setText(str(-self.num_minus))
        self.button_plus.clicked.connect(self.button)
        self.button_minus.clicked.connect(self.button)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
