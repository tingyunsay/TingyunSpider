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
		if not os.path.exists("{Date}/Copyright".format(Date=self.Date)):
				os.makedirs("{Date}/Copyright".format(Date=self.Date))
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
		self.Copyright = codecs.open('{Date}/Copyright/all_Copyright.json'.format(Date=self.Date),'a',encoding="utf-8")
		

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
		if re.search('copyright$',''.join(item['site_name'])):
				line = json.dumps(dict(item),ensure_ascii=False)+"\n"
				self.Copyright.write(line)
				return item





