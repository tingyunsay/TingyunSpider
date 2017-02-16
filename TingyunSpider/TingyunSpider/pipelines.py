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
from twisted.enterprise import adbapi
import MySQLdb.cursors


class TingyunspiderPipeline(object):
	def __init__(self):
		self.file = codecs.open('current_data.json','wb',encoding="utf-8")
	def process_item(self, item, spider):
		line = json.dumps(dict(item),ensure_ascii=False)+"\n"
		self.file.write(line)

