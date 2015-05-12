import util
from gui import strings
from kivy.logger import Logger
class ButtonHandler:
    def buttonPressed(app, origin, button):
        ButtonHandler.mappings[button](app)
        pass

    def CreateButtonPressed(app):
        pass

    def MaintainButtonPressed(app):
        pass

    def PlayButtonPressed(app):
        pass

    def GameMasterButtonPressed(app):
        pass

    def ToolsButtonPressed(app):
        pass

    def AboutButtonPressed(app):
        app.ScreenManager.switchTo(strings.about)

    mappings = {
        strings.create:CreateButtonPressed,
        strings.maintain:MaintainButtonPressed,
        strings.play:PlayButtonPressed,
        strings.gamemaster:GameMasterButtonPressed,
        strings.tools:ToolsButtonPressed,
        strings.about:AboutButtonPressed,
    }
