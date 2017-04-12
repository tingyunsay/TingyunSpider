#!coding=utf-8

from TingyunSpider import general_func
import re
import requests
import json
import datetime

def get_month():
	now = datetime.datetime.now()
	cur_time = now.strftime("%Y-%m-%d")
	ago_time = datetime.datetime(now.year,(now.month-1),(now.day-1),now.hour,now.minute,now.second).strftime("%Y-%m-%d")
	return cur_time,ago_time


#接受五个参数，两个传递给Relative_to_Absolute（通用的跳转规则）；第三，四，五个决定特殊化定制
def R_2_A(index_url,url_tail,site_name,level,is_sege):
		if not is_sege:
				if level == 0:
						if site_name == "weibo_index":
								res_urls = []
								cur_time,ago_time = get_month()
								map(lambda i:res_urls.append("http://data.weibo.com/index/ajax/getchartdata?wid={wid}&sdate={ago_time}&edate={cur_time}".format(wid=i,ago_time=ago_time,cur_time=cur_time)),url_tail)
								return res_urls
						
						if site_name == "222stars_weibo":
								res_urls = []
								map(lambda i:res_urls.append(re.sub('com','cn',i)),url_tail[:1])
								return res_urls
						
						return general_func.Relative_to_Absolute(index_url,url_tail)
				elif level == 1:
						if site_name == "tudou_mv":
								res_urls = []
								map(lambda i:res_urls.append("http://www.tudou.com/crp/itemSum.action?uabcdefg=506178039&juabcdefg=01b4ivh4olvfj&iabcdefg={Id}".format(Id=i)),url_tail)
								return res_urls
						
						return general_func.Relative_to_Absolute(index_url,url_tail)
				elif level == 2:
						
						return general_func.Relative_to_Absolute(index_url,url_tail)
				elif level == 3:
						
						return general_func.Relative_to_Absolute(index_url,url_tail)
				elif level == 4:
						
						return general_func.Relative_to_Absolute(index_url,url_tail)
		else:
				if level == 0:
						if site_name == "le_show":
								res_urls = []
								map(lambda i:res_urls.append("http://www.le.com/zongyi/{aid}.html".format(aid=i)),url_tail)
								return res_urls
						if site_name == "le_sp":
								res_urls = []
								map(lambda i:res_urls.append("http://www.le.com/zongyi/{aid}.html".format(aid=i)),url_tail)
								return res_urls
						if site_name == "le_movie":
								res_urls = []
								map(lambda i:res_urls.append("http://www.le.com/ptv/vplay/{aid}.html".format(aid=i)),url_tail)
								return res_urls
						if site_name == "le_tv":
								res_urls = []
								map(lambda i:res_urls.append("http://www.le.com/tv/{aid}.html".format(aid=i)),url_tail)
								return res_urls
						if site_name == "qq_music":
								res_urls = []
								map(lambda i:res_urls.append("https://y.qq.com/portal/singer/{aid}.html".format(aid=i)),url_tail)
								return res_urls
						if site_name == "china_piaofang":
								res_urls = []
								map(lambda i:res_urls.append("http://www.cbooo.cn/m/{ID}".format(ID=i)),url_tail)
								return res_urls
						if site_name == "yongle_concert":
								res_urls = []
								map(lambda i:res_urls.append("http://www.228.com.cn/ticket-{productid}.html".format(productid=i)),url_tail)
								return res_urls
						if site_name == "le_mv":
								res_urls = []
								map(lambda i:res_urls.append("http://www.le.com/ptv/vplay/{vid}.html".format(vid=i)),url_tail)
								return res_urls
						if site_name == "tudou_mv":
								url_temp = []
								try:
										map(lambda x:url_temp.append(re.sub('/$',"",(re.search('(?<=view/).+',x).group()))) , url_tail)
								except Exception,e:
										print "处理tudou_mv接口失败......"
								res_urls = []
								map(lambda i:res_urls.append("http://www.tudou.com/crp/getDvdInfo.action?c=14&i={itemid}".format(itemid=i)),url_temp)
								return res_urls
						if site_name == "music_station_mv":
								res_urls = []
								map(lambda i:res_urls.append("http://mv.yinyuetai.com/all?enName=A&sort=monthViews&tab=allmv&parenttab=mv&artistId={aid}&page=1".format(aid=i)),url_tail)
								return res_urls
								
						return general_func.Relative_to_Absolute(index_url,url_tail)
				elif level == 1:
						
						return general_func.Relative_to_Absolute(index_url,url_tail)
				elif level == 2:
						
						return general_func.Relative_to_Absolute(index_url,url_tail)
				elif level == 3:
						
						return general_func.Relative_to_Absolute(index_url,url_tail)
				elif level == 4:
						
						return general_func.Relative_to_Absolute(index_url,url_tail)


#接受三个参数，一个传递给Except_For_PageNo（通用生成url规则）；第二三决定特殊化定制
#这个函数的作用是：
#		应对分页的情况，但存在分页，则会有一个类似标识 page_no 的参数，一般这个参数都是在url末尾 {直接使用Url_Generate即可，替换末尾的page_no}
#			如:http://www.xiami.com/artist/index/c/1/type/0/class/0/page/1
#			这时候，我们只需要按照规则构造这个page_no即可跳转到对应网页，那么这个函数的作用即是：构造 剥离出page_no的其他部分的url
#			如这里即是：http://www.xiami.com/artist/index/c/1/type/0/class/0/page/{page_no} 	之后给这个page_no赋值即可
#
#		若类似这种：www.youku.tv/1.html    -->   www.youku.tv/{page_no}.html
def U_G(index_url,site_name,level):
		if level == 0:
				if site_name == "xiami_album":
						return re.sub('(?<=r/)\d+',"{page}",index_url),index_url
				if site_name == "youku_show":
						return re.sub('(?<=p_)\d+',"{page}",index_url),index_url
				if site_name == "souhu_show":
						return re.sub('(?<=p10)\d+',"{page}",index_url),index_url
				if site_name == "mangguo_show":
						return re.sub('(?<=2-)\d+',"{page}",index_url),index_url
				if site_name == "youku_sp":
						return re.sub('(?<=p_)\d+',"{page}",index_url),index_url
				if site_name == "souhu_sp":
						return re.sub('(?<=p10)\d+',"{page}",index_url),index_url
				if site_name == "mangguo_sp":
						return re.sub('(?<=2-)\d+',"{page}",index_url),index_url
				if site_name == "mangguo_movie":
						return re.sub('(?<=2-)\d+',"{page}",index_url),index_url
				if site_name == "souhu_movie":
						return re.sub('(?<=p10)\d+',"{page}",index_url),index_url
				if site_name == "youku_tv":
						return re.sub('(?<=p_)\d+',"{page}",index_url),index_url
				if site_name == "mangguo_tv":
						return re.sub('(?<=2-)\d+',"{page}",index_url),index_url
				if site_name == "souhu_tv":
						return re.sub('(?<=p10)\d+',"{page}",index_url),index_url
				if site_name == "aiqiyi_mv":
						return re.sub('(?<=11-)\d+',"{page}",index_url),index_url
				if site_name == "aiqiyi_sp":
						return re.sub('(?<=11-)\d+',"{page}",index_url),index_url
				if site_name == "tudou_mv":
						index_url = "http://www.tudou.com/list/albumData.action?tagType=3&firstTagId=12&areaCode=230100&sort=1&page=1"
						return re.sub('\\d+$',"{page}",index_url),index_url
				if site_name == "aiqiyi_tv":
						return re.sub('(?<=11-)\d+',"{page}",index_url),index_url
				if site_name == "aiqiyi_movie":
						return re.sub('(?<=11-)\d+',"{page}",index_url),index_url
				if site_name == "aiqiyi_show":
						return re.sub('(?<=11-)\d+',"{page}",index_url),index_url
				if site_name == "yongle_concert":
						index_url = "http://www.228.com.cn/category/yanchanghui/?j=1&p=1"
						return general_func.Url_Generate(index_url),index_url
				
				
				return general_func.Url_Generate(index_url),index_url
		elif level == 1:

				return general_func.Url_Generate(index_url),index_url
		elif level == 2:
				if site_name == "wangyiyun_album":
						index_url = index_url+"&offset=0"
						return re.sub("(\d+)$","{page}",index_url),index_url
				if site_name == "wangyiyun_mv":
						index_url = index_url+"&offset=0"
						return re.sub("(\d+)$","{page}",index_url),index_url
				
				return general_func.Url_Generate(index_url),index_url
		elif level == 3:
				if site_name == "xiami_mv":
						index_url = index_url + "?type=all&page=1"
						return general_func.Url_Generate(index_url),index_url
				if site_name == "xiami_music":
						index_url = index_url + "?page=1"
						return general_func.Url_Generate(index_url),index_url

				return general_func.Url_Generate(index_url),index_url
		elif level == 4:
	
				return general_func.Url_Generate(index_url),index_url
		elif level == 5:
	
				return general_func.Url_Generate(index_url),index_url

#详情请到general_func中查看
def G_V_U(urls):
	return general_func.Get_Valid_Url(urls)

def C_U_V(url):
	return general_func.Check_Url_Valid(url)








