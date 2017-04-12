#!/usr/bin/env python
# -*- coding:utf-8 -*-  
import sys,os
import requests
import json

#本文件请求开源项目IPProxyPool所提供的代理ip，每小时执行一次，刷新一次ip_proxy.txt文件

#请求500个ip，如果有这么多的话
#问题：这里我是本地的请求，服务器上是centos6.8，貌似有依赖包安装不上，这个需要后续解决
url = "http://127.0.0.1:8000/?types=0&count=500&country=%E5%9B%BD%E5%86%85"

res = requests.get(url).content
res_list = eval(res)

#得到list形式的结果，现在按照ip:port形式按行 写入到ip_proxy.txt中
with open("./ip_proxy.txt",'w') as f:
		for i in res_list:
				ip = "{ip}:{port}\n".format(ip=i[0],port=str(i[1]))
				f.write(ip)




