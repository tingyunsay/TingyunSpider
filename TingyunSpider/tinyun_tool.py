#!/usr/bin/env python
# -*- coding:utf-8 -*-  
import sys,os
import re
import time
import subprocess
import commands
import datetime
if not os.path.exists('config.json'):
	print "Error,缺少config.json文件，请添加后重新运行程序，退出!"
	exit()

def is_runing(spider_name):
	a = commands.getoutput("ps -ef|grep %s|grep -v grep"%spider_name)
	return True if a else False	
def get_pid(exists):
	return re.search("\d+",exists).group() if exists else None
def kill_pid(pid):
	return True if not (os.system("kill -9 %s"%pid) if pid else 1) else False
	
	#return True if not os.system("kill -9 %s"%pid) else False

#声明一个全局的变量，存放所有可执行的爬虫
spider_name = []
#时间变量，确定log文件存放路径
Date = datetime.datetime.now().strftime("%Y%m")

with open('config.json','r') as f:
		res = f.read()
		if not res:
				print "Error:\n\tconfig.json文件为NULL，请编写配置文件!"
				exit()
		elif not isinstance(eval(res),dict):
				print "Error:\n\tconfig.json文件没有被正确配置，请重新编写配置文件!"
				exit()
		spider_name = eval(res).keys()

#删除全部spider
if len(sys.argv) < 2:
		print "参数过少，请根据 --help操作!"

elif sys.argv[1].startswith('--'):
		option = sys.argv[1][2:]
		if option == "help":
				print "输入如下格式:"
				print "\t\t--show\t\t显示当前可运行的spider"
				print "\t\t--spider +name\t\t运行指定spider"
				print "\t\t--spider_name\t\tkill指定spider"
				print "\t\t--version\t\t版本查询"
				print "\t\t--alive\t\t\t查询所有存活spider"
				print "\t\t--run_all\t\t运行全部spider"
				print "\t\t--killall\t\t杀死所有spider"
				print "\t\t--kill +name\t\t杀死指定name的spider"
		elif option == "run_all":
				spider_name = spider_name
				for spider in spider_name:
						if not re.search('2',spider):
								#用当天的日期来做日志文件名
								if not os.path.exists("{Date}/log".format(Date=Date)):
										os.makedirs("{Date}/log".format(Date=Date))
								command = "nohup scrapy crawl %s >> %s/log/Log_spider.%s.log 2>&1 &"%(spider,Date,(time.strftime("%Y-%m-%d",time.localtime())).replace(' ','-'))
								os.system(command)
								print "spider %s is runing ...."%spider if is_runing(spider) else "spider %s start fail ...."%spider
		elif option == "show":
				print "config文件中所有的spider有 ，共%s个:\n %s\t\t\t\n"%(len(spider_name),(' , '.join(spider_name)))
				running = []
				for spider in spider_name:
						exists = commands.getoutput("ps -ef|grep %s|grep -v grep"%spider)
						running.append(spider) if exists else ""
				print "其中处于running状态的有 ，共%s个:\n %s \t\t\t\n"%(len(running),(' , '.join(running)))
				stop = list(set(spider_name)^set(running))
				print "其中处于stop状态的有 ，共%s个:\n %s \t\t\t\n"%(len(stop),(' , '.join(stop)))
				
		elif option == "spider":
				try:
						spider = sys.argv[2]
				except Exception,e:
						print "请不要输入空的spider name , 退出."
						sys.exit()
				if spider in spider_name:
						if not os.path.exists("{Date}/log".format(Date=Date)):
								os.makedirs("{Date}/log".format(Date=Date))
						command = "nohup scrapy crawl %s >> %s/log/Log_spider.%s.log 2>&1 &"%(spider,Date,(time.strftime("%Y-%m-%d",time.localtime())).replace(' ','-'))
						os.system(command)
						print "正在寻找spider %s 是否启动，稍等......"%spider
						time.sleep(1)
						print "spider %s is runing ...."%spider if is_runing(spider) else "spider %s start fail ...."%spider
				else:
						print "请输入正确的spider name."		
		elif option == "version":
				print "version 1.0 tingyun"
		elif option == "alive":
				res = []
				for spider in spider_name:
						exists = commands.getoutput("ps -ef|grep %s|grep -v grep"%spider)
						res.append(spider) if exists else ""
				print "the total of live spider are %s , and every signal is :\n\t%s"%(len(res),(','.join(res))) if res else "no spider is alive..."				
		elif option == "killall":
				res = []
				for spider in spider_name:
						exists = commands.getoutput("ps -ef|grep %s|grep -v grep"%spider)
						if kill_pid(get_pid(exists)):
								res.append(spider)
				print "all killed %s spiders , and every signal is :\n\t\t%s"%(len(res),','.join(res)) if len(res) > 0 else "no spider is killed"
		elif option == "kill":
				try:
						name = sys.argv[2]
				except Exception,e:
						print "请不要输入空的spider name , 退出."
						sys.exit()
				exists = commands.getoutput("ps -ef|grep %s|grep -v grep"%name)
				if kill_pid(get_pid(exists)):
						print "kill spider %s success...."%exists
				else:
						print "spider %s not found !!!"%exists
else:
		print "未知参数，退出...."






