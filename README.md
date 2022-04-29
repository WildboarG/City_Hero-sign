<!--
 * @Author: WildboarG
 * @version: 1.0
 * @Date: 2022-04-29 18:02:07
 * @LastEditors: WildboarG
 * @LastEditTime: 2022-04-29 19:17:05
 * @Descripttion: 
-->
# 郑州二七无限城签到
---
![python](https://img.shields.io/badge/cityhero-0.0.1-green)  ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fuckzk)  [![pypi_downloads_per_month](https://img.shields.io/pypi/dm/fuckzk)](https://pypi.org/project/fuckzk)  ![](https://img.shields.io/badge/License-MIT-reightgreen.svg)  ![](https://img.shields.io/badge/QQ%20Group-570418215-red)

##  配置  
##### 



需要手动抓包抓取这三个参数

> 奉上我们的小可爱[HttpCanary](https://huaigou.lanzouw.com/ieL9wtilq8h)

> 微信关注郑州二七区城市英雄无限城

> 会员购币 （先注册成为会员）

> 打开我们的小可爱 选定微信 开始抓包

> 点击会员购币

> 等待跳转登录上就可以停掉抓包

> 找到这个包（http://pay.zk2016.com/api/web/getwealth.do）

id 在请求体中



    [ID]  这两个ID是必须填写
    WechatId = osnijv40H3JmkBgixjo20Bxxxxx
    PublicOpenID = oGwGAvwu3_e9L9HGvDslxxxxxxx  

## 安装
    
     # 安装
     pip3 install cityhero

##  实现

* 创建一个main.py 文件

```python3
     from cityhero import Hero
     Hero(WechatId,PublicOpenID)
```

---

## 说明
- 签到
- 查看硬币余额
没什么卵用如果你能坚持手动签到也可以 一天两个硬币蛮客观的

---
