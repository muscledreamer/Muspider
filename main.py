# -*- coding: utf-8 -*-
# @Email: jqian_bo@163.com
# @Author: JingQian Bo
# @Create Time: 2018/11/6-4:31 PM
import time
from aio import Spider
from start_urls import StartUrls
from pipelines import PipeWebCommon
from aio import control_process
from factory.Output import output


class Base(object):
    def __init__(self, log_path):
        super(Base, self).__init__()
        self.log = output(log_path=log_path, log_format=1, logger_name="MuspiderBase_log", console_output=True,
                          log_level="INFO")

    @staticmethod
    def items_func():
        return {}

    def run(self, *, kargs):
        proxy = kargs["proxy"]  # 代理设置
        special_status = kargs["special_status"]  # 特殊状态码
        links_go = kargs["links_go"]  # 链接生成地址
        web_type = kargs["web_type"]  # 类型
        all_link = kargs["all_link"]  # 是否获取全部链接
        redis_list_key = kargs["redis_list_key"]  # 任务起始队列
        CONCURRENT_REQUESTS = kargs["CONCURRENT_REQUESTS"]  # 并发数
        CONCURRENT_ITEMS = kargs["CONCURRENT_ITEMS"]
        su = StartUrls(redis_list_key, from_redis=True)
        spider = Spider(proxy=proxy, special_status=special_status)
        pipe = PipeWebCommon(web_type, links_go, all_link, self.items_func).common_func
        while True:
            url_list = su.rds_url(CONCURRENT_REQUESTS)
            if url_list:
                before_get_url = time.time()
                self.log.info("Get Urls Okay~ --> {}".format(len(url_list)))
                result = spider.aio_spider(url_list)
                self.log.info("Crawler {} --> Used:{}".format(len(result), time.time() - before_get_url))
                items = control_process(result, func=pipe, process_count=CONCURRENT_ITEMS)
                self.log.info("Send {} --> Used:{}".format(len(items), time.time() - before_get_url ))
