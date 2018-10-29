# -*- coding: utf-8 -*-
# @Email: jqian_bo@163.com
# @Author: JingQian Bo
# @Create Time: 2018/10/19-9:29 AM
import re
from factory import RedisClient
from MuException import *


class StartUrls(object):
    def __init__(self, name, from_redis=False):
        self.name = name
        self.class_name = __class__.__name__
        self.rds = RedisClient() if from_redis else ()
        self.rds_url() if from_redis else self.get_url()

    def rds_url(self, count=1):
        pipe = self.rds.pipe
        if self.rds.redis.llen(self.name) <= count:
            return []
        while count > 0:
            pipe.lpop(self.name)
            count -= 1
        urls = pipe.execute()
        return urls

    def get_url(self):
        if isinstance(self.name, str):
            result = [self.name]
        elif isinstance(self.name, list):
            result = self.name
        else:
            raise Error(
                Error.ParameterError.format(Class=self.class_name, Parameter=self.name, True_type="list or str"))
        return result
