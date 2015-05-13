import gettext
import util
from util import strings
class LanguageManager():
    Current = ""

    def Set(app,language, name):
        language.install()
        current = name
        util.Logger.info("LanguageManager:Language set to "+name)
        app.ScreenManager.requestUpdate()

    def TrySet(app, languageName):
        util.Logger.info("LanguageManager:Attempting to set Language to "+languageName)
        LanguageManager.mappings[languageName](app)

    def SetEN(app):
        en = gettext.translation("en",localedir="locale",languages=["en"])
        LanguageManager.Set(app,en,strings.english)

    def SetDE(app):
        de = gettext.translation("de",localedir="locale",languages=["de"])
        LanguageManager.Set(app,de,strings.german)

    mappings = {
        strings.german:SetDE,
        strings.english:SetEN,
    }
