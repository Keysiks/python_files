from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MainApp(App):
    def build(self):
        self.percents = ['5%', '10%', '15%', 'your own variant']
        self.keyboard = []

if __name__ == '__main__':
    app = MainApp()
    app.run()