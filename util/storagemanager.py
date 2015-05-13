import util
from kivy.storage.jsonstore import JsonStore
class StorageManager():
    store = JsonStore("settings.json")

    def loadSettings():
        return StorageManager.store

    def writeSettings(*args):
        for setting in args:
            util.Logger.info("StorageManager:Writing "+str(setting))
            for key,value in setting.items():
                StorageManager.store.put(key,value=value)
