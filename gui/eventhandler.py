import util
from gui import strings
from kivy.logger import Logger
class ButtonHandler:
    @staticmethod
    def buttonPressed(app, origin, button):
        appReference = app
        ButtonHandler.mappings[button]()
        pass

    def CreateButtonPressed():
        pass

    def MaintainButtonPressed():
        pass

    def PlayButtonPressed():
        pass

    def GameMasterButtonPressed():
        pass

    def ToolsButtonPressed():
        pass

    def AboutButtonPressed():
        #appReference.UIManager.OpenAbout()

    mappings = {
        strings.create:CreateButtonPressed,
        strings.maintain:MaintainButtonPressed,
        strings.play:PlayButtonPressed,
        strings.gamemaster:GameMasterButtonPressed,
        strings.tools:ToolsButtonPressed,
        strings.about:AboutButtonPressed,
    }
