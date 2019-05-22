import os
import configparser

cur_path = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(cur_path,'config.ini')
conf = configparser.ConfigParser()
conf.read(config_path,"utf-8")

# City name-id mapping for WeatherSearch.py
city_config_path = os.path.join(cur_path,'CityMapping.ini')
city_config = configparser.ConfigParser()
city_config.read(city_config_path,"utf-8")


class ConfigReader:

    @classmethod
    def get_debug_flag(cls):
        return int(cls.__get_value(conf,"DEBUG_INFO",'debug'))

    @classmethod
    def getMoudleName(cls,key):
        return cls.__get_value(conf,"moudle",key.strip())

    @classmethod
    def getClassName(cls, key):
        return cls.__get_value(conf,"class", key.strip())

    @classmethod
    def getCityId(cls, cityName):
        return cls.__get_value(city_config,"cityMapping", cityName.strip())

    @classmethod
    def get_thread_pool_size(cls):
        return int(cls.__get_value(conf,"thread_pool", "pool_size"))

    @classmethod
    def get_thread_pool_size(cls):
        return int(cls.__get_value(conf,"thread_pool", "pool_size"))

    @classmethod
    def get_host(cls):
        return cls.__get_value(conf,"IRC_INFO", "host")

    @classmethod
    def get_port(cls):
        return int(cls.__get_value(conf,"IRC_INFO", "port"))

    @classmethod
    def get_nick_name(cls):
        return cls.__get_value(conf,"IRC_INFO", "nick_name")

    @classmethod
    def get_user_name(cls):
        return cls.__get_value(conf,"IRC_INFO", "nick_name")

    @classmethod
    def get_real_name(cls):
        return cls.__get_value(conf,"IRC_INFO", "real_name")

    @classmethod
    def get_chanel(cls):
        return cls.__get_value(conf,"IRC_INFO", "chanel")
    @classmethod
    def __get_value(cls,config, type, key):
        from zm.ircbot.util.IOUtil import IoUtil
        value = None
        try:
            value = config.get(type, key)
        except:
            value = None
        IoUtil.print("Get value by type - key(%s - %s):%s\r\n" %(type, key, value))
        return value
