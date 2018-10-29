# -*- coding: utf-8 -*-
# @Email    : jqian_bo@163.com
# @Author  : bojingqian

import redis
import random
import rediscluster
from conf import *


class RdsConnection(object):
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, cluster=REDIS_CLUSTER):
        self.host = host
        self.port = port
        redis_ = rediscluster.StrictRedisCluster if cluster else redis.StrictRedis
        self.redis = redis_(host=self.host, port=self.port)
        self.pipe = self.redis.pipeline()


class RedisClass(object):
    redis_list = []
    for i in range(REDIS_NUM):
        r = RdsConnection()
        redis_list.append(r)
        print('init redis' + str(i))

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not cls.redis_list:
            try:
                if not cls.redis_list:
                    cls.redis_list = super(RedisClass, cls).__new__(cls)
            finally:
                pass
        num = random.randint(0, REDIS_NUM - 1)
        # num = 0

        while True:
            try:
                # cls.redis_list[num].llen("NewsL:L:News_url")
                return cls.redis_list[num]
            except:
                try:
                    cls.redis_list[num] = RdsConnection()
                except Exception as e:
                    try:
                        cls.redis_list[num] = RdsConnection()
                    except Exception as e:
                        continue


if __name__ == "__main__":
    r = RedisClass()
    a = r.llen("NewsL:L:News_url")
    print(a)
