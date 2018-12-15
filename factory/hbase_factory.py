# -*- coding: utf-8 -*-
# @Email    : jqian_bo@163.com
# @Author  : bojingqian

import random
from setting import BLK_HBASE_NUM, INFO_HBASE_NUM
from factory.kind_of_hbase import BlockHbaseBase, InfoHbaseBase


class BlockHbase(object):
    hbase_list = []
    for i in range(BLK_HBASE_NUM):
        k = BlockHbaseBase()
        hbase_list.append(k)
        print('init Blkhbase' + str(i))

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not cls.hbase_list:
            try:
                if not cls.hbase_list:
                    cls.hbase_list = super(BlockHbase, cls).__new__(cls)
            finally:
                pass
        num = random.randint(0, BLK_HBASE_NUM - 1)
        while True:
            try:
                cls.hbase_list[num].exists('test')
                return cls.hbase_list[num]
            except:
                try:
                    cls.hbase_list[num] = BlockHbaseBase()
                except Exception as e:
                    try:
                        cls.hbase_list[num] = BlockHbaseBase()
                    except Exception as e:
                        continue


class InfoHbase(object):
    hbase_list = []
    for i in range(INFO_HBASE_NUM):
        k = InfoHbaseBase()
        hbase_list.append(k)
        print('init Infohbase' + str(i))

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not cls.hbase_list:
            try:
                if not cls.hbase_list:
                    cls.hbase_list = super(InfoHbase, cls).__new__(cls)
            finally:
                pass
        num = random.randint(0, INFO_HBASE_NUM - 1)
        while True:
            try:
                cls.hbase_list[num].exists('test')
                return cls.hbase_list[num]
            except:
                try:
                    cls.hbase_list[num] = InfoHbaseBase()
                except Exception as e:
                    try:
                        cls.hbase_list[num] = InfoHbaseBase()
                    except Exception as e:
                        continue
