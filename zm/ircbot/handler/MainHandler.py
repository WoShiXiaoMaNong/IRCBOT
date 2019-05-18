from zm.ircbot.util.IOUtil import IoUtil
from zm.ircbot.item.IrcMsg import IrcMsg
from config.read_config import ConfigReader


class MainHandler:

    def __init__(self, client_helper):
        self._clientHelper = client_helper

    def execute(self, msg):
        irc_msg = IrcMsg(msg, self._clientHelper.getNickName())
        if irc_msg.is_to_me():
            IoUtil.print("%s:>>>>%s<<<<<\r\n" % (irc_msg.get_from_nick_name(), irc_msg.get_messge()))
            result = self.do_execute(irc_msg)
            self._clientHelper.sendMsg(irc_msg.get_from_nick_name() + ":" + result)
        else:
            IoUtil.print("%s %s" % (irc_msg.get_from_nick_name(),  irc_msg.get_messge()))

    def do_execute(self,msg):
        obj = None
        if msg.is_command_msg():
            handler_name = msg.get_method()
            message = msg.get_param()
            obj = self.get_handler_ojb(handler_name)
        if obj is not None:
            return obj.execute(message.replace("\r\n",""))
        else:
            return "听不懂你在说什么。。。"

    def get_handler_ojb(self,handler_name):
        moudle_name = ConfigReader.getMoudleName(handler_name)
        class_name = ConfigReader.getClassName(handler_name)

        if moudle_name is not None and class_name is not None:
            m = __import__(moudle_name, fromlist=True)
            class_name = getattr(m, class_name)
            obj = class_name()
            return obj
        else:
            return None



if __name__ == "__main__":
    print("ss")
    kk = "s:s".split(':')
    print (len(kk))
