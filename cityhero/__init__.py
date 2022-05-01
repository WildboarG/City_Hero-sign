'''
Author: WildboarG
version: 1.0
Date: 2022-04-29 15:53:37
LastEditors: WildboarG
LastEditTime: 2022-04-29 17:39:07
Descripttion: 
'''
import requests
import json
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
            "Content-Type":"application/json;charset=UTF-8",
            "Origin":"http://pay.zk2016.com",
            "Referer":"http://pay.zk2016.com/web/signin.do?PlaceID=c4bf4cdd-a5f3-4e0d-926f-7f67e2042cc7",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
        }
        
        try:
            print("[cyan]start...[/cyan]")
            self.sign = self.__sign()
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
        try:
            respose = self.s.post(url=self.signurl,
                                headers=self.__headers,
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
            print(self.status)
            return self.status
        except:
            self.status = None
        
