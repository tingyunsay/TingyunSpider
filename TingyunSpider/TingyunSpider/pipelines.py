# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import twisted
from scrapy import log
from scrapy.exceptions import DropItem
from pybloomfilter import BloomFilter
from scrapy.exceptions import CloseSpider
import re
import time
import os
import datetime
from twisted.enterprise import adbapi
import MySQLdb.cursors



class TingyunspiderPipeline(object):
	def __init__(self):
		self.Date = datetime.datetime.now().strftime("%Y%m")
		if not os.path.exists("{Date}/Concert".format(Date=self.Date)):
				os.makedirs("{Date}/Concert".format(Date=self.Date))
		if not os.path.exists("{Date}/Mv".format(Date=self.Date)):
				os.makedirs("{Date}/Mv".format(Date=self.Date))
		if not os.path.exists("{Date}/Artist".format(Date=self.Date)):
				os.makedirs("{Date}/Artist".format(Date=self.Date))
		if not os.path.exists("{Date}/Album".format(Date=self.Date)):
				os.makedirs("{Date}/Album".format(Date=self.Date))
		if not os.path.exists("{Date}/Music".format(Date=self.Date)):
				os.makedirs("{Date}/Music".format(Date=self.Date))
		if not os.path.exists("{Date}/Nettv".format(Date=self.Date)):
				os.makedirs("{Date}/Nettv".format(Date=self.Date))
		if not os.path.exists("{Date}/Nettv_Sp".format(Date=self.Date)):
				os.makedirs("{Date}/Nettv_Sp".format(Date=self.Date))
		if not os.path.exists("{Date}/Movie".format(Date=self.Date)):
				os.makedirs("{Date}/Movie".format(Date=self.Date))
		if not os.path.exists("{Date}/Tv".format(Date=self.Date)):
				os.makedirs("{Date}/Tv".format(Date=self.Date))
		if not os.path.exists("{Date}/TiebaWeibo".format(Date=self.Date)):
				os.makedirs("{Date}/TiebaWeibo".format(Date=self.Date))
		if not os.path.exists("{Date}/Piaofang".format(Date=self.Date)):
				os.makedirs("{Date}/Piaofang".format(Date=self.Date))
		if not os.path.exists("{Date}/Index".format(Date=self.Date)):
				os.makedirs("{Date}/Index".format(Date=self.Date))
		self.Concert = codecs.open('{Date}/Concert/all_Concert.json'.format(Date=self.Date),'a',encoding="utf-8")
		self.Mv = codecs.open('{Date}/Mv/all_Mv.json'.format(Date=self.Date),'a',encoding="utf-8")
		self.Artist = codecs.open('{Date}/Artist/all_Artist.json'.format(Date=self.Date),'a',encoding="utf-8")
		self.Album = codecs.open('{Date}/Album/all_Album.json'.format(Date=self.Date),'a',encoding="utf-8")
		self.Music = codecs.open('{Date}/Music/all_Music.json'.format(Date=self.Date),'a',encoding="utf-8")
		self.Nettv = codecs.open('{Date}/Nettv/all_Nettv.json'.format(Date=self.Date),'a',encoding="utf-8")
		self.Nettv_sp = codecs.open('{Date}/Nettv_Sp/all_Nettv_sp.json'.format(Date=self.Date),'a',encoding="utf-8")
		self.Movie = codecs.open('{Date}/Movie/all_Movie.json'.format(Date=self.Date),'a',encoding="utf-8")
		self.Tv = codecs.open('{Date}/Tv/all_Tv.json'.format(Date=self.Date),'a',encoding="utf-8")
		self.TiebaWeibo = codecs.open('{Date}/TiebaWeibo/all_TiebaWeibo.json'.format(Date=self.Date),'a',encoding="utf-8")
		self.Piaofang = codecs.open('{Date}/Piaofang/all_Piaofang.json'.format(Date=self.Date),'a',encoding="utf-8")
		self.Index = codecs.open('{Date}/Index/all_Index.json'.format(Date=self.Date),'a',encoding="utf-8")
		

	def process_item(self, item, spider):
		if re.search('concert$',''.join(item['site_name'])):
				line = json.dumps(dict(item),ensure_ascii=False)+"\n"
				self.Concert.write(line)
				return item
		if re.search('mv$',''.join(item['site_name'])):
				line = json.dumps(dict(item),ensure_ascii=False)+"\n"
				self.Mv.write(line)
				return item
		if re.search('artist$',''.join(item['site_name'])):
				line = json.dumps(dict(item),ensure_ascii=False)+"\n"
				self.Artist.write(line)
				return item
		if re.search('album$',''.join(item['site_name'])):
				line = json.dumps(dict(item),ensure_ascii=False)+"\n"
				self.Album.write(line)
				return item
		if re.search('music$',''.join(item['site_name'])):
				line = json.dumps(dict(item),ensure_ascii=False)+"\n"
				self.Music.write(line)
				return item
		if re.search('show$',''.join(item['site_name'])):
				line = json.dumps(dict(item),ensure_ascii=False)+"\n"
				self.Nettv.write(line)
				return item
		if re.search('sp$',''.join(item['site_name'])):
				line = json.dumps(dict(item),ensure_ascii=False)+"\n"
				self.Nettv_sp.write(line)
				return item
		if re.search('movie$',''.join(item['site_name'])):
				line = json.dumps(dict(item),ensure_ascii=False)+"\n"
				self.Movie.write(line)
				return item
		if re.search('tv$',''.join(item['site_name'])):
				line = json.dumps(dict(item),ensure_ascii=False)+"\n"
				self.Tv.write(line)
				return item
		if re.search('tieba$',''.join(item['site_name'])) or re.search('weibo$',''.join(item['site_name'])):
				line = json.dumps(dict(item),ensure_ascii=False)+"\n"
				self.TiebaWeibo.write(line)
				return item
		if re.search('piaofang$',''.join(item['site_name'])):
				line = json.dumps(dict(item),ensure_ascii=False)+"\n"
				self.Piaofang.write(line)
				return item
		if re.search('index$',''.join(item['site_name'])):
				line = json.dumps(dict(item),ensure_ascii=False)+"\n"
				self.Index.write(line)
				return item

		"""
class Count(object):
	def __init__(self):
		self.line = ""
		self.count = 0
		self.flag = 0

class TingyunspiderPipeline(object):
	def __init__(self):
		self.Date = datetime.datetime.now().strftime("%Y%m")
		self.Concert = Count()
		self.Mv = Count()
		self.Artist = Count()
		self.Album = Count()
		self.Music = Count()
		self.Nettv = Count()
		self.Nettv_sp = Count()
		self.Movie = Count()
		self.Tv = Count()
		self.Tieba = Count()
		self.Piaofang = Count()
		

	def process_item(self, item, spider):
		if re.search('tieba$',''.join(item['site_name'])):
				if self.Tieba.count < 20:
						self.Tieba.line += json.dumps(dict(item),ensure_ascii=False)+"\n"
						self.Tieba.count += 1
				else:
						if not os.path.exists("{Date}/TiebaWeibo".format(Date=self.Date)):
								os.makedirs("{Date}/TiebaWeibo".format(Date=self.Date))
						f = codecs.open('{Date}/TiebaWeibo/all_Tieba.json'.format(Date=self.Date),'a',encoding="utf-8")
						f.write(self.Tieba.line)
						f.close()
						self.Tieba.line = ""
						self.Tieba.count = 0
		if re.search('piaofang$',''.join(item['site_name'])):
				if self.Piaofang.count < 20:
						self.Piaofang.line += json.dumps(dict(item),ensure_ascii=False)+"\n"
						self.Piaofang.count += 1
				else:
						if not os.path.exists("{Date}/Piaofang".format(Date=self.Date)):
								os.makedirs("{Date}/Piaofang".format(Date=self.Date))
						f = codecs.open('{Date}/Piaofang/all_Piaofang.json'.format(Date=self.Date),'a',encoding="utf-8")
						f.write(self.Piaofang.line)
						f.close()
						self.Piaofang.line = ""
						self.Piaofang.count = 0
		if re.search('mv$',''.join(item['site_name'])):
				if self.Mv.count < 20:
						self.Mv.line += json.dumps(dict(item),ensure_ascii=False)+"\n"
						self.Mv.count += 1
				else:
						if not os.path.exists("{Date}/Mv".format(Date=self.Date)):
								os.makedirs("{Date}/Mv".format(Date=self.Date))
						f = codecs.open('{Date}/Mv/all_Mv.json'.format(Date=self.Date),'a',encoding="utf-8")
						f.write(self.Mv.line)
						f.close()
						self.Mv.line = ""
						self.Mv.count = 0
		if re.search('album$',''.join(item['site_name'])):
				if self.Album.count < 20:
						self.Album.line += json.dumps(dict(item),ensure_ascii=False)+"\n"
						self.Album.count += 1
				else:
						if not os.path.exists("{Date}/Album".format(Date=self.Date)):
								os.makedirs("{Date}/Album".format(Date=self.Date))
						f = codecs.open('{Date}/Album/all_Album.json'.format(Date=self.Date),'a',encoding="utf-8")
						f.write(self.Album.line)
						f.close()
						self.Album.line = ""
						self.Album.count = 0
		if re.search('concert$',''.join(item['site_name'])):
				if self.Concert.count < 20:
						self.Concert.line += json.dumps(dict(item),ensure_ascii=False)+"\n"
						self.Concert.count += 1
				else:
						if not os.path.exists("{Date}/Concert".format(Date=self.Date)):
								os.makedirs("{Date}/Concert".format(Date=self.Date))
						f = codecs.open('{Date}/Concert/all_Concert.json'.format(Date=self.Date),'a',encoding="utf-8")
						f.write(self.Concert.line)
						f.close()
						self.Concert.line = ""
						self.Concert.count = 0
		if re.search('movie$',''.join(item['site_name'])):
				if self.Movie.count < 20:
						self.Movie.line += json.dumps(dict(item),ensure_ascii=False)+"\n"
						self.Movie.count += 1
				else:
						if not os.path.exists("{Date}/Movie".format(Date=self.Date)):
								os.makedirs("{Date}/Movie".format(Date=self.Date))
						f = codecs.open('{Date}/Movie/all_Movie.json'.format(Date=self.Date),'a',encoding="utf-8")
						f.write(self.Movie.line)
						f.close()
						self.Movie.line = ""
						self.Movie.count = 0
		if re.search('tv$',''.join(item['site_name'])):
				if self.Tv.count < 20:
						self.Tv.line += json.dumps(dict(item),ensure_ascii=False)+"\n"
						self.Tv.count += 1
				else:
						if not os.path.exists("{Date}/Tv".format(Date=self.Date)):
								os.makedirs("{Date}/Tv".format(Date=self.Date))
						f = codecs.open('{Date}/Tv/all_Tv.json'.format(Date=self.Date),'a',encoding="utf-8")
						f.write(self.Tv.line)
						f.close()
						self.Tv.line = ""
						self.Tv.count = 0
		if re.search('sp$',''.join(item['site_name'])):
				if self.Nettv_sp.count < 20:
						self.Nettv_sp.line += json.dumps(dict(item),ensure_ascii=False)+"\n"
						self.Nettv_sp.count += 1
				else:
						if not os.path.exists("{Date}/Nettv_Sp".format(Date=self.Date)):
								os.makedirs("{Date}/Nettv_Sp".format(Date=self.Date))
						f = codecs.open('{Date}/Nettv_Sp/all_Nettv_sp.json'.format(Date=self.Date),'a',encoding="utf-8")
						f.write(self.Nettv_sp.line)
						f.close()
						self.Nettv_sp.line = ""
						self.Nettv_sp.count = 0
		if re.search('show$',''.join(item['site_name'])):
				if self.Nettv.count < 20:
						self.Nettv.line += json.dumps(dict(item),ensure_ascii=False)+"\n"
						self.Nettv.count += 1
				else:
						if not os.path.exists("{Date}/Nettv".format(Date=self.Date)):
								os.makedirs("{Date}/Nettv".format(Date=self.Date))
						f = codecs.open('{Date}/Nettv/all_Nettv.json'.format(Date=self.Date),'a',encoding="utf-8")
						f.write(self.Nettv.line)
						f.close()
						self.Nettv.line = ""
						self.Nettv.count = 0
		if re.search('artist$',''.join(item['site_name'])):
				if self.Artist.count < 20:
						self.Artist.line += json.dumps(dict(item),ensure_ascii=False)+"\n"
						self.Artist.count += 1
				else:
						if not os.path.exists("{Date}/Artist".format(Date=self.Date)):
								os.makedirs("{Date}/Artist".format(Date=self.Date))
						f = codecs.open('{Date}/Artist/all_Artist.json'.format(Date=self.Date),'a',encoding="utf-8")
						f.write(self.Artist.line)
						f.close()
						self.Artist.line = ""
						self.Artist.count = 0
		if re.search('music$',''.join(item['site_name'])):
				if self.Music.count < 20:
						self.Music.line += json.dumps(dict(item),ensure_ascii=False)+"\n"
						self.Music.count += 1
				else:
						if not os.path.exists("{Date}/Music".format(Date=self.Date)):
								os.makedirs("{Date}/Music".format(Date=self.Date))
						f = codecs.open('{Date}/Music/all_Music.json'.format(Date=self.Date),'a',encoding="utf-8")
						f.write(self.Music.line)
						f.close()
						self.Music.line = ""
						self.Music.count = 0
				f.close()
		"""



