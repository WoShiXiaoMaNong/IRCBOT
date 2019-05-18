import os
import configparser

cur_path = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(cur_path,'config.ini')
conf = configparser.ConfigParser()
conf.read(config_path,"utf-8")

class ConfigReader:

    @classmethod
    def getMoudleName(cls,key):
        return cls._getValue("moudle",key.strip())

    @classmethod
    def getClassName(cls, key):
        return cls._getValue("class", key.strip())

    @classmethod
    def getCityId(cls, cityName):
        return cls._getValue("cityMapping", cityName.strip())

    @classmethod
    def _getValue(cls,type,key):
        value = None
        try:
            value = conf.get(type,key)
        except:
            value = None
        return value