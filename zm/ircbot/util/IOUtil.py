import time

from config.read_config import ConfigReader
class IoUtil:

    @classmethod
    def print(cls, msg):
        timeStr = time.strftime('%H:%M:%S',time.localtime())
        print (timeStr +" "+ msg,end='')


    @classmethod
    def debug(cls,msg):
        if ConfigReader.get_debug_flag() == 1:
            timeStr = time.strftime('%H:%M:%S',time.localtime())
            print ("Debug:" + timeStr +" "+ msg,end='')
