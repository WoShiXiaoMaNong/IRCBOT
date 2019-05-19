import os
import configparser
from zm.ircbot.util.IOUtil import IoUtil

cur_path = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(cur_path,'command.ini')
conf = configparser.ConfigParser()
conf.read(config_path,"utf-8")


class command_config:

    @classmethod
    def get_command_help_msg(cls,command):
        return cls.__get_value("command",command)

    @classmethod
    def __get_value(cls, type, key):
        value = None
        try:
            value = conf.get(type, key)
        except:
            value = None

        IoUtil.print("Get value by type - key(%s - %s):%s\r\n" %(type, key, value))
        return value
