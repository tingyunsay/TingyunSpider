#!coding=utf-8

from TingyunSpider import general_func


#这个文件：分离出所有需要计算站点实际page页面的模块，一个可扩展的if elif语句来实现

#这个是对所有的当前同级页面的总的page数的一个统计
#Total_page_circulate接受两个参数，前者是最大的数据数，后者是每一页面包含的数据数，相除得到最大页面的page_no
def T_P_C(site_name,max_pages,level):
		if level == 0:
				if site_name == "xiami_album":
						return general_func.Total_page_circulate(max_pages,30)
				if site_name == "tudou_show":
						return general_func.Total_page_circulate(max_pages,84)
				if site_name == "tudou_sp":
						return general_func.Total_page_circulate(max_pages,84)
				if site_name == "tudou_tv":
						return general_func.Total_page_circulate(max_pages,90)
				if site_name == "tudou_mv":
						return general_func.Total_page_circulate(max_pages,40)
				if site_name == "le_tv":
						return general_func.Total_page_circulate(max_pages,30)
				if site_name == "le_sp":
						return general_func.Total_page_circulate(max_pages,30)
				if site_name == "le_show":
						return general_func.Total_page_circulate(max_pages,30)
				if site_name == "yongle_concert":
						return general_func.Total_page_circulate(max_pages,12)
				if site_name == "tudou_music":
						return general_func.Total_page_circulate(max_pages,40)
				if site_name == "tudou_movie":
						return general_func.Total_page_circulate(max_pages,90)
				if site_name == "le_mv":
						return general_func.Total_page_circulate(max_pages,30)

				return general_func.Total_page_circulate(max_pages,1)
		elif level == 1:
				if site_name == "xiami_mv":
						return general_func.Total_page_circulate(max_pages,30)
				
				return general_func.Total_page_circulate(max_pages,1)
		elif level == 2:
				if site_name == "xiami_album":
						return general_func.Total_page_circulate(max_pages,9)
				else:	
						return general_func.Total_page_circulate(max_pages,1)
		elif level == 3:
				if site_name == "xiami_album":
						return general_func.Total_page_circulate(max_pages,9)
				if site_name == "xiami_mv":
						return general_func.Total_page_circulate(max_pages,20)
				if site_name == "xiami_music":
						return general_func.Total_page_circulate(max_pages,20)
				
				return general_func.Total_page_circulate(max_pages,1)
		elif level == 4:
				
				return general_func.Total_page_circulate(max_pages,1)
		elif level == 5:
				
				return general_func.Total_page_circulate(max_pages,1)


#指定当前层你指定的page数，像豆瓣，即没有最大页数，无法自动切分分页，手动指定
def T_P_B(site_name,max_pages,level):
		if level == 0:
				if site_name == "douban_movie":
						return 17
				if site_name == "douban_tv":
						return 25
				if site_name == "aiqiyi_mv":
						return 30
				if site_name == "aiqiyi_tv":
						return 30
				if site_name == "aiqiyi_movie":
						return 30
				if site_name == "aiqiyi_show":
						return 30
				if site_name == "tudou_mv":
						return 30
				
				return max_pages
		elif level == 1:
				if site_name == "xiami_album":
						return general_func.Total_page_circulate(max_pages,30)
				if site_name == "xiami_music":
						return general_func.Total_page_circulate(max_pages,30)
				
				return max_pages
		elif level == 2:
				
				return max_pages
		elif level == 3:
				if site_name == "xiami_music":
						return 1
				
				return max_pages
		elif level == 4:
				
				return max_pages
		elif level == 5:
			
				return max_pages
				
#有些网页的page_no格式不一样
#比如:www.example.net/xxx/xxxx/page_no=0
#	  www.example.net/xxx/xxxx/page_no=20
#	  www.example.net/xxx/xxxx/page_no=40
#这时候还需要对page_no作处理
#Turn_True_Page，作类似 1 ->> 1*page_num 这样的改变，默认是1，指定一页包含的page_num即可
def T_T_P(page_no,site_name,level):
		if level == 0:
				if site_name == "tencent_show":
						return general_func.Turn_True_Page(page_no,30)
				if site_name == "tencent_sp":
						return general_func.Turn_True_Page(page_no,30)
				if site_name == "tencent_tv":
						return general_func.Turn_True_Page(page_no,30)
				if site_name == "tencent_movie":
						return general_func.Turn_True_Page(page_no,30)
				if site_name == "douban_tv":
						return general_func.Turn_True_Page(page_no,20)
				if site_name == "douban_movie":
						return general_func.Turn_True_Page(page_no,20)

				return general_func.Turn_True_Page(page_no,1)
		elif level == 1:

				return general_func.Turn_True_Page(page_no,1)
		elif level == 2:
				if site_name == "wangyiyun_album":
						return general_func.Turn_True_Page(page_no,12)
				if site_name == "wangyiyun_mv":
						return general_func.Turn_True_Page(page_no,12)

				return general_func.Turn_True_Page(page_no,1)
		elif level == 3:

				return general_func.Turn_True_Page(page_no,1)
		elif level == 4:

				return general_func.Turn_True_Page(page_no,1)
		elif level == 5:

				return general_func.Turn_True_Page(page_no,1)
				










