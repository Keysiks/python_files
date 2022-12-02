import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLineEdit, QPlainTextEdit


class MyWidget(QMainWindow, QCheckBox, QLineEdit, QPlainTextEdit):
    def __init__(self):
        super().__init__()
        uic.loadUi('makdak.ui', self)  # Загружаем дизайн
        self.order = []
        self.printf = ["Ваш заказ:"]
        self.price = {"Чизбургер": 15, "Нагетсы": 30, "Кола": 10, "Гамбургер": 20}
        self.checkBox1.clicked.connect(self.makeorder)
        self.checkBox2.clicked.connect(self.makeorder)
        self.checkBox3.clicked.connect(self.makeorder)
        self.checkBox4.clicked.connect(self.makeorder)
        self.make_order.clicked.connect(self.make)
        self.menu.setEnabled(False)
        self.lineEdit1.setEnabled(False)
        self.lineEdit2.setEnabled(False)
        self.lineEdit3.setEnabled(False)
        self.lineEdit4.setEnabled(False)

    def makeorder(self):
        food = self.sender().text()
        if food not in self.order:
            if food == "Чизбургер":
                self.lineEdit1.setEnabled(True)
                self.lineEdit1.setText("1")
            elif food == "Кола":
                self.lineEdit2.setEnabled(True)
                self.lineEdit2.setText("1")
            elif food == "Нагетсы":
                self.lineEdit3.setEnabled(True)
                self.lineEdit3.setText("1")
            else:
                self.lineEdit4.setEnabled(True)
                self.lineEdit4.setText("1")
            self.order.append(food)
        else:
            if food == "Чизбургер":
                self.lineEdit1.setEnabled(False)
                self.lineEdit1.setText("")
            elif food == "Кола":
                self.lineEdit2.setEnabled(False)
                self.lineEdit2.setText("")
            elif food == "Нагетсы":
                self.lineEdit3.setEnabled(False)
                self.lineEdit3.setText("")
            else:
                self.lineEdit4.setEnabled(False)
                self.lineEdit4.setText("")
            del self.order[self.order.index(food)]
        self.menu.setPlainText("")

    def make(self):
        amount = 0
        for i in self.order:
            food = i
            if food == "Чизбургер":
                x = self.lineEdit1.text()
            elif food == "Кола":
                x = self.lineEdit2.text()
            elif food == "Нагетсы":
                x = self.lineEdit3.text()
            else:
                x = self.lineEdit4.text()
            print(x)
            amount += self.price[food] * int(x)
            self.printf.append(f"{food}-----{x}-----{self.price[food]}")
        self.printf.append(f"Всего: {amount}")
        self.menu.setPlainText("\n\n".join(self.printf))
        self.printf = ["Ваш заказ:"]

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())