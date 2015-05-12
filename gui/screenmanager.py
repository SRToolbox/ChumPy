import gui
from kivy import uix
class ScreenManager():
    manager = uix.screenmanager.ScreenManager()
    last = None
    def registerScreen(screen):
        gui.Logger.info("ScreenManager:Registered Screen "+screen.name)
        ScreenManager.manager.add_widget(screen)

    @staticmethod
    def switchTo(screenName):
        gui.Logger.info("ScreenManager:Switched to "+screenName)
        ScreenManager.last = ScreenManager.manager.current
        ScreenManager.manager.current = screenName

    @staticmethod
    def switchToLast():
        if not ScreenManager.last is None:
            ScreenManager.switchTo(ScreenManager.last)

    def getManager():
        return ScreenManager.manager
