import requests
def cooks():
    url = "http://pay.zk2016.com/web/index_membercenter.do"
    headers = {
            "Host":"pay.zk2016.com",
            "Connection":"keep-alive",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":"Mozilla/5.0 (Linux; Android 12; 22041211AC Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3211 MMWEBSDK/20220303 Mobile Safari/537.36 MMWEBID/966 MicroMessenger/8.0.21.2120(0x280015E5) Process/toolsmp WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/wxpic,image/tpg,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "X-Requested-With":"com.tencent.mm",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cookie":"serveropenid_215ab968-3797-e911-85df-d7af90092ad6=osnijv3u51YTY4DvX1rX90Z-gy8M; branchopenid_wxc89501e85bc2b259_215ab968-3797-e911-85df-d7af90092ad6=oGwGAv2zCrR2Vay-QgYagl6FPhIk"
            }
    data = {   
                "B":"B=215ab968-3797-e911-85df-d7af90092ad6"
            }
    s = requests.Session()
    res = s.get(url,headers=headers,params=data,allow_redirects=False)
    cook = res.headers.get('Set-Cookie')
    print(cook)
    return cook
