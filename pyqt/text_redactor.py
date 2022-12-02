import sys
import os.path

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLineEdit, QPushButton


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('text_redactor.ui', self)  # Загружаем дизайн
        self.make_file.clicked.connect(self._make_file)
        self.save_file.clicked.connect(self._save_file)
        self.open_file.clicked.connect(self._open_file)

    def _make_file(self):
        self.label.setText("")

    def _save_file(self):
        with open(self.file_name.text(), "w") as f:
            mytext = self.label.toPlainText()
            f.write(mytext)

    def _open_file(self):
        if os.path.exists(self.file_name.text()):
            with open(self.file_name.text(), "r") as f:
                file = f.read()
            self.label.setText(file)
        else:
            self.label.setText("Wrong file name")


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
