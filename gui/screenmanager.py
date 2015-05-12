import gui
from kivy import uix
manager = uix.screenmanager.ScreenManager()
class ScreenManager():
    @staticmethod
    def registerScreen(screen):
        gui.Logger.info("ScreenManager:Registered Screen "+screen.name)
        manager.add_widget(screen)

    @staticmethod
    def switchTo(screenName):
        gui.Logger.info("ScreenManager:Switched to "+screenName)
        manager.current = screenName

    @staticmethod
    def getManager():
        return manager
