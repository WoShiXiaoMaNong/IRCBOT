
from zm.ircbot.util.ClientHelpr import ClientHelper

def main():
    host = "chat.freenode.net"
    port = 6667
    client = ClientHelper(host,port)
    client.start("MrkkkBot","MrkkkBot","MrkkkBot","mrkkkbottest")
   #client.sendPublicMsg("mrkkkbottest","test message")

if __name__ == '__main__':
    main()
