# -*- coding: utf-8 -*-
# @Email    : jqian_bo@163.com
# @Author  : bojingqian
from setting import PLACE_CONFIG

# 杨经天代理池
PROXY_POOL = "Website_proxy:H:pool"

# 关注采集(定向关注)
GZ_NEWS_L = "NewsL:L:News_url_gz"  # 新闻关注上报

# 外交部采集
Jw_wjb_crawled_List = "JwL:L:Wjb_one"
News_wjb_crawled_List = "NewsL:L:Wjb_one"

# 境外测试采集
JingWai_test = "JwL:L:Test_All"

# 域名内全量采集
News_all = "NewsL:L:Hot_All"
SuDi_all = "SdL:L:Hot_All"
JingWai_all = "JwL:L:Hot_All"

# 滚动新闻采集
News_Breadth_A = "NewsL:L:Breadth_link"
News_Breadth_A2 = "NewsL:L:Breadth_links"

# 热度采集
News_Hot_A = "NewsL:L:Hot"
News_Hot_A2 = "NewsL:L:Hot_link"
News_Hot_A3 = "NewsL:L:Hot_links"

SuDi_Hot_A = "SdL:L:Hot"
SuDi_Hot_A2 = "SdL:L:Hot_link"
SuDi_Hot_A3 = "SdL:L:Hot_links"

JingWai_Hot_A = "JwL:L:Hot"
JingWai_Hot_A2 = "JwL:L:Hot_link"
JingWai_Hot_A3 = "JwL:L:Hot_links"

# 单条采集(基于百度搜索关键词or单条上报)
News_crawled_List = "News:L:Search"
Sd_crawled_List = "Sd:L:Search"
Jw_crawled_List = "Jw:L:Search"
Luntan_crawled_List = "Luntan:L:Search"

# 论坛采集队列
BBS_ALL_List = "Luntan:List"

All_news_info = "NewsH:All_info"  # 广度新闻INFO
Gundong_news_info = "NewsH:Gundong"  # 滚动新闻INFO
BBS_INFO = "Luntan:Info"
Add_Sd_A_info = "SdH:A:Hot_info"
Add_Jw_A_info = "JwH:A:Hot_info_breath"

# 发送请求与落地碎片计数器队列

# 单条队列 统计

# requests 统计
NEWS_DAY_REQUESTS_COUNT_ONE = "NewsH:Daily_requests_count_one"  # 新闻每日发送请求 统计
SD_DAY_REQUESTS_COUNT_ONE = "SdH:Daily_requests_count_one"  # 属地每日发送请求 统计
JW_DAY_REQUESTS_COUNT_ONE = "JwH:Daily_requests_count_one"  # 境外每日发送请求 统计
BBS_DAY_REQUESTS_COUNT_ONE = "BbsH:Daily_requests_count_one"  # 论坛每日发送请求 统计
# response 统计
NEWS_DAY_RESPONSE_COUNT_ONE = "NewsH:Daily_response_count_one"  # 新闻每日response 统计
SD_DAY_RESPONSE_COUNT_ONE = "SdH:Daily_response_count_one"  # 属地每日response 统计
JW_DAY_RESPONSE_COUNT_ONE = "JwH:Daily_response_count_one"  # 境外每日response 统计
BBS_DAY_RESPONSE_COUNT_ONE = "BbsH:Daily_response_count_one"  # 论坛每日response 统计
# 网页未发生变化 统计
NEWS_DAY_NOCHANGE_COUNT_ONE = "NewsH:Daily_nochange_count_one"  # 新闻每日response未发生变化 统计
SD_DAY_NOCHANGE_COUNT_ONE = "SdH:Daily_nochange_count_one"  # 属地每日response未发生变化 统计
JW_DAY_NOCHANGE_COUNT_ONE = "JwH:Daily_nochange_count_one"  # 境外每日response未发生变化 统计
BBS_DAY_NOCHANGE_COUNT_ONE = "BbsH:Daily_nochange_count_one"  # 论坛每日response未发生变化 统计
# 入库 统计
NEWS_DAY_INHBASE_COUNT_ONE = "NewsL:Daily_blk_count_one"  # 新闻每日碎片表插入数(传入解析队列) 统计
SD_DAY_INHBASE_COUNT_ONE = "SdL:Daily_blk_count_one"  # 属地每日碎片表插入数(传入解析队列) 统计
JW_DAY_INHBASE_COUNT_ONE = "JwL:Daily_blk_count_one"  # 境外每日碎片表插入数(传入解析队列) 统计
BBS_DAY_INHBASE_COUNT_ONE = "BbsL:Daily_blk_count_one"  # 论坛每日碎片表插入数(传入解析队列) 统计

# 综合队列 统计

# requests 统计
NEWS_DAY_REQUESTS_COUNT = "NewsH:Daily_requests_count"  # 新闻每日发送请求 统计
SD_DAY_REQUESTS_COUNT = "SdH:Daily_requests_count"  # 属地每日发送请求 统计
JW_DAY_REQUESTS_COUNT = "JwH:Daily_requests_count"  # 境外每日发送请求 统计
BBS_DAY_REQUESTS_COUNT = "BbsH:Daily_requests_count"  # 论坛每日发送请求 统计
# response 统计
NEWS_DAY_RESPONSE_COUNT = "NewsH:Daily_response_count"  # 新闻每日response 统计
SD_DAY_RESPONSE_COUNT = "SdH:Daily_response_count"  # 属地每日response 统计
JW_DAY_RESPONSE_COUNT = "JwH:Daily_response_count"  # 境外每日response 统计
BBS_DAY_RESPONSE_COUNT = "BbsH:Daily_response_count"  # 论坛每日response 统计
# 网页未发生变化 统计
NEWS_DAY_NOCHANGE_COUNT = "NewsH:Daily_nochange_count"  # 新闻每日response未发生变化 统计
SD_DAY_NOCHANGE_COUNT = "SdH:Daily_nochange_count"  # 属地每日response未发生变化 统计
JW_DAY_NOCHANGE_COUNT = "JwH:Daily_nochange_count"  # 境外每日response未发生变化 统计
# 入库 统计
NEWS_DAY_INHBASE_COUNT = "NewsL:Daily_blk_count"  # 新闻每日碎片表插入数(传入解析队列)统计
SD_DAY_INHBASE_COUNT = "SdL:Daily_blk_count"  # 属地每日碎片表插入数(传入解析队列)统计
JW_DAY_INHBASE_COUNT = "JwL:Daily_blk_count"  # 境外每日碎片表插入数(传入解析队列)统计
BBS_DAY_INHBASE_COUNT = "BbsL:Daily_blk_count"  # 论坛每日碎片表插入数(传入解析队列)统计

# 域名信息
NEWS_DOMAIN = "NewsH:Domain"  # 新闻域名信息表
SD_DOMAIN = "SdH:Domain"  # 属地域名信息表
JW_DOMAIN = "JwH:Domain"  # 境外域名信息表
BBS_DOMAIN = "Luntan:Domain"  # 论坛博客域名信息表
BBS_DOMAIN_NAME = "Luntan:Name"  # 论坛博客域名对应论坛名信息表

# NEWS_CK = "NewsH:Crawl_key"  # 新闻爬取主键信息表
# NEWS_HARM_L = "NewsL:Harmful:News_url"  # 有害新闻信息通道
# NEWS_HARM_H = "NewsH:Harmful:News_info"  # 有害新闻信息表

# 解析队列
NEWS_REDIS_ANALYSIS = "NewsL:News_Identity"  # 新闻解析接口
REDIS_HARM_ANALYSIS = "NewsL:News_HARM_Identity"  # 有害新闻解析接口
GZ_REDIS_ANALYSIS = "NewsL:News_Identity_gz"  # 关注上报解析接口
SD_REDIS_ANALYSIS = "Monitor:C_Identity2"  # 属地解析接口
JW_REDIS_ANALYSIS = "Monitor:P_Identity2"  # 境外解析接口

# bloomfilter
FILTER_KEY_HTML_NEWS = 'News:BF:HTML'
FILTER_KEY_HTML_HARM = 'News:BF:Harmful_HTML'
FILTER_KEY_HTML_MONITOR = 'Monitor:BF:HTML'
BBS_FILTER_KEY_HTML = 'Luntan:BF:HTML'

no_type_list = ['png', "jpeg", 'jpg', 'apk', 'js', 'css', 'xml', 'svg', 'pdf', 'rar', 'doc', 'mp3']  # 非法链接后缀
# 百度域名忽略黑名单
baidu_black_list = ["news.baidu", "zhidao.baidu",
                    "music.baidu", "image.baidu",
                    "v.baidu", "map.baidu",
                    "wenku.baidu"]

# DFS IP&PORT
FDFS_ADDRESS = PLACE_CONFIG["FDFS_ADDRESS"]

# #文件存放路径
FOLDER_PWD = "/home/python/download_files/news_file"

# Block_Hbase IDC
HBASE_ADDRESS_LIST = PLACE_CONFIG["HBASE_ADDRESS_LIST"]
INFO_HBASE_ADDRESS_LIST = PLACE_CONFIG["INFO_HBASE_ADDRESS_LIST"]

HBASE_PORT = '9090'

# # 正式log地址
# LOGG_PATH_REQUESTS = '/home/python/add_scrapy_log/requests.logs'
# LOGG_PATH_PIPELINES = '/home/python/add_scrapy_log/pipelines.logs'
# LOGG_PATH_REDIRECTION = '/home/python/add_scrapy_log/redirection.logs'

# 测试log地址
LOG_PATH_REQUESTS = 'logs/requests.logs'
LOG_PATH_PIPELINES = 'logs/pipelines.logs'
LOG_PATH_REDIRECTION = 'logs/redirection.logs'

# 境外代理池
# PROXIES_POOL = [
#     {'ip_port': '127.0.0.1:9999', 'user_pass': None},
#     {'ip_port': '127.0.0.1:9998', 'user_pass': None},
#     {'ip_port': '127.0.0.1:9997', 'user_pass': None},
#     {'ip_port': '127.0.0.1:9996', 'user_pass': None},
#     {'ip_port': '127.0.0.1:9995', 'user_pass': None},
#     {'ip_port': '127.0.0.1:9994', 'user_pass': None},
#     {'ip_port': '127.0.0.1:9993', 'user_pass': None},
#     {'ip_port': '127.0.0.1:9992', 'user_pass': None},
#     {'ip_port': '127.0.0.1:9991', 'user_pass': None},
#     # {'ip_port': '127.0.0.1:9990', 'user_pass': None},
#
# ]

PROXIES_POOL = ['127.0.0.1:9991', '127.0.0.1:9992', '127.0.0.1:9993']

# 香港代理池
PROXIES_HK = [
    {'ip_port': '47.91.229.77:23400', 'user_pass': None},
]
# 境内代理池
PROXIES_CH_POOL = [
    {'ip_port': '116.62.202.199:23400', 'user_pass': None},  # 1
    {'ip_port': '47.104.13.50:23400', 'user_pass': None},  # 0
    {'ip_port': '47.92.152.67:23400', 'user_pass': None},  # 1
    {'ip_port': '47.100.121.114:23400', 'user_pass': None},  # 0
]

# # 新大接口
# XINDA_URL = 'http://10.10.40.2:10003/whichlang'

Agents = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
    "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
]

# 境外三级中间件设置
abroad_settings = {
    'DOWNLOAD_DELAY': 3,
    'RANDOMIZE_DOWNLOAD_DELAY': True,
    'CONCURRENT_REQUESTS': 5,
    'CONCURRENT_REQUESTS_PER_DOMAIN': 4,
    'RETRY_ENABLED': True,
    'RETRY_TIMES': 1,
    'DOWNLOAD_TIMEOUT': 15,
    'DEFAULT_REQUEST_HEADERS': {
        'Referer': "http://www.google.com/"
    },
    'DOWNLOADER_MIDDLEWARES': {
        # "collect_scrapy.middlewares.request_middleware.CheckProxyMiddleware": 10,
        "collect_scrapy.middlewares.request_middleware.UrlHourEffectiveness": 90,
        # "collect_scrapy.middlewares.request_middleware.UrlHbaseEffectiveness": 95,
        "collect_scrapy.middlewares.request_middleware.HeaderMiddleware": 450,
        "collect_scrapy.middlewares.request_middleware.RedisLoggingMiddleware": 570,
        "collect_scrapy.middlewares.response_middleware.CheckMiddleware": 595,
    }
}

# 境外全量中间件设置
abroad_all_settings = {
    'DOWNLOAD_DELAY': 1,
    'RANDOMIZE_DOWNLOAD_DELAY': True,
    'CONCURRENT_REQUESTS': 10,
    'CONCURRENT_REQUESTS_PER_DOMAIN': 10,
    'RETRY_ENABLED': True,
    'RETRY_TIMES': 2,
    'DOWNLOAD_TIMEOUT': 20,
    'DEFAULT_REQUEST_HEADERS': {
        'Referer': "http://www.google.com/"
    },
    'DOWNLOADER_MIDDLEWARES': {
        # "collect_scrapy.middlewares.request_middleware.CheckProxyMiddleware": 10,
        "collect_scrapy.middlewares.request_middleware.UrlHourEffectiveness": 90,
        # "collect_scrapy.middlewares.request_middleware.UrlHbaseEffectiveness": 95,
        "collect_scrapy.middlewares.request_middleware.HeaderMiddleware": 450,
        "collect_scrapy.middlewares.request_middleware.RedisLoggingMiddleware": 570,
        "collect_scrapy.middlewares.response_middleware.CheckMiddleware": 595,
    }
}

# 境外测试中间件设置
abroad_test_settings = {
    'DOWNLOAD_DELAY': 1,
    'RANDOMIZE_DOWNLOAD_DELAY': True,
    'CONCURRENT_REQUESTS': 1,
    'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
    'RETRY_ENABLED': False,
    'RETRY_TIMES': 2,
    'DOWNLOAD_TIMEOUT': 20,
    'DEFAULT_REQUEST_HEADERS': {
        'Referer': "http://www.google.com/"
    },
    'DOWNLOADER_MIDDLEWARES': {
        # "collect_scrapy.middlewares.request_middleware.CheckProxyMiddleware": 10,
        # "collect_scrapy.middlewares.request_middleware.UrlHourEffectiveness": 90,
        # "collect_scrapy.middlewares.request_middleware.UrlHbaseEffectiveness": 95,
        "collect_scrapy.middlewares.request_middleware.HeaderMiddleware": 450,
        "collect_scrapy.middlewares.request_middleware.RedisLoggingMiddleware": 570,
        "collect_scrapy.middlewares.response_middleware.CheckMiddleware": 595,
    }
}

# 外交部中间件设置
baidu_search_settings = {
    'CONCURRENT_REQUESTS': 32,
    'DOWNLOADER_MIDDLEWARES': {
        # "collect_scrapy.middlewares.request_middleware.CheckProxyMiddleware": 10,
        # "collect_scrapy.middlewares.request_middleware.UrlHourEffectiveness": 90,
        # "collect_scrapy.middlewares.request_middleware.UrlHbaseEffectiveness": 95,
        "collect_scrapy.middlewares.request_middleware.HeaderMiddleware": 450,
        "collect_scrapy.middlewares.request_middleware.RedisLoggingMiddleware": 570,
        "collect_scrapy.middlewares.response_middleware.CheckMiddleware": 595,
    }
}
