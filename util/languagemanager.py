import gettext
import util
from util import strings
class LanguageManager():
    Current = ""

    def getSettings():
        setting = {strings.setting_currentLanguage:LanguageManager.Current}
        return setting

    def loadSettings(settings):
        Current = settings.get(strings.setting_currentLanguage)["value"]
        util.Logger.info("LanguageManager:Read "+strings.setting_currentLanguage+" : "+Current)

    def Set(language, name):
        language.install()
        LanguageManager.Current = name
        util.Logger.info("LanguageManager:Language set to "+name)

    def TrySet(self,languageName):
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
