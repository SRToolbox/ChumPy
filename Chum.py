import kivy
kivy.require("1.9.0")

from kivy.app import App
from gui import MainMenu

class ChumPy(App):
    def build(self):
        return MainMenu.MainMenu()

if __name__ == "__main__":
    ChumPy().run()
