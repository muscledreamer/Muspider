# -*- coding: utf-8 -*-
# @Email: jqian_bo@163.com
# @Author: JingQian Bo
# @Create Time: 2018/10/19-11:13 AM
# -*- coding: utf-8 -*-

# 本地测试True
_DEBUG = True
# "TJ" or "WLMQ"
_PLACE = "TJ"

# 地区具体配置
place_config = {
    "WLMQ": {
        'REDIS_HOST': '10.10.21.19',
        'REDIS_PORT': 6379,
        'REDIS_CLUSTER': True,
        'CONCURRENT_REQUESTS': 16,
        'YIELD_COUNT': 10,
        'CONCURRENT_ITEMS': 20,
        'HBASE_ADDRESS_LIST': ['10.10.20.84', '10.10.20.85', '10.10.20.86', '10.10.20.87', '10.10.20.88'],
        'INFO_HBASE_ADDRESS_LIST': ['10.10.30.20', '10.10.30.21', '10.10.30.22', '10.10.30.24'],
        'FDFS_ADDRESS': 'http://10.10.20.21:8083/',
        "FDFS_CLIENT": "client_uq.conf"
    },
    "TJ": {
        'REDIS_HOST': '10.20.10.207',
        'REDIS_PORT': 6379,
        'REDIS_CLUSTER': False,
        'CONCURRENT_REQUESTS': 16,
        'YIELD_COUNT': 10,
        'CONCURRENT_ITEMS': 20,
        'HBASE_ADDRESS_LIST': ['192.168.120.81', '192.168.120.82', '192.168.120.83', '192.168.120.84',
                               '192.168.120.85'],
        'INFO_HBASE_ADDRESS_LIST': ['192.168.120.81', '192.168.120.82', '192.168.120.83', '192.168.120.84',
                                    '192.168.120.85'],
        'FDFS_ADDRESS': 'http://192.168.120.81:8083/',
        "FDFS_CLIENT": "client_tj.conf"
    }
}

# 配置选择
PLACE_CONFIG = place_config[_PLACE]

#  调度器
# SCHEDULER_PERSIST = True  # 在redis中保持scrapy-redis用到的各个队列，从而允许暂停和暂停后恢复
OS_LOGGING = False if _DEBUG else True  # 日志系统(本地False)
DETAIL_ABROAD_LOG = True  # 打印境外详细日志
PROXY_START = False  # 代理启用True
REDIS_CLUSTER = PLACE_CONFIG["REDIS_CLUSTER"]  # Redis 集群启动(勿动)
FDFS_CLIENT = PLACE_CONFIG["FDFS_CLIENT"]
TELNETCONSOLE_ENABLED = False  # Address already in use(勿动)
YIELD_COUNT = PLACE_CONFIG["YIELD_COUNT"]
CONCURRENT_ITEMS = PLACE_CONFIG["CONCURRENT_ITEMS"]

# 组件初始化数目
FDFS_NUM = 3
BLK_HBASE_NUM = 3
INFO_HBASE_NUM = 3
BBSINFO_HBASE_NUM = 3
REDIS_NUM = 2

BOT_NAME = 'collect_scrapy'  # 项目名称，默认情况下构造User-Agent，也用于日志记录。
COMMANDS_MODULE = 'collect_scrapy.commands'

SPIDER_MODULES = ['collect_scrapy.spiders']
NEWSPIDER_MODULE = 'collect_scrapy.spiders'

# COOKIES_ENABLED = True
# COOKIES_DEBUG = True

ITEM_PIPELINES = {
    'collect_scrapy.pipelines.ScrapyNewsPipeline': 1
}

DEFAULT_REQUEST_HEADERS = {
    'Referer': "http://www.baidu.com/"
}

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Redis Setting
REDIS_HOST = PLACE_CONFIG["REDIS_HOST"]
REDIS_PORT = PLACE_CONFIG["REDIS_PORT"]

# Scrapy Logging
# if not _DEBUG:
#    LOG_ENABLED = True
#    LOG_FILE = '{}/spider.logs'.format("/home/python/add_scrapy_log" if OS_LOGGING else "logs")
#    LOG_LEVEL = 'INFO'  # 日志级别
#    LOG_ENCODING = 'utf-8'
#    LOG_STDOUT = True
#    LOG_FORMAT = '%(asctime)s [%(name)s:%(module)s:%(funcName)s:%(lineno)s] %(message)s'
#
# 反爬及超时处理
# REDIRECT_ENABLED = False  # 禁止重定向
DOWNLOAD_TIMEOUT = 10  # 超时10秒忽略
DOWNLOAD_DELY = 0.2  # 相互延时

# 重新链接中间件
RETRY_ENABLED = False
# RETRY_TIMES = 1
# RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 408]

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1 if _DEBUG else PLACE_CONFIG["CONCURRENT_REQUESTS"]
CONCURRENT_REQUESTS_PER_DOMAIN = 5  # 4  # 针对单个网站的并发数，默认8
# CONCURRENT_ITEMS = 20
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 0.1
AUTOTHROTTLE_MAX_DELAY = 0.5
