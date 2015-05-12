import gettext
class LanguageChanger():
    @staticmethod
    def SetDE():
        de = gettext.translation("de",localedir="locale",languages=["de"])
        de.install()

    @staticmethod
    def SetEN():
        en = gettext.translation("en",localedir="locale",languages=["en"])
        en.install()
