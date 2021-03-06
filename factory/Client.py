# -*- coding: utf-8 -*-
# @Email    : jqian_bo@163.com
# @Author  : bojingqian
# -*- coding:utf-8 -*-

import redis
import rediscluster
from setting import _DEBUG
from fdfs_client.client import *
from setting import FDFS_CLIENT, REDIS_HOST, REDIS_PORT, REDIS_CLUSTER


class RdsConnection(object):
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, cluster=REDIS_CLUSTER):
        self.host = host
        self.port = port
        redis_client = rediscluster.StrictRedisCluster if cluster else redis.StrictRedis
        self.redis = redis_client(host=self.host, port=self.port)
        self.pipe = self.redis.pipeline()


# 上传端口：22122
# 下载端口：8080
class FDfsConnection(object):
    def __init__(self):
        self.client_file = FDFS_CLIENT
        self.client = Fdfs_client(self.client_file)

    def save_file(self, filepath: str):
        """ 通过本地文件上传fastdfs
        :param filepath: 本地文件路径
        :return: 存储fastdfs地址
        """
        if os.path.exists(filepath):
            ret0 = self.client.upload_by_filename(filepath)
            if ret0['Status'] == 'Upload successed.':
                fastdfs_nameid = ret0['Remote file_id'].decode()
                return fastdfs_nameid
        else:
            return "No such File:{}".format(filepath)

    def delete_file(self, dfs_name: str):
        """ 删除fastdfs中的文件
        :param dfs_name: fastdfs中地址, 以group开头
        :return: 删除信息
        """
        ret1 = self.client.delete_file(dfs_name)
        return ret1

    def save_buffer(self, buf: bytes, suffix: str = None):
        """ 流文件上传fastdfs
        :param buf: 文本内容(bytes)类型
        :param suffix: 上传文件尾缀
        :return: 存储fastdfs地址
        """
        try:
            ret = self.client.upload_by_buffer(buf, file_ext_name=suffix)
            result = self.check_exception(ret)
            if not result:
                self.client = Fdfs_client(self.client_file)
                ret = self.client.upload_by_buffer(buf, file_ext_name=suffix)
                result = self.check_exception(ret)
        except Exception as e:
            self.client = Fdfs_client(self.client_file)
            ret = self.client.upload_by_buffer(buf, file_ext_name=suffix)
            result = self.check_exception(ret)
        return result

    @staticmethod
    def check_exception(ret):
        try:
            dfsName = ret['Remote file_id'].decode()
            if 'group' in dfsName:
                return dfsName
            else:
                return ""
        except:
            return ""
    # def download_file(self, address):
    #     ret = self.client.download_to_buffer(address)
    #     print(ret)
    #     return ret
    # try:
    #     ret = self.client.download_to_buffer(address)
    #     result = self.checkException(ret)
    #     if not result:
    #         self.client = Fdfs_client('client.conf')
    #         ret = self.client.upload_by_buffer(buf, file_ext_name=ext)
    #         result = self.checkException(ret)
    # except Exception as e:
    #     self.client = Fdfs_client('client.conf')
    #     ret = self.client.upload_by_buffer(buf, file_ext_name=ext)
    #     result = self.checkException(ret)
    # return ret


def redis_client():
    if _DEBUG:
        return RdsConnection()

    else:
        from factory.Singleton import RedisClass
        return RedisClass()


def fdfs_client():
    if _DEBUG:
        return FDfsConnection()
    else:
        from factory.Singleton import FastDFSClass
        return FastDFSClass()


if __name__ == "__main__":
    import requests
    from conf import FDFS_ADDRESS
    file_text = b"123"
    fdfs = FDfsConnection()
    a = fdfs.save_buffer(file_text)
    status_code = requests.get("{}{}".format(FDFS_ADDRESS, a)).status_code
    print(status_code)
    # b = "group1/M00/00/00/wKiBDVviUYeAAzkuAAAAA4i3nNI8631577"
    # c = fdfs.delete_file(b)
    print(a)
