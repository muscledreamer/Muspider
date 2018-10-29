# -*- coding: utf-8 -*-
# @Email: jqian_bo@163.com
# @Author: JingQian Bo
# @Create Time: 2018/10/29-11:30 AM
from tools import decode_content
from factory import FastDFSClient, RedisClient
from aio import control_process
from factory import output


class SaveUp(object):
    def __init__(self):
        self.FastDFS = FastDFSClient
        self.Redis = RedisClient
        self.log = output(log_path='demo.log', log_format=3, logger_name="SaveUp_log", console_output=True,
                      log_level="INFO")

    def up_dfs(self, content):
        url_fdfs_pwd = self.FastDFS.saveBuffer(content.encode(), "html")
        return url_fdfs_pwd

    def push_redis(self, redis_key, info):
        self.Redis.redis.rpush(redis_key, info)
        print("rpush --> {}:{}".format(redis_key, info))

    @staticmethod
    def decode_content(html):
        return decode_content(html)

    def aps(self, base_data_list):
        data_list = control_process(base_data_list, func=save_fdfs, process_count=20)
