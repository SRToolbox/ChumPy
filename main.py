__version__ = "0.0.4"
import kivy
kivy.require("1.9.0")
import util
from util.languagemanager import LanguageManager
from util.screenmanager import ScreenManager
from kivy import platform
from kivy.app import App
from kivy.uix.widget import Widget
import gui
from gui.mainmenu import MainMenu
from gui.about import About
from gui.eventhandler import ButtonHandler

class ChumPyApp(App):
    ScreenManager = ScreenManager()
    LanguageManager = LanguageManager()

    def buttonPressed(*args):
        ButtonHandler.buttonPressed(*args)

    def initializeScreenManager(self):
        ScreenManager.registerScreen(MainMenu(name=util.strings.mainmenu))
        ScreenManager.registerScreen(About(name=util.strings.about))
        ScreenManager.switchTo(util.strings.mainmenu)

    def build(self):
        LanguageManager.SetEN()
        self.initializeScreenManager()
        return ScreenManager.getManager()

if __name__ == "__main__":
    ChumPyApp().run()
