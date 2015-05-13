import gui
from kivy import uix
class ScreenManager():
    manager = uix.screenmanager.ScreenManager()
    last = None
    def registerScreen(screen):
        gui.Logger.info("ScreenManager:Registered Screen "+screen.name)
        ScreenManager.manager.add_widget(screen)

    @staticmethod
    def requestUpdate():
        ScreenManager.manager.current.canvas.ask_update()

    @staticmethod
    def setSlideRight():
        ScreenManager.manager.transition = uix.screenmanager.SlideTransition(direction="right")

    @staticmethod
    def setSlideLeft():
        ScreenManager.manager.transition = uix.screenmanager.SlideTransition(direction="left")

    @staticmethod
    def switchTo(screenName):
        ScreenManager.last = ScreenManager.manager.current
        ScreenManager.manager.current = screenName

    @staticmethod
    def switchToLast():
        if not ScreenManager.last is None:
            ScreenManager.switchTo(ScreenManager.last)

    def getManager():
        return ScreenManager.manager
