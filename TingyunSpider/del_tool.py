#!/usr/bin/env python
# -*- coding:utf-8 -*-  
import sys,os
import commands
if len(sys.argv) < 2:
		print "参数过少，请根据--help执行命令."
elif sys.argv[1].startswith('--'):
		option = sys.argv[1][2:]
		if option == "help":
				print "使用如下命令:"
				print "\t\t--all\t删除所有无关文件"
		elif option == "all":
				os.system("find ../ -name *.pyc | xargs rm -f")
				print "删除所有无关文件成功...."
		else:
				print "未知参数 ，请使用 --help 查看帮助."
else:
		print "参数不是以--开头，请重新输入."
