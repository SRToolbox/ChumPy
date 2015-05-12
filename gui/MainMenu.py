import kivy
kivy.require("1.9.0")

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

class MainMenu(Screen):
    kivy.logger.Logger.info("MainMenu:Initialized")
    Builder.load_file("gui/mainmenu.kv")
