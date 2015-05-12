import gettext
class Changer():

    @staticmethod
    def switchDE():
        de = gettext.translation("de",localedir="locale",languages=["de"])
        de.install()

    @staticmethod
    def switchEN():
        en = gettext.translation("en",localedir="locale",languages=["en"])
        en.install()
