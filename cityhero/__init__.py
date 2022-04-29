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
            "Accept":"application/json, text/javascript, */*; q=0.01",
            "X-Requested-With":"XMLHttpRequest",
            "User-Agent":"Mozilla/5.0 (Linux; Android 10; PACM00 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/045806 Mobile Safari/537.36 MMWEBID/6680 MicroMessenger/8.0.1.1841(0x2800015C) Process/tools WeChat/arm32 Weixin NetType/4G Language/zh_CN ABI/arm64",
            "Content-Type":"application/json;charset=UTF-8",
            "Origin":"http://pay.zk2016.com",
            "Referer":"http://pay.zk2016.com/web/index_membercenter.do?B=215ab968-3797-e911-85df-d7af90092ad6",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
        }
        
        try:
            self.sign = self.__sign()
            self.seach = self.__seach()
            print("[cyan]Suessfully[/cyan]")
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

        try:
            self.CustID = res["userinfo"]["CustID"]
            self.referer = self.signurl+"?PlaceID="+ self.placeID
            self.Name = res["userinfo"]["Name"]
            self.Cions = res["userinfo"]["Coins"]
            #print(self.Name,self.Cions)
        except:
            self.CustID = None
    def __seach(self):
        self.__headers["Referer"] = self.referer
        data = {
            "CustID":self.CustID,
            "PlaceID":self.placeID
        }
        try:
            respose = self.s.post(url=self.signurl,
                                headers=self.__headers,
                                data=json.dumps(data)
                                )
           
        except:
            return  None
        
        # print(respose.text)
        res = respose.json()
        
        try:
            # 签到的状态
            self.status = res['ResultMsg']

        except:
            self.status = None
        
