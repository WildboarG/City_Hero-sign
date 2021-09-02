# -*- coding: utf-8 -*-
# @Time    : 2021/9/2 17:52
# @Author  : 坏狗i
from configparser import ConfigParser
import requests
import json


#WechatId ="osnijv3u51YTY4DvX1rX90Z-gy8M"
#PublicOpenID="oGwGAv2zCrR2Vay-QgYagl6FPhIk"

def login():
    cfg = ConfigParser()
    cfg.read("base.cfg")
    placeID = cfg.get("ID","placeID")
    WechatId = cfg.get("ID","WechatId")
    PublicOpenID = cfg.get("ID","PublicOpenID")
    print(placeID)
    s = requests.session()
    url = "http://pay.zk2016.com/api/web/getwealth.do"
    signurl = "http://pay.zk2016.com/api/web/SignIn.do"
    headers={
                "Host":"pay.zk2016.com",
                "Connection":"keep-alive",
                #"Content-Length":"138",
                "Accept":"application/json, text/javascript, */*; q=0.01",
                "X-Requested-With":"XMLHttpRequest",
                "User-Agent":"Mozilla/5.0 (Linux; Android 10; PACM00 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/045806 Mobile Safari/537.36 MMWEBID/6680 MicroMessenger/8.0.1.1841(0x2800015C) Process/tools WeChat/arm32 Weixin NetType/4G Language/zh_CN ABI/arm64",
                "Content-Type":"application/json;charset=UTF-8",
                "Origin":"http://pay.zk2016.com",
                "Referer":"http://pay.zk2016.com/web/index_membercenter.do?B=215ab968-3797-e911-85df-d7af90092ad6",
                "Accept-Encoding":"gzip, deflate",
                "Accept-Language":"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                #"Cookie":"JSESSIONID=6EE93830009B2B192D86CD8FFE8B73E9"
    }
    data_json = json.dumps(
                           { "PlaceID":placeID,
                            "WechatId":WechatId,
                            "PublicOpenID":PublicOpenID})
    res = s.post(url,headers=headers,data=data_json)
    b = res.json()
    CustID = b['userinfo']["CustID"]
    Number = b['userinfo']["Number"]
    Name = b['userinfo']["Name"]
    Coins = b['userinfo']["Coins"]
    Money = b['userinfo']["Money"]
    content = "卡号: "+Number+"\n名字："+Name+"\n余币："+str(Coins)+"\nMoney: "+str(Money)
    referer = signurl+"?PlaceID="+ placeID
    headers["Referer"]=referer
    #print(headers)
    data = json.dumps({
        "CustID":CustID,
        "PlaceID":placeID
    })
    resp = s.post(url=signurl,headers=headers,data=data)
    c = resp.json()
    resultMsg = c['ResultMsg']
    result = content + "\n"+resultMsg
    print(result)
    #return result

if __name__=="__main__":
    login()

