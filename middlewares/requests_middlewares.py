# -*- coding: utf-8 -*-
# @Email: jqian_bo@163.com
# @Author: JingQian Bo
# @Create Time: 2018/11/6-10:57 AM
from conf import LOG_PATH_REQUESTS
from factory.Output import output
from factory.Redis import RedisClient
from tools import base_url_list, url_boo_hour


class Requests(object):
    def __init__(self):
        super(Requests, self).__init__()
        self.rds = RedisClient
        self.log = output(log_path=LOG_PATH_REQUESTS, log_format=1, logger_name="pipelines_log", console_output=True,
                          log_level="INFO")
        self.base_url_list = base_url_list

    @staticmethod
    def requests_headers(headers, cookies, proxies):
        return {
            "headers": headers,
            "cookies": cookies,
            "proxies": proxies,
        }

    def url_exist(self, url):
        if url[:3] != "htt":
            return 0
        if url not in self.base_url_list and url_boo_hour(url):
            self.log.debug("时间布隆忽略 ", url)
            return 0
        return 1

