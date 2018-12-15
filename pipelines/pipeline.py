# -*- coding: utf-8 -*-
# @Email: jqian_bo@163.com
# @Author: JingQian Bo
# @Create Time: 2018/10/29-11:30 AM
from tools import decode_content, get_title
from conf import LOG_PATH_PIPELINES
from factory.Output import output
from factory.FastDFS import FastDFSClient
from factory.Redis import RedisClient


class PipeBase(object):
    def __init__(self):
        super(PipeBase, self).__init__()
        self.log = output(log_path=LOG_PATH_PIPELINES, log_format=3, logger_name="pipelines_log", console_output=True,
                          log_level="INFO")

    @staticmethod
    def pipe_decode_content(html):
        return decode_content(html)

    @staticmethod
    def pipe_get_title(html):
        return get_title(html)

    @staticmethod
    def pipe_url_correction(url):
        return url[:-1] if url.endswith("/") else url

    # def pipe_up_dfs(self, content):
    #     url_fdfs_pwd = self.FastDFS.save_buffer(content.encode(), "html")
    #     return url_fdfs_pwd

    # def pipe_push_redis(self, redis_key, info):
    #     self.rds.redis.rpush(redis_key, info)
    #     self.log.info("rpush --> {}:{}".format(redis_key, info))
