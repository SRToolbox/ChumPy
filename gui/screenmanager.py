import gui
from kivy import uix
class ScreenManager():
    manager = uix.screenmanager.ScreenManager()
    def registerScreen(screen):
        gui.Logger.info("ScreenManager:Registered Screen "+screen.name)
        ScreenManager.manager.add_widget(screen)

    @staticmethod
    def switchTo(screenName):
        gui.Logger.info("ScreenManager:Switched to "+screenName)
        ScreenManager.manager.current = screenName

    def getManager():
        return ScreenManager.manager
