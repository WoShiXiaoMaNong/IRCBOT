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
            result = self.doExcute(message.replace(self._clientHelper.getNickName()+":",""))
            self._clientHelper.sendMsg(nickFrom + ":" + result)
        else:
            IoUtil.print("%s %s" % (nickFrom, message))




    def doExcute(self,msg):
        command = Command(msg)
        obj = None
        if(command.is_command_msg()):
            hander_name = command.get_method()
            message = command.get_param()
            obj = self.get_handler_ojb(hander_name)
        if obj != None:
            return obj.search(message.replace("\r\n",""))
        else:
            return "听不懂你在说什么。。。"

    def get_handler_ojb(self,hander_name):
        moudle_name = ConfigReader.getMoudleName(hander_name)
        class_name = ConfigReader.getClassName(hander_name)

        if moudle_name != None and class_name != None:
            m = __import__(moudle_name, fromlist=True)
            class_name = getattr(m, class_name)
            obj = class_name()
            return obj
        else:
            return None

class Command:

    def __init__(self,command_msg):
        self._command_msg = command_msg

    def get_method(self):
        if(self.is_command_msg()):
            return self._command_msg.split(':')[0]
    def get_param(self):
        if(self.is_command_msg()):
            return self._command_msg.split(':')[1]

    def is_command_msg(self):
        if self._command_msg.find(":") == -1:
            return False
        elif len(self._command_msg.split(':')) != 2:
            return False
        return True

if __name__ == "__main__":
    print("ss")
    kk = "s:s".split(':')
    print (len(kk))
