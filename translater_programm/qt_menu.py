import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('webcam_menu.ui', self)
        self.setWindowTitle("WEB_CAM_PROJECT")
        #установка изображения главного экрана
        self.fon = QPixmap("fon.jpg")
        self.image.setPixmap(self.fon)
        #Процесс печатания приветственного текста
        self.hello_text.setFrameStyle(False)
        self.hello_text.setEnabled(False)
        self.text_for_hello_edit = "Приветствую Вас в моем проекте Web_Cam project...\n" \
                                   "Этот проект создан в фановых целях...\n" \
                                   "В процессе использования проекта\n" \
                                   "Вам будет помогать мой ассистент  - Маруся...\n" \
                                   "Жми НАЧАТЬ и поехали!...\n" \
                                   "Надеюсь проект вам понравится =)...\n"
        self.timer = QTimer()
        self.printed = 1
        self.timer.start(50)
        self.timer.timeout.connect(self.end_timer_hello_text)
        #обработка кнопки "НАЧАТЬ"
        self.start_button.hide()
        self.start_button.clicked.connect(self.start)

    def end_timer_hello_text(self):
        self.hello_text.setText(self.text_for_hello_edit[:self.printed])
        self.printed += 1
        if self.printed >= len(self.text_for_hello_edit):
            del self.timer
            self.start_button.show()

    def start(self):
        pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())