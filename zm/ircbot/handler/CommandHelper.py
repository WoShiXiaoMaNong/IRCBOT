
from zm.ircbot.handler.HandlerBase import Handler
from config.command_config import command_config

class CommandHelper(Handler):

    def __init__(self):
        Handler.__init__(self)

    def execute(self, irc_msg):
        rst = "我不知道你在说什么"
        command = irc_msg.get_param()
        rst = command_config.get_command_help_msg(command)

        if rst is None:
            rst = "目前不支持这个功能：%s" % command
        else:
            rst = "命令<%s>" % command + " --->" + rst
        return rst




if __name__ =="__main__":
    s = CommandHelper()
    kk = s.execute("fanyi")
    print (kk)