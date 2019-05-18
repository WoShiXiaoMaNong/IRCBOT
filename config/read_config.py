import os
import configparser

cur_path = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(cur_path,'config.ini')
conf = configparser.ConfigParser()
conf.read(config_path,"utf-8")

class ConfigReader:

    @classmethod
    def getMoudleName(cls,key):
        return cls.__get_value("moudle",key.strip())

    @classmethod
    def getClassName(cls, key):
        return cls.__get_value("class", key.strip())

    @classmethod
    def getCityId(cls, cityName):
        return cls.__get_value("cityMapping", cityName.strip())

    @classmethod
    def get_thread_pool_size(cls):
        return int(cls.__get_value("thread_pool", "pool_size"))

    @classmethod
    def __get_value(cls, type, key):
        value = None
        try:
            value = conf.get(type, key)
        except:
            value = None
        return value
