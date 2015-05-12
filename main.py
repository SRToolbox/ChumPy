__version__ = "0.0.4"
import kivy
kivy.require("1.9.0")
import util
from util.languagechanger import LanguageChanger
from kivy import platform
from kivy.app import App
from kivy.uix.widget import Widget
import gui
from gui.mainmenu import MainMenu
from gui.about import About
from gui.eventhandler import ButtonHandler
from gui.screenmanager import ScreenManager

class ChumPyApp(App):
    ScreenManager = ScreenManager()

    def buttonPressed(*args):
        ButtonHandler.buttonPressed(*args)

    def initializeScreenManager(self):
        ScreenManager.registerScreen(MainMenu(name=gui.strings.mainmenu))
        ScreenManager.registerScreen(About(name=gui.strings.about))
        ScreenManager.switchTo(gui.strings.mainmenu)

    def build(self):
        LanguageChanger.SetEN()
        self.initializeScreenManager()
        return ScreenManager.getManager()

if __name__ == "__main__":
    ChumPyApp().run()
