from config.read_config import ConfigReader
from zm.ircbot.util.ClientHelpr import ClientHelper


def main():
    host = ConfigReader.get_host()
    port = ConfigReader.get_port()
    client = ClientHelper(host,port)
    nick_name = ConfigReader.get_nick_name()
    user_name = ConfigReader.get_user_name()
    real_name = ConfigReader.get_real_name()
    chanel = ConfigReader.get_chanel()
    client.start(nick_name,user_name,real_name,chanel)


if __name__ == '__main__':
    main()
