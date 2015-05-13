from kivy.uix.screenmanager import ScreenManager,SlideTransition
import util
class ScreenManager():
    manager = ScreenManager()
    last = None

    def getSettings():
        return {}

    def registerScreen(screen):
        util.Logger.info("ScreenManager:Registered Screen "+screen.name)
        ScreenManager.manager.add_widget(screen)

    @staticmethod
    def requestUpdate():
        pass

    @staticmethod
    def setSlideRight():
        ScreenManager.manager.transition = SlideTransition(direction="right")

    @staticmethod
    def setSlideLeft():
        ScreenManager.manager.transition = SlideTransition(direction="left")

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
