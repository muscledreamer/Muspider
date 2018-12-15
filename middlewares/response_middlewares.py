# -*- coding: utf-8 -*-
# @Email: jqian_bo@163.com
# @Author: JingQian Bo
# @Create Time: 2018/11/6-10:57 AM
from tools import decode_content
from conf import LOG_PATH_REQUESTS
from factory.Output import output
from factory.Redis import RedisClient


class ResponseMiddlewares(object):
    def __init__(self):
        super(ResponseMiddlewares, self).__init__()
        self.rds = RedisClient
        self.log = output(log_path=LOG_PATH_REQUESTS, log_format=1, logger_name="pipelines_log", console_output=True,
                          log_level="INFO")


    def status_code(self):
        pass