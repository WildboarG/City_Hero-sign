# 郑州二七无限城签到
---

##  配置  
***

##### base.cfg  
配置文件在这里
需要手动抓包抓取这三个参数
奉上我们的小可爱![HttpCanary](https://huaigou.lanzouw.com/ieL9wtilq8h)
微信关注郑州二七区城市英雄无限城
会员购币 （先注册成为会员）
打开我们的小可爱 选定微信 开始抓包
点击会员购币
等待跳转登录上就可以停掉抓包
找到这个包（http://pay.zk2016.com/api/web/getwealth.do）
id 在请求体中



    [ID]  这三个ID是必须填写
    placeID = c4bf4cdd-a5f3-4e0d-926f-7f67e20xxxxx
    WechatId = osnijv40H3JmkBgixjo20Bxxxxx
    PublicOpenID = oGwGAvwu3_e9L9HGvDslxxxxxxx  


##  运行

     #拉取依赖
     pip3 install -r requirements.txt
     #运行
     python3 main.py

---

## 说明
- 签到
- 查看硬币余额
没什么卵用如果你能坚持手动签到也可以 一天两个硬币蛮客观的

---
