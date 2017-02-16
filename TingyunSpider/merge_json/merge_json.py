#!/usr/bin/env python
# -*- coding:utf-8 -*-  
import sys,os
import json
import commands
import re

if os.path.exists('all_data.json'):
		print "Error,all_data.json文件已存在，请确定要合并的文件是否正确，并在删除all_data.json后重新运行程序!"
		exit()


all_json_name = []
if not commands.getoutput('ls *.json'):
		all_json_name = map(lambda x:x.replace('.',''),re.findall('.+\.',commands.getoutput('ls *.json')))
else:
		print "Error,请确认当前目录下有能被合并的json文件，合并失败!"
		exit()


with open('all_mv.json','w') as f:
		for name in all_json_name:
					a = open("%s.json"%name,'r')
					f.write(a.read())




