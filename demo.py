# -*- coding: utf-8 -*-
# @Email: jqian_bo@163.com
# @Author: JingQian Bo
# @Create Time: 2018/10/22-3:29 PM

from main import Base
from conf import *


class NewsBreadthA(Base):
    def __init__(self):
        super(NewsBreadthA, self).__init__("logs/NewsBreadthA.log")
        self.kargs = {
            "redis_list_key": News_Breadth_A,
            "web_type": "news",
            "links_go": News_Breadth_A2,
            "all_link": True,
            "CONCURRENT_REQUESTS": 10,
            "CONCURRENT_ITEMS": 10,
        }

    @staticmethod
    def items_func():
        return {"news_boo": 1}

    def run_NewsBreadthA(self):
        super().run(kargs=self.kargs)


# 外交部新闻采集(百度搜索采集)
class NewsWjb(Base):
    def __init__(self):
        super(NewsWjb, self).__init__("logs/NewsWjb.log")
        self.kargs = {
            "proxy": None,
            "special_status": True,
            "redis_list_key": News_wjb_crawled_List,
            "web_type": "news",
            "links_go": "",
            "all_link": True,
            "CONCURRENT_REQUESTS": 10,
            "CONCURRENT_ITEMS": 10,
        }

    @staticmethod
    def items_func():
        return {"news_boo": 1}

    def NewsWjb(self):
        super().run(kargs=self.kargs)


if __name__ == '__main__':
    wjb = NewsWjb()
    wjb.NewsWjb()
