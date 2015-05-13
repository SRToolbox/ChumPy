import gettext
import util
from util import strings
class LanguageManager():
    Current = ""

    def Set(language, name):
        language.install()
        current = name
        util.Logger.info("LanguageManager:Language set to "+name)
        #root.ScreenManager.requestUpdate()

    def TrySet(caller,languageName):
        util.Logger.info("LanguageManager:Attempting to set Language to "+languageName)
        LanguageManager.mappings[languageName]()
    
    def SetEN():
        en = gettext.translation("en",localedir="locale",languages=["en"])
        LanguageManager.Set(en,strings.english)

    def SetDE():
        de = gettext.translation("de",localedir="locale",languages=["de"])
        LanguageManager.Set(de,strings.german)

    mappings = {
        strings.german:SetDE,
        strings.english:SetEN,
    }
