import gettext
en = gettext.translation("en",localedir="locale",languages=["en"])
de = gettext.translation("de",localedir="locale",languages=["de"])
en.install()

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
