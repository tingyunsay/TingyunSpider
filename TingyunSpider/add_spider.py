#!/usr/bin/env python
# -*- coding:utf-8 -*-  
import sys,os
import commands
import re

	
def f_exists_spider():
		res_str = commands.getoutput("grep \"name =\" TingyunSpider/spiders/*.py")
		res = re.findall('(?<=name =\')\w+',res_str)
		#remove函数返回None
		res.remove('template')
		return res

def f_config_spider():
		spider_name = ""
		with open('config.json','r') as f:
				res = f.read()
				if not res:
						print "Error:\n\tconfig.json文件为NULL，请编写配置文件!"
						exit()
				elif not isinstance(eval(res),dict):
						print "Error:\n\tconfig.json文件没有被正确配置，请重新编写配置文件!"
						exit()
				spider_name = eval(res).keys()
		return spider_name
#在config中配置好，但没有创建的spider
def f_ready_spider():
		if f_config_spider():
				if f_exists_spider():
						return set(f_config_spider()).difference(f_exists_spider())
				else:
						return f_config_spider()
		else:
				print "没有任何配置好的spider，无法创建spider."
				return []


def copy_spider(name):
		exists_spider = f_exists_spider()
		ready_spider = f_ready_spider()
		if exists_spider:
				if name in exists_spider:
						raise ValueError("spider %s已经存在，请输入一个新的spider name."%name)
						exit()
				elif name in ready_spider:
						f1 = open('./TingyunSpider/spiders/%s.py'%name,'r').read()
						f1 = re.sub('template',name,f1)
						with open('./TingyunSpider/spiders/%s.py'%name,'wb') as f:
								f.write(f1)
								f.close()
						if name in f_exists_spider():
								return True
						else:
								return False
		else:
				if ready_spider:
						if name in ready_spider:
								f1 = open('./TingyunSpider/spiders/%s.py'%name,'r').read()
								f1 = re.sub('template',name,f1)
								with open('./TingyunSpider/spiders/%s.py'%name,'wb') as f:
										f.write(f1)
										f.close()
								if name in f_exists_spider():
										return True
								else:
										return False
				else:
						print "没有可供创建的spider."
						return False

def drop_spider(name):
		if f_exists_spider():
				if name not in f_exists_spider():
						print "spider %s不存在，销毁失败."%name
						exit()
				else:
						os.system("rm -f ./TingyunSpider/spiders/%s.py"%name)
						if name not in f_exists_spider():
								print "销毁spider %s成功"%name
								return True
						else:
								print "销毁spider %s失败，请重新确认%s."%name
								return False
		else:
				print "系统当前没有任何存在的spider项目，销毁无效."
				return False

exists_spider = f_exists_spider()
config_spider = f_config_spider()
ready_spider = f_ready_spider()

if len(sys.argv) < 2:
		print "参数过少，请根据--help执行命令."
elif sys.argv[1].startswith('--'):
		option = sys.argv[1][2:]
		if option == "help":
				print "使用如下命令:"
				print "\t\t--show\t显示所有spider状态"
				print "\t\t--all\t根据配置新建所有还未创建的spider"
				print "\t\t--spider yourname\t创建名字为yourname的spider"
				print "\t\t--drop yourname\t销毁名字为yourname的spider"
				print "\t\t--dropall \t销毁所有spider"
		elif option == "show":
				print "已经配置的spider如下，共%d个:\n\t\t%s\n"%(len(config_spider),' , '.join(config_spider))
				print "创建成功的spider如下，共%d个:\n\t\t%s\n"%(len(exists_spider),' , '.join(exists_spider)) if exists_spider else "系统当前没有创建任何spider\n"
				print "有待创建的spider如下，共%s个:\n\t\t%s\n"%(len(ready_spider),' , '.join(ready_spider))
		elif option == "all":
				success = []
				for i in ready_spider:
						os.system("cp TingyunSpider/spiders/tingyun_spider.py TingyunSpider/spiders/%s.py"%i)
						if copy_spider(i):
								print "创建spider %s成功"%i
								success.append(i)
						else:
								print "Error , spider %s创建失败"%i
				
				print "创建如下spider成功,总共%d个:\n\t\t%s"%(len(success),' , '.join(success))
		elif option == "spider":
				try:
						spider = sys.argv[2]
				except Exception,e:
						print "请不要输入空的spider name ，退出."
						sys.exit()
				if spider in ready_spider:
						os.system("cp TingyunSpider/spiders/tingyun_spider.py TingyunSpider/spiders/%s.py"%spider)
						if copy_spider(spider):
								print "创建spider %s成功"%spider
						else:
								print "Error ， spider %s创建失败"%spider
				else:
						print "请输入正确的spider，退出~"
						sys.exit()
				
				#print "创建spider %s成功"%
		elif option == "drop":
				spider = sys.argv[2]
				drop_spider(spider)
		elif option == "dropall":
				try:
						check = sys.argv[2]
				except Exception,e:
						print "Warning : 请确认你是否要删除所有spider!!!"
						exit()
				if check == "-y":
						for i in exists_spider:
								drop_spider(i)
				else:
						print "Warning : 请确认你是否要删除所有spider!!!"
						exit()

		else:
				print "未知参数 ，请使用 --help 查看帮助."
else:
		print "参数不是以--开头，请重新输入."




