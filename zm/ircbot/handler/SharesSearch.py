import http.client
from zm.ircbot.util.IOUtil import IoUtil
import json

class SharesSearch:

    def __init__(self):
        self._host = "hq.sinajs.cn"
        self._requset = "/list="

    def execute(self, shares_id):
        rst = "我不知道你在说什么"
        if shares_id == None:
            return "请给我一个股票代码"
        reqeust = self._requset + self.getLocation(shares_id) + shares_id
        IoUtil.print("Start to send request %s%s\r\n" % (self._host, reqeust))
        conn = http.client.HTTPConnection(self._host)
        conn.request("GET", reqeust)
        response = conn.getresponse()
        status = response.status
        reason = response.reason
        IoUtil.print("Request result. Status %s,reason:%s\r\n" % (status, reason))
        if status == 200:
            shares = Shares(response.read().decode('gbk'))
            rst = shares.get_string()

        if rst == None:
            rst = "机器人遇到了未知的问题！！！奔溃中"

        return rst

    def getLocation(self,shares_id):
        if shares_id.startswith("60"):
            return "sh"
        elif shares_id.startswith("300") or shares_id.startswith("002"):
            return "sz"
        else:
            return ""
class Shares:
    def __init__(self,shares_info_str):
        self._shares_info = shares_info_str.split(',')

    def get_name(self):
        name = self._shares_info[0].split("=\"")[1]
        return name

    def get_cheng_jiao(self):
        amount = float(self._shares_info[9])
        return amount / 10000

    def get_string(self):
        if len(self._shares_info) < 31:
            return None
        return ">>> %s <<<:今日开盘价:%s,昨日收盘价:%s,当前价格：%s，今日最高：%s，今日最低：%s，买一：%s，卖一：%s，成交股票数量（百股）：%s，成交金额（万元）：%s，买二(股数)：%s，买二：%s，日期：%s %s"  \
                %(self.get_name(),self._shares_info[1],self._shares_info[2],self._shares_info[3],self._shares_info[4],self._shares_info[5],self._shares_info[6],self._shares_info[7] \
                  ,self._shares_info[8],self.get_cheng_jiao(),self._shares_info[12],self._shares_info[13],self._shares_info[30],self._shares_info[31])
if __name__ =="__main__":
    s = SharesSearch()
    kk = s.execute("600354")
    print (kk)