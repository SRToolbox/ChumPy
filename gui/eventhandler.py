import util
from util import strings
from kivy.logger import Logger
class ButtonHandler:
    def buttonPressed(app, origin, button, *args):
        ButtonHandler.mappings[button](app,*args)
        pass

    def CreateButtonPressed(app,*args):
        pass

    def MaintainButtonPressed(app,*args):
        pass

    def PlayButtonPressed(app,*args):
        pass

    def GameMasterButtonPressed(app,*args):
        pass

    def ToolsButtonPressed(app,*args):
        pass

    def AboutButtonPressed(app,*args):
        app.ScreenManager.setSlideLeft()
        app.ScreenManager.switchTo(strings.about)

    def BackButtonPressed(app,*args):
        app.ScreenManager.setSlideRight()
        app.ScreenManager.switchToLast()

    def ChangeLanguagePressed(app,*args):
        language = args[0]
        app.LanguageManager.TrySet(language)

    mappings = {
        strings.create:CreateButtonPressed,
        strings.maintain:MaintainButtonPressed,
        strings.play:PlayButtonPressed,
        strings.gamemaster:GameMasterButtonPressed,
        strings.tools:ToolsButtonPressed,
        strings.about:AboutButtonPressed,
        strings.back:BackButtonPressed,
        strings.changelanguage:ChangeLanguagePressed,
    }
