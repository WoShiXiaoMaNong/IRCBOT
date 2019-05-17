from zm.ircbot.util.IOUtil import IoUtil
import sys
from config.read_config import ConfigReader

class MainHandler:

    def __init__(self,clienthelper):
        self._clientHelper =clienthelper

    def excute(self,msg):
        nickFrom = msg.split('!')[0].replace(':', '')
        message = ':'.join(msg.split(':')[2:])
        if self._clientHelper.isSendToMe(message):
            IoUtil.print("%s:>>>>%s<<<<<\r\n" % (nickFrom, message.replace("\r\n", "")))
            result = self.doExcute(message)
            self._clientHelper.sendMsg(nickFrom + ":" + result)
        else:
            IoUtil.print("%s %s" % (nickFrom, message))




    def doExcute(self,msg):
        handlerName = msg.split(':')[1]
        message = msg.split(':')[2]
        moudleName = ConfigReader.getMoudleName(handlerName)
        className = ConfigReader.getClassName(handlerName)
        m = __import__(moudleName,fromlist=True)
        class_name=getattr(m,className)
        obj=class_name()
        return obj.search(message.replace("\r\n",""))

if __name__ == "__main__":
    print("ss")
    m = __import__("zm.ircbot.handler.weatherSearch", fromlist=True)
    class_name = getattr(m, "WeatherSerch")
    print (class_name)
    obj = class_name()
    print (obj.search("101030300"))