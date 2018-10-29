# -*- coding: utf-8 -*-
# @Email: jqian_bo@163.com
# @Author: JingQian Bo
# @Create Time: 2018/10/22-3:29 PM
from aio import Spider
from start_urls import StartUrls
from setting import CONCURRENT_REQUESTS as count

url = ["http://www.google.com" for _ in range(2)]
rds_key = "Muspider:crawl_list"

# 返回的是列表, {url: , text:}
su = StartUrls(url)
spider = Spider()
# 直接获取
url_list = su.get_url()
result = spider.aio_spider(url_list)
# print(result)
# while True:
#     url_list = su.rds_url(count)
#     # []
#
#
#
#     print(url_list)