# -*- coding: utf-8 -*-
# @Email: jqian_bo@163.com
# @Author: JingQian Bo
# @Create Time: 2018/10/22-3:29 PM
from aio import Spider, Pipelines, control_process
from start_urls import StartUrls
from setting import CONCURRENT_REQUESTS, CONCURRENT_ITEMS

url = ["http://www.sina.com.cn" for _ in range(2)]
rds_key = "Muspider:crawl_list"

# 返回的是列表, {url: , text:}
su = StartUrls(url)
spider = Spider()
# 直接获取
url_list = su.get_url()
result = spider.aio_spider(url_list)


class Analysis(Pipelines):
    def __init__(self):
        super(Analysis, self).__init__()

    # def up_dfs(self, content):
    #     return super().up_dfs(content)
    #
    # @staticmethod
    # def decode_content(html):
    #     return super().decode_content(html)

    def save_fdfs(self, result):
        html = result["html"]
        content = super().decode_content(html)
        address = super().up_dfs(content)
        print(address)


analysis = Analysis()

control_process(result, func=analysis.save_fdfs, process_count=CONCURRENT_ITEMS)

# print(result)
# while True:
#     url_list = su.rds_url(count)
#     # []
#
#
#
#     print(url_list)
