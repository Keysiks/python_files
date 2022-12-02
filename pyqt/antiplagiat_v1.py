import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLineEdit, QPushButton


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('antoplagiat_v1.ui', self)
        self.check.clicked.connect(self.check_text)

    def check_text(self):
        text1 = self.text1.toPlainText()
        text2 = self.text2.toPlainText()
        res = self.check_result(text1, text2)
        predel = float(self.predel.text())
        if res >= predel:
            self.result.setText(str(res))
            self.result.setStyleSheet("background-color: red;")
        else:
            self.result.setText(str(res))
            self.result.setStyleSheet("background-color: green;")

    def check_result(self, text1, text2):
        amount = 0
        s1, s2 = '', ''
        for i in text1:
            if i != '':
                s1 += i
        for i in text2:
            if i != '':
                s2 += i
        k1 = s1.count("\n")
        k2 = s2.count("\n")
        s1, s2 = s1.split('\n'), s2.split('\n')
        print(s1, "\n", s2)
        for i in range(min(len(s1), len(s2))):
            if s1[i] == s2[i]:
                print("+")
                amount += 1

        if len(s1) < len(s2):
            return amount / (k1 + 1) * 100
        else:
            return amount / (k2 + 1) * 100


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
