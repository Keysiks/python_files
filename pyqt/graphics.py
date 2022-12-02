import sys
from math import sin
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLineEdit, QPushButton


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('graphics.ui', self)
        self.button_build.clicked.connect(self.build_graphik)

    def build_graphik(self):
        func = self.function.text()
        minn = int(self.minn_d.text())
        maxx = int(self.maxx_d.text())
        self.widget.clear()
        normal_mass = []
        deletion = []
        for x in range(minn, maxx + 1):
            try:
                normal_mass.append(eval(func))
            except ZeroDivisionError:
                deletion.append(x)
        X = [i for i in range(minn, maxx + 1)]
        for i in deletion:
            del X[X.index(i)]
        print(normal_mass)
        self.widget.plot(X, normal_mass)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())