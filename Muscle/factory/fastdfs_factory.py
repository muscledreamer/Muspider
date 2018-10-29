# -*- coding: utf-8 -*-
# @Email    : jqian_bo@163.com
# @Author  : bojingqian

import random
from conf import FDFS_NUM
from factory.FastDfsTools import FastDfsTask


class FastDFS(object):
    fastdfs_list = []
    for i in range(FDFS_NUM):
        k = FastDfsTask()
        fastdfs_list.append(k)
        print('init FastDFS' + str(i))

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not cls.fastdfs_list:
            try:
                if not cls.fastdfs_list:
                    cls.fastdfs_list = super(FastDFS, cls).__new__(cls)
            finally:
                pass
        num = random.randint(0, FDFS_NUM - 1)
        while True:
            try:
                return cls.fastdfs_list[num]
            except:
                try:
                    cls.fastdfs_list[num] = FastDfsTask()
                except Exception as e:
                    try:
                        cls.fastdfs_list[num] = FastDfsTask()
                    except Exception as e:
                        continue

# if __name__ == '__main__':
#     f = FastDFS()
#     a = f.saveBuffer(b"ttt", "html")
#     print(a)
