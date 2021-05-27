import os, configparser
from dotenv import load_dotenv

load_dotenv()

class LoadProperties():

    def getConfig(self):
        return self.config

    def getHome(self):
        return self.home

    def getOutPutFolder(self):
        return self.outPutFolder

    def getAppProp(self):
        return self.appProp
    
    def getLoadGift(self):
        return self.loadGift

    def getParameters(self):
        return {
                'config': self.config,
                'home': self.home,
                'outPutFolder': self.outPutFolder,
                'config': self.config,
                'loadGift': self.loadGift,
                'rootPath' : self.rootPath,
                'windowIcon': self.windowIcon
                }        

    def __init__(self, parent=None):
        self.config = configparser.ConfigParser()
        self.rootPath = os.getcwd()
        self.home = os.getenv('HOME')
        self.outPutFolder = os.getenv('OUTPUT_FOLDER')
        self.appProp = os.path.join(self.rootPath, os.getenv('CONFIG_FOLDER'), os.getenv('PROPERTIES'))
        self.loadGift = os.path.join(self.rootPath, os.getenv('ICONS_FOLDER'), os.getenv('LOAD_GIF'))
        self.config.read(self.appProp)
        self.windowIcon = os.path.join(self.rootPath, 'icons', self.config.get('THEME', 'window.icon'))
