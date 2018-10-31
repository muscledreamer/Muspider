# -*- coding: utf-8 -*-
# @Email: jqian_bo@163.com
# @Author: JingQian Bo
# @Create Time: 2018/10/29-11:30 AM
from tools import decode_content
from conf import LOG_PATH_PIPELINES
from factory import output, FastDFSClient, RedisClient


class Pipelines(object):
    def __init__(self):
        super(Pipelines, self).__init__()
        self.FastDFS = FastDFSClient()
        # self.Redis = RedisClient()
        self.log = output(log_path=LOG_PATH_PIPELINES, log_format=3, logger_name="pipelines_log", console_output=True,
                          log_level="INFO")

    @staticmethod
    def decode_content(html):
        return decode_content(html)

    def up_dfs(self, content):
        url_fdfs_pwd = self.FastDFS.save_buffer(content.encode(), "html")
        return url_fdfs_pwd

    def push_redis(self, redis_key, info):
        self.Redis.redis.rpush(redis_key, info)
        self.log.info("rpush --> {}:{}".format(redis_key, info))
