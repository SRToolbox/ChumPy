import util
class Button:

    @staticmethod
    def buttonPressed(*args):
        origin = args[1]
        button = args[2]
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
        _("Create"):CreateButtonPressed,
        _("Maintain"):MaintainButtonPressed,
        _("Play"):PlayButtonPressed,
        _("GameMaster"):GameMasterButtonPressed,
        _("Tools"):ToolsButtonPressed,
        _("About"):AboutButtonPressed,
    }
