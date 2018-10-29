# -*- coding: utf-8 -*-
# @Email: jqian_bo@163.com
# @Author: JingQian Bo
# @Create Time: 2018/10/19-11:20 AM
from setting import _DEBUG
from factory.Output import output


def redis_client():
    if _DEBUG:
        from factory.Client import RdsConnection
        return RdsConnection

    else:
        from factory.Singleton import RedisClass
        return RedisClass


def fdfs_client():
    if _DEBUG:
        from factory.Client import FDfsConnection
        return FDfsConnection

    else:
        from factory.Singleton import FastDFSClass
        return FastDFSClass


RedisClient = redis_client()
FastDFSClient = fdfs_client()
