#!coding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import scrapy
#from scrapy_redis.spiders import RedisSpider
from scrapy.loader import ItemLoader
from scrapy.http import Request
from TingyunSpider.items import TingyunspiderItem
import requests
import bs4
from scrapy.loader.processors import MapCompose
from bs4 import BeautifulSoup
import lxml
import re
from urllib2 import URLError
import json
import time
import signal
from pybloomfilter import BloomFilter
import os
from scrapy.exceptions import CloseSpider
from urllib import quote_plus
import datetime
from scrapy.item import Item,Field
import hashlib
from TingyunSpider.path_translate import Relative_to_Absolute,Relative_to_Absolute2,Get_Valid_Url,get_HeadUrl,Check_Url_Valid
from TingyunSpider.total_page_circulate import Total_page_circulate,Turn_True_Page,Total_Page_Byyourself


class TingyunSpider(scrapy.Spider):
	name ='xiami_album'
	allowed_domain = []
		
	def __init__(self,*args,**kwargs):
		super(TingyunSpider,self).__init__(*args,**kwargs)
		self.now = time.time()
		self.config = []
		self.Index_Url = ""
			
	
	def start_requests(self):
		with open('config.json','r') as f:
			data = json.load(f)
			for i in data.iteritems():
				if i[0].encode('utf-8') == self.name:
					self.config.append(i)
			f.close()
		
		for v in self.config:
			#self.Splash作为全局变量，控制final页是否渲染
			if len(v[1]) == 2:
				self.Splash = v[1][0]['Splash']
				self.Index_Url = v[1][0]['Index_Url']
				Segement = v[1][0]['Segement']
				Final_Xpath = v[1][1]['Final_Xpath']
				#有json这个字段，说明为json页
				if  Index_Url.has_key('json'):
						for url in self.Index_Url['url']:
								request = Request(url,self.parse_json)
								request.meta['Index_Url'] = url
								request.meta['Segement'] = Segement
								request.meta['Final_Xpath'] = Final_Xpath
								yield request
				else:
						#默认是不指定splash，即不渲染，走else；只要加上了splash这个key，就表示需要渲染。每一层会有这样的规则
						if self.Index_Url['url'].has_key('splash'):
								for url in self.Index_Url['url']:
										request = Request(url,self.parse_splash,meta={
												'splash':{
												'endpoint':'render.html',
												'args':{
														'wait':0.5,
														'images':0,
														'render_all':1
														}
												}
										})				
										request.meta['Index_Url'] = url
										request.meta['Segement'] = Segement
										request.meta['Final_Xpath'] = Final_Xpath
										yield request
						else:
								for url in  self.Index_Url['url']:
										request = Request(url,self.parse_splash)				
										request.meta['Index_Url'] = url
										request.meta['Segement'] = Segement
										request.meta['Final_Xpath'] = Final_Xpath
										yield request
								
			
			if len(v[1]) == 3:
				self.Splash = v[1][0]['Splash']
				self.Index_Url = v[1][0]['Index_Url']
				Is_Json = v[1][0]['Is_Json']
				Segement = v[1][0]['Segement']
				First = v[1][1]['First']
				Final_Xpath = v[1][2]['Final_Xpath']
				if Is_Json == 1:
						for url in self.Index_Url['url']:
								request = Request(url,self.parse_json)
								request.meta['Index_Url'] = url
								request.meta['Segement'] = Segement
								request.meta['First'] = First
								request.meta['Final_Xpath'] = Final_Xpath
								yield request
				else:
						if self.Index_Url['url'].has_key('splash'):
								for url in  self.Index_Url['url']:
										request = Request(url,self.parse_splash,meta={
												'splash':{
												'endpoint':'render.html',
												'args':{
														'wait':0.5,
														'images':0,
														'render_all':1
														}
												}
										})				
										request.meta['Index_Url'] = url
										request.meta['Segement'] = Segement
										request.meta['First'] = First
										request.meta['Final_Xpath'] = Final_Xpath
										yield request
						else:
								for url in  self.Index_Url['url']:
										request = Request(url,self.parse_splash)
										request.meta['Index_Url'] = url
										request.meta['Segement'] = Segement
										request.meta['First'] = First
										request.meta['Final_Xpath'] = Final_Xpath
										yield request	
				
			if len(v[1]) == 4:
				self.Splash = v[1][0]['Splash']
				self.Index_Url = v[1][0]['Index_Url']
				Segement = v[1][0]['Segement']
				First = v[1][1]['First']
				Second = v[1][2]['Second']
				Final_Xpath = v[1][3]['Final_Xpath']
				if self.Index_Url.has_key('json'):
						for url in self.Index_Url['url']:
								request = Request(url,callback = self.parse_json)
								request.meta['Index_Url'] = url
								request.meta['Segement'] = Segement
								request.meta['First'] = First
								request.meta['Second'] = Second
								request.meta['Final_Xpath'] = Final_Xpath
								yield request
				else:
						if self.Index_Url.has_key('splash'):
								for url in self.Index_Url['url']:
										request = Request(url,callback = self.parse_zero,dont_filter=True,meta={
													'splash':{
															'endpoint':'render.html',
															'args':{
																	'wait':0.5,
																	'images':0,
																	'render_all':1
																}
															}
														})
										request.meta['Index_Url'] = url
										request.meta['Segement'] = Segement
										request.meta['First'] = First
										request.meta['Second'] = Second
										request.meta['Final_Xpath'] = Final_Xpath
										yield request
						else:
								for url in self.Index_Url['url']:
										request = Request(url,callback = self.parse_zero,dont_filter=True)
										request.meta['Index_Url'] = url
										request.meta['Segement'] = Segement
										request.meta['First'] = First
										request.meta['Second'] = Second
										request.meta['Final_Xpath'] = Final_Xpath
										yield request

			if len(v[1]) == 5:
				self.Splash = v[1][0]['Splash']
				self.Index_Url = v[1][0]['Index_Url']
				Segement = v[1][0]['Segement']
				First = v[1][1]['First']
				Second = v[1][2]['Second']
				Third = v[1][3]['Third']
				Final_Xpath = v[1][4]['Final_Xpath']
				if self.Index_Url.has_key('json'):
						for url in self.Index_Url['url']:
								request = Request(url,callback = self.parse_json)
								request.meta['Index_Url'] = url
								request.meta['Segement'] = Segement
								request.meta['First'] = First
								request.meta['Second'] = Second
								request.meta['Third'] = Third
								request.meta['Final_Xpath'] = Final_Xpath
								yield request
				else:
						if self.Index_Url.has_key('splash'):
								for url in self.Index_Url['url']:
										request = Request(url,callback = self.parse_zero,meta={
													'splash':{
															'endpoint':'render.html',
															'args':{
																	'wait':0.5,
																	'images':0,
																	'render_all':1
																}
															}
														})
										request.meta['Index_Url'] = url
										request.meta['Segement'] = Segement
										request.meta['First'] = First
										request.meta['Second'] = Second
										request.meta['Third'] = Third
										request.meta['Final_Xpath'] = Final_Xpath
										yield request
						else:
								for url in self.Index_Url['url']:
										request = Request(url,callback = self.parse_zero)
										request.meta['Index_Url'] = url
										request.meta['Segement'] = Segement
										request.meta['First'] = First
										request.meta['Second'] = Second
										request.meta['Third'] = Third
										request.meta['Final_Xpath'] = Final_Xpath
										yield request
	
	def parse_zero(self,response):
		#这个是真正处理第一级页面的函数，上面只不过是一个分类，每个层级需要传递的参数确定，再分别传输
		#规定：接受Segement参数，或者xpath参数，前者表示会分页，并将分页得到的link提交到绑定函数处理，再传递给正常的下一层
		Index_Url = response.meta.get('Index_Url',None)
		Segement = response.meta.get('Segement',None)
		First = response.meta.get('First',None)
		Second = response.meta.get('Second',None)
		Third = response.meta.get('Third',None)
		Final_Xpath = response.meta.get('Final_Xpath',None)
		max_pages = 2
		urls = ""

		if Segement.has_key('Max_Page'):
				if not Segement['Max_Page'].has_key('json'):
						try:
								max_pages = re.search(Segement['Max_Page']['re'],''.join(response.xpath(Segement['Max_Page']['xpath']).extract())).group()
						except Exception,e:
								print Exception,":",e
						if isinstance(max_pages,unicode):
								max_pages = max_pages.encode('utf-8')
						if isinstance(max_pages,int) or isinstance(max_pages,str):
								max_pages = Total_page_circulate(self.name,int(max_pages))
						#如果该站点压根没有告诉你有多少页面，那就只能手动给出一个值了，如下函数
						elif max_pages == '':
								max_pages = Total_Page_Byyourself(self.name)	
						else:
								raise CloseSpider("in the splashing,can not find the Max_page in Segement ,please check ,spider closed!!!")
						urls = get_HeadUrl(Index_Url,self.name)
				#存在json即用json的方式去解读
				else:
						res_json = json.loads(response.body_as_unicode())
						depth = 0
						if isinstance(Segement['Max_Page']['index'],list):
								try:
									while depth < len(Segement['Max_Page']['index']):
										res_json = res_json.get(Segement['Max_Page']['index'][depth])
										depth += 1
								except Exception,e:
									print Exception,":",e 
								max_pages = Total_page_circulate(self.name,int(res_json))
						elif isinstance(Segement['Max_Page']['index'],int):
								max_pages = Total_Page_Byyourself(self.name)
						else:
								raise CloseSpider("json页面中，找不到Max_Page ，请重新确认 ，爬虫关闭!!!")
						#这个就不变了，但是下层的页面要是再分页的话，就能使用类似的如get_HeadUrl2，get_HeadUrl3....
						urls = get_HeadUrl(Index_Url,self.name)	
				print "最大页数是:%d"%max_pages
				#分了页，之后，就是绑定分页处理函数.这里是segement_zero:又分成是否需要渲染
				if Segement['Max_Page'].has_key('splash'):
						begin = 1
						try:
								begin = re.search('\d+$',Index_Url).group()
						except Exception,e:
								print Exception,":",e
								raise CloseSpider("can not find the start page number,please check,spider closed!!!")
						for i in range(int(begin),max_pages+1):
								i = Turn_True_Page(i,self.name)
								url = urls.format(page=str(i))
								if Check_Url_Valid(url):
										request = Request(url,callback = self.segement_zero,dont_filter=True,meta={
																	'splash':{
																	'endpoint':'render.html',
																	'args':{
																			'wait':0.5,
																			'images':0,
																			'render_all':1
																			}
																		}
																	})
										request.meta['segement'] = Segement['Max_Page']['segement']
										request.meta['Final_Xpath'] = Final_Xpath
										yield request
								else:
										continue
				else:
						begin = 1
						try:
								begin = re.search('\d+$',Index_Url).group()
						except Exception,e:
								print Exception,":",e
								raise CloseSpider("can not find the start page number,please check,spider closed!!!")
						for i in range(int(begin),max_pages+1):
								i = Turn_True_Page(i,self.name)
								url = urls.format(page=str(i))
								if Check_Url_Valid(url):
										request = Request(url,callback = self.segement_zero,dont_filter=True)
										request.meta['segement'] = Segement['Max_Page']['segement']
										request.meta['Final_Xpath'] = Final_Xpath
										yield request
								else:
										continue

		else:
				detail_url = []
				if not Segement.has_key('json'):
						for xpath in Segement['xpath']:
								for url in Relative_to_Absolute(Index_Url,response.xpath(xpath).extract(),self.name):
										detail_url.append(url)
				else:
						res_json = json.loads(response.body_as_unicode())
						#递归读取最底层的key对应的value值，我去，想出来了～～[这里是要for一遍最底层的list，所以要读到len-1处，然后在得到detail_url]
						depth = 0
						length = len(Segement['index'])
						while depth < length - 1:
							res_json = res_json.get(All_Detail_Page['index'][depth])
							depth += 1
							#print "now the res_json is %s"%res_json
						for i in res_json:
							detail_url.append(i.get(All_Detail_Page['index'][length-1]))
						try:
							detail_url = Relative_to_Absolute2(Index_Url,detail_url,self.name)
							#detail_url = Relative_to_Absolute(Index_Url,detail_url,self.name)
						except Exception,e:
							print Exception,":",e
				if First is None:
						if self.Splash:
								for url in detail_url:
										if Check_Url_Valid(url):
												request = Request(url,callback = self.parse_final,dont_filter=True,meta={
																	'splash':{
																	'endpoint':'render.html',
																	'args':{
																			'wait':0.5,
																			'images':0,
																			'render_all':1
																			}
																		}
																	})
												request.meta['Final_Xpath'] = Final_Xpath
												yield request
										else:
												continue
						else:
								for url in detail_url:
										if Check_Url_Valid(url):
												request = Request(url,callback = self.parse_final,dont_filter=True)
												request.meta['Final_Xpath'] = Final_Xpath
												yield request
										else:
												continue
				else:
						for url in detail_url:
								if Check_Url_Valid(url):
										request = Request(url,callback = self.parse_first)
										request.meta['Index_Url'] = Index_Url
										request.meta['Signal_Detail_Page'] = Signal_Detail_Page
										request.meta['Target_Detail_Page'] = Target_Detail_Page
										request.meta['Final_Xpath'] = Final_Xpath
										yield request
								else:
										continue
								
						


	def parse_first(self,response):
		Index_Url = response.meta.get('Index_Url',None)
		First = response.meta.get('First',None)
		Second = response.meta.get('Second',None)
		Third = response.meta.get('Third',None)
		Final_Xpath = response.meta.get('Final_Xpath',None)
		Some_Info = {}
		if 'Some_Info' in First.keys():
				keys = First['Some_Info'].keys()
				for key in keys:
						try:
								Some_Info[key] = response.xpath(First['Some_Info'][key]).extract()[0]
						except Exception,e:
								print Exception,":",e
		#一个页面可能会需要多个提取的xpath，这里就指定为一个list了
		detail_url = []
		
		for xpath in First['xpath']:
				for url in Relative_to_Absolute(Index_Url,response.xpath(xpath).extract(),self.name):
						detail_url.append(url)
		#在考虑在每一层加一个判断，相当于如果没有（第一个）要传递给下一层的数据，就直接传递给final_parse（注：在传递给final_parse时需要判断是否需要渲染，这里我暂时先默认都渲染，但是之后可以考虑在config.json的Final_Xpath加一个flag，1表示需要渲染，0表示不需要）
		if Second is None:
				if self.Splash:
						for url in detail_url:
								if Check_Url_Valid(url):
										request = Request(url,callback = self.parse_final,dont_filter=True,meta={
															'splash':{
															'endpoint':'render.html',
															'args':{
																	#只有aiyiyi需要load 10s，才能拿到播放量
																	'wait':0.5,
																	'images':0,
																	'render_all':1
																	}
																}
															})
										request.meta['Some_Info'] = Some_Info
										request.meta['Final_Xpath'] = Final_Xpath
										yield request
								else:
										continue
				else:
						for url in detail_url:
								if Check_Url_Valid(url):
										request = Request(url,callback = self.parse_final,dont_filter=True)
										request.meta['Some_Info'] = Some_Info
										request.meta['Final_Xpath'] = Final_Xpath
										yield request
								else:
										continue
		else:
				if Second.has_key('splash'):
						for url in detail_url:
								if Check_Url_Valid(url):
										#增加一个可有可无的splash参数，存在就渲染，不存在就默认走静态
										request = Request(url,callback = self.parse_second,dont_filter=True,meta={
															'splash':{
															'endpoint':'render.html',
															'args':{
																	'wait':0.5,
																	'images':0,
																	'render_all':1
																	}
																}
															})
										#我没想到起始页有不是www.xxxx.com/xxx/xxx这种开头的，这个芒果台是list.mangguo.com/.... 这里我不能用这个url头部来构造下一层url，所以我把当前页面的url头部作为新的Index_Url传递下去
										request.meta['Index_Url'] = url
										request.meta['Second'] = Second
										request.meta['Third'] = Third
										request.meta['Final_Xpath'] = Final_Xpath
										yield request
								else:
										continue
				else:
						for url in detail_url:
								if Check_Url_Valid(url):
										request = Request(url,callback = self.parse_second,dont_filter=True)
										request.meta['Index_Url'] = url
										request.meta['Second'] = Second
										request.meta['Third'] = Third
										request.meta['Final_Xpath'] = Final_Xpath
										yield request
								else:
										continue
	
	def parse_second(self,response):
		Index_Url = response.meta.get('Index_Url',None)
		Second = response.meta.get('Second',None)
		Third = response.meta.get('Third',None)
		Final_Xpath = response.meta.get('Final_Xpath',None)
		Some_Info = {}
		if 'Some_Info' in Second.keys():
				keys = Second['Some_Info'].keys()
				for key in keys:
						try:
								Some_Info[key] = response.xpath(Second['Some_Info'][key]).extract()[0]
						except Exception,e:
								print Exception,":",e
		detail_url = Relative_to_Absolute(Index_Url,response.xpath(Second['xpath']).extract(),self.name)
		if Third is None:
				if self.Splash:
						for url in detail_url:
								if Check_Url_Valid(url):
										request = Request(url,callback = self.parse_final,dont_filter=True,meta={
																'splash':{
																'endpoint':'render.html',
																'args':{
																		'wait':0.5,
																		'images':0,
																		'render_all':1
																		}
																	}
																})
										request.meta['Some_Info'] = Some_Info
										request.meta['Final_Xpath'] = Final_Xpath
										yield request
								else:
										continue
				else:
						for url in detail_url:
								if Check_Url_Valid(url):
										print url,"$$$$$$$$$$"
										request = Request(url,callback = self.parse_final,dont_filter=True)
										request.meta['Some_Info'] = Some_Info
										request.meta['Final_Xpath'] = Final_Xpath
										yield request
								else:
										#非法的url，直接continue，省略
										continue
		else:
				for url in detail_url:
						if Check_Url_Valid(url):
								request = Request(url,callback = self.parse_third,dont_filter=True)
								request.meta['Index_Url'] = Index_Url
								request.meta['Third'] = Third
								request.meta['Final_Xpath'] = Final_Xpath
								yield request
						else:
								continue
		

	def parse_third(self,response):
		Index_Url = response.meta['Index_Url']
		Third = response.meta.get('Third',None)
		Final_Xpath = response.meta.get('Final_Xpath',None)
		detail_url = Relative_to_Absolute(Index_Url,response.xpath(Third['xpath']).extract(),self.name)	
		Some_Info = {}
		if 'Some_Info' in Third.keys():
				keys = Third['Some_Info'].keys()
				for key in keys:
						try:
								Some_Info[key] = response.xpath(Third['Some_Info'][key]).extract()[0]
						except Exception,e:
								print Exception,":",e
		if self.Splash:
				for url in detail_url:
						if Check_Url_Valid(url):
								request = scrapy.Request(url,callback = self.parse_final,dont_filter=True,meta = {
														'splash':{
														'endpoint':'render.html',
														'args':{
																'wait':0.5,
																'images':0,
																'render_all':1
																}
															}
														})				
								request.meta['Some_Info'] = Some_Info
								request.meta['Final_Xpath'] = Final_Xpath
								yield request
						else:
								continue
		else:
				for url in detail_url:
						if Check_Url_Valid(url):
								request = scrapy.Request(url,callback = self.parse_final,dont_filter=True)
								request.meta['Some_Info'] = Some_Info
								request.meta['Final_Xpath'] = Final_Xpath
								yield request
						else:
								continue
	#现在修改逻辑是：每一层绑定一个segement函数，在存在segement字段的时候，需要交给这个segement函数处理。
	#第一层一般都需要分页，我们加上segement这个字段，并且后面的命名规则定为：segement_zero,segement_first,segement_second,segement_third......
	def segement_zero(self,response):
		#这边就是管你有没有，我都接收，在使用的时候判断，如果不存在，说明要直接到final_parse处
		Index_Url = response.meta.get('Index_Url',None)
		segement = response.meta.get('segement',None)
		First = response.meta.get('First',None)
		Second = response.meta.get('Second',None)
		Third = response.meta.get('Third',None)
		Final_Xpath = response.meta.get('Final_Xpath',None)
		detail_url = []
		if segement.has_key('json'):
				res_json = json.loads(response.body_as_unicode())
				#递归读取最底层的key对应的value值，我去，想出来了～～[这里是要for一遍最底层的list，所以要读到len-1处，然后在得到detail_url]
				depth = 0
				length = len(segement['index'])
				while depth < length - 1:
						res_json = res_json.get(segement['index'][depth])
						depth += 1
				#print "now the res_json is %s"%res_json
				for i in res_json:
						detail_url.append(i.get(segement['index'][length-1]))
				try:
						detail_url = Relative_to_Absolute2(Index_Url,detail_url,self.name)
						#detail_url = Relative_to_Absolute(Index_Url,detail_url,self.name)
				except Exception,e:
						print Exception,":",e
		else:
				for xpath in segement['xpath']:
						for url in Relative_to_Absolute(Index_Url,response.xpath(xpath).extract(),self.name):
								detail_url.append(url)
		if First is None:
				if self.Splash:
						for url in detail_url:
								if Check_Url_Valid(url):
										request = Request(url,callback = self.parse_final,dont_filter=True,meta={
															'splash':{
															'endpoint':'render.html',
															'args':{
																	#只有aiyiyi需要load 10s，才能拿到播放量
																	'wait':0.5,
																	'images':0,
																	'render_all':1
																	}
																}
															})
										request.meta['Some_Info'] = Some_Info
										request.meta['Final_Xpath'] = Final_Xpath
										yield request
								else:
										continue
				else:
						for url in detail_url:
								if Check_Url_Valid(url):
										request = Request(url,callback = self.parse_final,dont_filter=True)
										request.meta['Some_Info'] = Some_Info
										request.meta['Final_Xpath'] = Final_Xpath
										yield request
								else:
										continue
		else:
				if First.has_key('splash'):
						for url in detail_url:
								if Check_Url_Valid(url):
										#增加一个可有可无的splash参数，存在就渲染，不存在就默认走静态
										request = Request(url,callback = self.parse_second,dont_filter=True,meta={
															'splash':{
															'endpoint':'render.html',
															'args':{
																	'wait':0.5,
																	'images':0,
																	'render_all':1
																	}
																}
															})
										#我没想到起始页有不是www.xxxx.com/xxx/xxx这种开头的，这个芒果台是list.mangguo.com/.... 这里我不能用这个url头部来构造下一层url，所以我把当前页面的url头部作为新的Index_Url传递下去
										request.meta['Index_Url'] = url
										request.meta['Signal_Detail_Page'] = Signal_Detail_Page
										request.meta['Target_Detail_Page'] = Target_Detail_Page
										request.meta['Final_Xpath'] = Final_Xpath
										yield request
								else:
										continue
				else:
						for url in detail_url:
								if Check_Url_Valid(url):
										request = Request(url,callback = self.parse_second,dont_filter=True)
										request.meta['Index_Url'] = url
										request.meta['Signal_Detail_Page'] = Signal_Detail_Page
										request.meta['Target_Detail_Page'] = Target_Detail_Page
										request.meta['Final_Xpath'] = Final_Xpath
										yield request
								else:
										continue		

		
	def parse_json(self,response):
		Index_Url = response.meta.get('Index_Url',None)
		Segement = response.meta.get('Segement',None)
		First = response.meta.get('First',None)
		Second = response.meta.get('Second',None)
		Third = response.meta.get('Third',None)
		Final_Xpath = response.meta.get('Final_Xpath',None)
		res_json = json.loads(response.body_as_unicode())
		
		depth = 0
		if isinstance(Segement['index'],list):
				try:
						while depth < len(Segement['index']):
								res_json = res_json.get(Segement['index'][depth])
								depth += 1
				except Exception,e:
						print Exception,":",e 
				max_pages = Total_page_circulate(self.name,int(res_json))
		elif isinstance(Segement['index'],int):
				max_pages = Total_Page_Byyourself(self.name)
		else:
				raise CloseSpider("json页面中，找不到Segement ，请重新确认 ，爬虫关闭!!!")

		
		#这个就不变了，但是下层的页面要是再分页的话，就能使用类似的如get_HeadUrl2，get_HeadUrl3....
		urls = get_HeadUrl(Index_Url,self.name)	
		print "最大页数是:%d"%max_pages
		if First is None:
				if self.Splash:
						begin = 1
						try:
								begin = re.search('\d+$',Index_Url).group()
						except Exception,e:
								print Exception,":",e
								raise CloseSpider("can not find the start page number,please check,spider closed!!!")
						for i in range(int(begin),max_pages+1):
								i = Turn_True_Page(i,self.name)
								url = urls.format(page=str(i))
								if Check_Url_Valid(url):
										request = Request(url,callback = self.parse_final,dont_filter=True,meta={
															'splash':{
															'endpoint':'render.html',
															'args':{
																	'wait':0.5,
																	'images':0,
																	'render_all':1
																	}
																}
															})
										request.meta['Final_Xpath'] = Final_Xpath
										yield request
								else:
										continue
				else:
						begin = 1
						try:
								begin = re.search('\d+$',Index_Url).group()
						except Exception,e:
								print Exception,":",e
								raise CloseSpider("can not find the start page number,please check,spider closed!!!")
						for i in range(int(begin),max_pages+1):
								i = Turn_True_Page(i,self.name)
								url = urls.format(page=str(i))
								if Check_Url_Valid(url):
										request = Request(url,callback = self.parse_final,dont_filter=True)
										request.meta['Final_Xpath'] = Final_Xpath
										yield request
								else:
										continue
		else:
				begin = 1
				try:
						begin = re.search('\d+$',Index_Url).group()
				except Exception,e:
						print Exception,":",e
						raise CloseSpider("can not find the start page number,please check,spider closed!!!")
				for i in range(int(begin),int(max_pages)+1):
						try:
								i = Turn_True_Page(i,self.name)
								url = urls.format(page=str(i))
						except Exception,e:
								print Exception,":",e
						if Check_Url_Valid(url):
								request = Request(url,callback = self.parse_json2,dont_filter=True)
								request.meta['Index_Url'] = Index_Url
								request.meta['First'] = First
								request.meta['Second'] = Second
								request.meta['Third'] = Third
								request.meta['Final_Xpath'] = Final_Xpath
								yield request
						else:
								continue
		
	def parse_json2(self,response):
		Index_Url = response.meta.get('Index_Url',None)
		First = response.meta.get('First',None)
		Second = response.meta.get('Second',None)
		Third = response.meta.get('Third',None)
		Final_Xpath = response.meta.get('Final_Xpath',None)
		detail_url = []
		res_json = json.loads(response.body_as_unicode())
		#递归读取最底层的key对应的value值，我去，想出来了～～[这里是要for一遍最底层的list，所以要读到len-1处，然后在得到detail_url]
		depth = 0
		length = len(First['index'])
		while depth < length - 1:
				res_json = res_json.get(First['index'][depth])
				depth += 1
		#print "now the res_json is %s"%res_json
		for i in res_json:
				detail_url.append(i.get(First['index'][length-1]))
		try:
				detail_url = Relative_to_Absolute2(Index_Url,detail_url,self.name)
				#detail_url = Relative_to_Absolute(Index_Url,detail_url,self.name)
		except Exception,e:
				print Exception,":",e
		
		if Second is None:
				if self.Splash:
						for url in detail_url:
								if Check_Url_Valid(url):
										request = Request(url,callback = self.parse_final,dont_filter=True,meta={
															'splash':{
															'endpoint':'render.html',
															'args':{
																	'wait':0.5,
																	'images':0,
																	'render_all':1
																	}
																}
															})
										request.meta['Final_Xpath'] = Final_Xpath
										yield request
								else:
										continue
				else:
						for url in detail_url:
								if Check_Url_Valid(url):
										request = Request(url,callback = self.parse_final,dont_filter=True)
										request.meta['Final_Xpath'] = Final_Xpath
										yield request
								else:
										continue
		else:
				for url in detail_url:
						if Check_Url_Valid(url):
								request = Request(url,callback = self.parse_second)
								request.meta['Index_Url'] = Index_Url
								request.meta['Second'] = Second
								request.meta['Third'] = Third
								request.meta['Final_Xpath'] = Final_Xpath
								yield request
						else:
								continue
			
	


	def parse_final(self,response):
		#我去，这个Final_Xpath竟然只会传递一次......你要是动了这个Final_Xpath，那就无法修改回来了
		Final_Xpath = response.meta.get('Final_Xpath',None)
		Some_Info = response.meta.get('Some_Info',None)
		
		if 'All_Xpath' not in Final_Xpath.keys():
				item = TingyunspiderItem()
				l = ItemLoader(item=item, response=response)
				for key in Final_Xpath.keys():
						item.fields[key] = Field()
						try:
								#itemloader在add_xxx方法找不到值的时候，会自动忽略这个字段，可是我不想忽略它，这时候需要将其置为空("")
								if map(lambda x:1 if x else 0, map(lambda x:response.xpath(x).extract() if x != "/" else "",Final_Xpath[key])) in [[0,0],[0]] and key != "site_name":		
										map(lambda x:l.add_value(key , ""),["just_one"])
								elif key == "site_name":
										map(lambda x:l.add_value(key , x),Final_Xpath[key])
								else:
										map(lambda x:l.add_xpath(key , x) if response.xpath(x).extract() != [] else "",Final_Xpath[key])
						except Exception,e:
								print Exception,":",e
				if Some_Info:
						for key in Some_Info.keys():
								item.fields[key] = Field()
								l.add_value(key , Some_Info[key])
				yield l.load_item()
		else:
		#感觉这里不能用itemloader的add_xxx方法了，因为要先找到一个页面所有的含有目标item的块，再在每个块里面提取出单个item，itemloader的话是一次性直接全取出，add_xpath不能再细分了;;打算用add_value方法
				my_Final_Xpath = Final_Xpath.copy()
				All_Xpath = my_Final_Xpath['All_Xpath'].copy()
				del my_Final_Xpath['All_Xpath']
				all_xpath = All_Xpath['all_xpath']
				del All_Xpath['all_xpath']
				for i in response.xpath(all_xpath[0]):
						item = TingyunspiderItem()
						l = ItemLoader(item=item, response=response)
						#把All_Xpath中的数据提取出来
						for key in All_Xpath.keys():
								item.fields[key] = Field()
								try:
										#itemloader在add_xxx方法找不到值的时候，会自动忽略这个字段，可是我不想忽略它，这时候需要将其置为空("")
										if map(lambda x:1 if x else 0, map(lambda x:response.xpath(x).extract() if x != "/" else "",Final_Xpath[key])) in [[0,0],[0]]:
												map(lambda x:l.add_value(key , ""),["just_one"])
										else:
												map(lambda x:l.add_value(key, i.xpath(x).extract()) if i.xpath(x).extract() != [] else "",Final_Xpath[key])
								except Exception,e:
										print Exception,",",e
						#将除了All_Xpath中的数据提取出来，像豆瓣就特别需要这种情况，一般下面的数据是（多次取得），All_Xpath中才是真正单条的数据
						for key in my_Final_Xpath.keys():
								item.fields[key] = Field()
								try:
										if map(lambda x:1 if x else 0, map(lambda x:response.xpath(x).extract() if x != "/" else "",Final_Xpath[key])) in [[0,0],[0]] and key != "site_name":
												map(lambda x:l.add_value(key , ""),["just_one"])
										elif key == "site_name":
												map(lambda x:l.add_value(key , x),my_Final_Xpath[key])
										else:
												map(lambda x:l.add_xpath(key , x) if response.xpath(x).extract() != [] else "",Final_Xpath[key])
								except Exception,e:
											print Exception,":",e
					
						if Some_Info:
								for key in Some_Info.keys():
									item.fields[key] = Field()
									l.add_value(key , Some_Info[key])
						yield l.load_item()
