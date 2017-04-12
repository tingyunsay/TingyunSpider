#!coding=utf-8
import json
import base64
import requests
import time
import re
from get_verifycode import get_verifycode
import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import logging
from PIL import Image

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
	)
logger = logging.getLogger(__name__)
logging.getLogger("selenium").setLevel(logging.WARNING)

user_pool = []

with open('weibo_list/user.txt','r') as f:
		temp = f.read().split('\n')[:-1]
		for i in temp:
				user_pool.append({'username':re.sub(":.+","",i),'password':re.sub(".+:","",i)})
		f.close()

#获取单个账号的cookie
def getCookie(user,password):
	try:
		browser = webdriver.PhantomJS(desired_capabilities=dcap)
		browser.get("https://weibo.cn/login/")
		time.sleep(1)

		failure = 0
		while "微博" in browser.title.encode('utf-8') and failure < 5:
			failure += 1
			browser.save_screenshot("aa.png")
			username = browser.find_element_by_name("mobile")
			username.clear()
			username.send_keys(user)

			psd = browser.find_element_by_xpath('//input[@type="password"]')
			psd.clear()
			psd.send_keys(password)
			try:
				code = browser.find_element_by_name("code")
				code.clear()
				img = browser.find_element_by_xpath('//form[@method="post"]/div/img[@alt]')
				x = img.location["x"]
				y = img.location["y"]
				im = Image.open("aa.png")
				im.crop((int(x), int(y), 100 + int(x), int(y) + 22)).save("ab.png")
				code_txt = get_verifycode()
				time.sleep(1)
				code.send_keys(code_txt)
			except Exception, e:
				#print Exception,":1111",e
				pass

			commit = browser.find_element_by_name("submit")
			commit.click()
			time.sleep(3)
			if "我的首页" not in browser.title.encode('utf-8'):
				time.sleep(4)

		cookie = {}
		if "我的首页" in browser.title.encode('utf-8'):
			for elem in browser.get_cookies():
				cookie[elem["name"]] = elem["value"]
			logger.warning("Get Cookie Success!( Account:%s )" % user)
		return json.dumps(cookie)
	except Exception, e:
			#print Exception,":22222222",e
			logger.warning("Failed %s!" % user)
			return ""
	finally:
			try:
				browser.quit()
			except Exception,e:
				#print Exception,":333333",e
				pass

cookies = []
map(lambda x:cookies.append(getCookie(x['username'],x['password'])) , user_pool)

cookies = filter((lambda x:x is not ""),cookies)

"""
#老版本获取cookies
def getCookie(my_user_pool):
	cookies = []
	login_Url = r"https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)"
	for user in my_user_pool:
		name = user["username"]
		password = user["password"]
		username = base64.b64encode(name.encode('utf-8')).decode('utf-8')
		postData = {
				"entry": "sso",
				"gateway": "1",	
				"from": "null",
				"savestate": "30",
				"useticket": "0",
				"pagerefer": "",
				"vsnf": "1",
				"su": username,
				"sp": password,
				"service": "sso",
				"sr": "1440*900",
				"encoding": "UTF-8",
				"cdult": "3",
				"domain": "sina.com.cn",
				"prelt": "0",
				"returntype": "TEXT"
				}
	
		session = requests.Session()
		try:
			res = session.post(login_Url,data = postData)
			return_str = res.content.decode('gbk')
			info = json.loads(return_str)
			if info['retcode'] == "0":
				#print "Get a Cookie Success!!!(By phoneNum = %s)" % name
				cookie = session.cookies.get_dict()
				cookies.append(json.dumps(cookie))
			else:
				print "ERROR , not get cookie , the Reason is %s" % info['reason']
				#print >> log,"At time %s , failed to get cookie , Reault = %s" % (time.ctime,info['reason'])
		except Exception,e:
			print "%s , ",Exception,":",e
	return cookies

cookies = getCookie(user_pool)
"""
