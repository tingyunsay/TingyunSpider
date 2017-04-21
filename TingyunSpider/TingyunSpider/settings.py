# -*- coding: utf-8 -*-

# Scrapy settings for TingyunSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'TingyunSpider'

SPIDER_MODULES = ['TingyunSpider.spiders']
NEWSPIDER_MODULE = 'TingyunSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'TingyunSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
#ROBOTSTXT_OBEY = True

#DOWNLOAD_DELAY = 2
DOWNLOAD_DELAY = 0.2
#LOG_LEVEL = 'DEBUG'
LOG_LEVEL = 'INFO'

#HTTP_PROXY = 'http://localhost:8118'
#http_proxy = 'http://localhost:8118'
#http_proxys = 'http://localhost:8118'

RETRY_HTTP_DELAY = 3
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]

DUPEFILTER_CLASS = 'scrapyjs.SplashAwareDupeFilter'
SPLASH_URL = 'http://127.0.0.1:8050/'
#SPLASH_URL = 'http://192.168.217.41:8050/'

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "tingyun"
MONGODB_COLLECTION = "copyright2"

DOWNLOADER_MIDDLEWARES = {
	#'TingyunSpider.middlewares.MyCustomDownloaderMiddleware': 543,
	'TingyunSpider.middlewares.RandomUserAgent': 5,
	#'TingyunSpider.middlewares.ProxyMiddleware': 30,
	#开启和关闭微博的cookie获取，涉及到在线打码，需注意是否启用
	#'TingyunSpider.cookie_middlewares.CookiesMiddleware': 100,
	'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 200,
	'scrapyjs.SplashMiddleware': 725,
}

ITEM_PIPELINES = {
	#'TingyunSpider.pipelines.SomePipeline': 300,
	#'TingyunSpider.pipelines.TingyunspiderPipeline': 300,
	#'TingyunSpider.pipelines.MongoPipeline': 300
	'TingyunSpider.pipelines.MariadbPipeline': 300
}

#scrapyi性能优化
CONCURRENT_REQUESTS = 100
#COOKIES_ENABLED=False

#开启dns缓存,默认大小10000kb,timeout 60s
DNSCACHE_ENABLED = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'TingyunSpider.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'TingyunSpider.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'TingyunSpider.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
