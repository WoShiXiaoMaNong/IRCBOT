import os
import configparser

cur_path = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(cur_path,'config.ini')
conf = configparser.ConfigParser()
conf.read(config_path,"utf-8")

class ConfigReader:

    @classmethod
    def getMoudleName(cls,key):
        return conf.get("moudle",key.strip())

    @classmethod
    def getClassName(cls, key):
        return conf.get("class", key.strip())

    @classmethod
    def getCityId(cls, cityName):
        return conf.get("cityMapping", cityName.strip())

    def getValue(self,type,value):
        v = ''
