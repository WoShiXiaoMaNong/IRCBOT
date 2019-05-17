import time
class IoUtil:

    @classmethod
    def print(cls, msg):
        timeStr = time.strftime('%H:%M:%S',time.localtime())
        print (timeStr +" "+ msg)