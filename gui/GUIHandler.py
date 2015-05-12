import util
from gui.strings import mainmenu
from kivy.logger import Logger
class Button:

    @staticmethod
    def buttonPressed(app, origin, button):
        Button.mappings[button]()
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
        pass

    mappings = {
        mainmenu.create:CreateButtonPressed,
        mainmenu.maintain:MaintainButtonPressed,
        mainmenu.play:PlayButtonPressed,
        mainmenu.gamemaster:GameMasterButtonPressed,
        mainmenu.tools:ToolsButtonPressed,
        mainmenu.about:AboutButtonPressed,
    }
