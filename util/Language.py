import gettext
class Change():

    @staticmethod
    def DE():
        de = gettext.translation("de",localedir="locale",languages=["de"])
        de.install()

    @staticmethod
    def EN():
        en = gettext.translation("en",localedir="locale",languages=["en"])
        en.install()
