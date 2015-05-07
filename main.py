__version__ = "0.0.4"
import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.widget import Widget
from kivy import platform
from kivy.lang import Builder
from gui import MainMenu
from gui import GUIHandler

import gettext
en = gettext.translation("en",localedir="locale",languages=["en"])
de = gettext.translation("de",localedir="locale",languages=["de"])
en.install()

class ChumPyApp(App):
    def buttonPressed(*args):
        GUIHandler.Button.buttonPressed(*args)

    def loadKVfiles(self):
        Builder.load_file("gui/mainmenu.kv")

    def build(self):
        self.loadKVfiles()
        #platform is either win, linux, android, macosx or unknown
        if platform == 'android':
            ui = MainMenu.Mobile()
        else:
            ui = MainMenu.Desktop()
        return ui


if __name__ == "__main__":
    ChumPyApp().run()
