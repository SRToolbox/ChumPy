import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.widget import Widget

class MainMenu(Widget):
    pass

class ChumPyApp(App):
    def build(self):
        return MainMenu()

if __name__ == "__main__":
    ChumPyApp().run()
