# -*- coding: utf-8 -*-
# @Email    : jqian_bo@163.com
# @Author  : bojingqian

import random
from setting import *
from factory.Client import RdsConnection, FDfsConnection


class RedisClass(object):
    redis_list = []
    for i in range(REDIS_NUM):
        r = RdsConnection()
        redis_list.append(r)
        print('Init Redis' + str(i))

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


class FastDFSClass(object):
    fdfs_list = []
    for i in range(FDFS_NUM):
        r = FDfsConnection()
        fdfs_list.append(r)
        print('Init FastDFS' + str(i))

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not cls.fdfs_list:
            try:
                if not cls.fdfs_list:
                    cls.fdfs_list = super(FastDFSClass, cls).__new__(cls)
            finally:
                pass
        num = random.randint(0, FDFS_NUM - 1)
        # num = 0

        while True:
            try:
                # cls.redis_list[num].llen("NewsL:L:News_url")
                return cls.fdfs_list[num]
            except:
                try:
                    cls.fdfs_list[num] = FDfsConnection()
                except Exception as e:
                    try:
                        cls.fdfs_list[num] = FDfsConnection()
                    except Exception as e:
                        continue


if __name__ == "__main__":
    r = RedisClass()
    a = r.llen("NewsL:L:News_url")
    print(a)
