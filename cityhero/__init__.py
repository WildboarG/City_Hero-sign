import requests
import json
from  test import *
from rich import print
## 创建一个类  
class Hero:
    def __init__(self,WechatId,PublicOpenID):
        
        self.WechatId = WechatId
        self.PublicOpenID = PublicOpenID
        self.placeID = "c4bf4cdd-a5f3-4e0d-926f-7f67e2042cc7"
        
        self.s = requests.session()
        self.url = "http://pay.zk2016.com/api/web/getwealth.do"
        self.signurl = "http://pay.zk2016.com/api/web/SignIn.do"
        self.__headers={
            "Host":"pay.zk2016.com",
            "Connection":"keep-alive",
            "Content-Length":"98",
            "Accept":"application/json, text/javascript, */*; q=0.01",
            "X-Requested-With":"XMLHttpRequest",
            "User-Agent":"Mozilla/5.0 (Linux; Android 12; 22041211AC Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3211 MMWEBSDK/20220303 Mobile Safari/537.36 MMWEBID/966 MicroMessenger/8.0.21.2120(0x280015E5) Process/toolsmp WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64",
            "Content-Type":"application/json; charset=UTF-8",
            "Origin":"http://pay.zk2016.com",
            "Referer":"http://pay.zk2016.com/web/index_membercenter.do?B=215ab968-3797-e911-85df-d7af90092ad6",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
        }
        
        try:
            print("[cyan]start...[/cyan]")

            self.sign = self.__sign()
            headers1 = {
                "Host":"pay.zk2016.com",
                #Connection":"keep-alive",
                "Content-Type":"application/json; charset=UTF-8",
                "Upgrade-Insecure-Requests":"1",
                "User-Agent":"Mozilla/5.0 (Linux; Android 12; 22041211AC Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3211 MMWEBSDK/20220303 Mobile Safari/537.36 MMWEBID/966 MicroMessenger/8.0.21.2120(0x280015E5) Process/toolsmp WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/wxpic,image/tpg,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "X-Requested-With":"com.tencent.mm",
                "Referer":"http://pay.zk2016.com/web/signin.do?PlaceID=c4bf4cdd-a5f3-4e0d-926f-7f67e2042cc7",
                "Accept-Encoding":"gzip, deflate",
                "Accept-Language":"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                "cookie":"serveropenid_215ab968-3797-e911-85df-d7af90092ad6=osnijv3u51YTY4DvX1rX90Z-gy8M; branchopenid_wxc89501e85bc2b259_215ab968-3797-e911-85df-d7af90092ad6=oGwGAv2zCrR2Vay-QgYagl6FPhIk; BranchID=215ab968-3797-e911-85df-d7af90092ad6; PublicPlaceID215ab968-3797-e911-85df-d7af90092ad6=c4bf4cdd-a5f3-4e0d-926f-7f67e2042cc7; placeName215ab968-3797-e911-85df-d7af90092ad6=%u90D1%u5DDE%u57CE%u5E02%u82F1%u96C4%u65E0%u9650%u57CE%u5E97; JSESSIONID=A1883AC7808D964F1932F9FF850D3978"
            }
            a = self.s.get(url="http://pay.zk2016.com/web/signin.do?PlaceID=c4bf4cdd-a5f3-4e0d-926f-7f67e2042cc7",
                headers=headers1)
            #print(a.text)
            self.seach = self.__seach()
            message = """
Title: "城市英雄无限城自动签到"\n
name: {}\n
cions: {}\n
status: {}\n
            """.format(self.Name,self.Cions,self.status)
            print(message)
            
        
        except:
            pass
    def __sign(self):
        #cook = test.cooks()[:43]
        #print(cook)
        
        #self.__headers['Cookie'] = cook
        data = {"PlaceID":self.placeID,
                "WechatId":self.WechatId,
                "PublicOpenID":self.PublicOpenID
            }
        try:
            respose = self.s.post(
                url=self.url,
                headers=self.__headers,
                data=json.dumps(data)
                )

        except:
            return  None
        # print(respose.text)
        res = respose.json()
        #print(res)
        try:
            self.CustID = res["userinfo"]["CustID"]
           # print(self.CustID)
            self.referer = "http://pay.zk2016.com/web/signin.do?PlaceID=c4bf4cdd-a5f3-4e0d-926f-7f67e2042cc7"
            self.Name = res["userinfo"]["Name"]
            self.Cions = res["userinfo"]["Coins"]
            #print(self.Name,self.Cions)
        except:
            self.CustID = None
    def __seach(self):
        self.__headers["Referer"] = self.referer
        #print(self.__headers)
        data = {
            "CustID":self.CustID,
           # "PageSize":"10",
            "PlaceID":self.placeID
        }
        #print(data)
        try:
            # sult = self.s.post(url="http://pay.zk2016.com/api/web/SignInList.do",headers=self.__headers,data=json.dumps(data))
            # print(sult.json())
            head = {
                "Host": "pay.zk2016.com",
                "Connection": "keep-alive",
                "User-Agent": "Mozilla/5.0 (Linux; Android 12; 22041211AC Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3211 MMWEBSDK/20220303 Mobile Safari/537.36 MMWEBID/966 MicroMessenger/8.0.21.2120(0x280015E5) Process/toolsmp WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64",
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": "http://pay.zk2016.com/web/signin.do?PlaceID=c4bf4cdd-a5f3-4e0d-926f-7f67e2042cc7",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                "Content-Type": "application/json; charset=UTF-8",
                "Origin":"http://pay.zk2016.com"
            }
            respose =   requests.post(url=self.signurl,
                                headers=head,
                                #data=json.dumps(data)
                                data = json.dumps(data)
                                )
           
        except:
            return  None
        
        #print(respose.text)
        res = respose.json()
        #print(res)
        try:
            # 签到的状态
            self.status = res['ResultMsg']
            #print(self.status)
            return self.status
        except:
            self.status = None
        
