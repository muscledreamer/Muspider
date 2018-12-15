# -*- coding: utf-8 -*-
# @Email    : jqian_bo@163.com
# @Author  : bojingqian
from conf import BLOCK_TABLE, INFO_TABLE
from factory.Hbase_class import BaseHbase, DataBaseHbase


class BlockHbaseBase(BaseHbase):
    def __init__(self):
        super(BlockHbaseBase, self).__init__()
        self.table = BLOCK_TABLE

    def exists(self, rowkey):
        return super().exists(rowkey)


class InfoHbaseBase(DataBaseHbase):
    def __init__(self):
        super(InfoHbaseBase, self).__init__()
        self.table = INFO_TABLE

    def exists(self, rowkey):
        return super().exists(rowkey)


if __name__ == "__main__":
    blk = BlockHbaseBase()
    url = b'http://0.gravatar.com/avatar/0019964859b020bfd3f3dc4d9ddaa46b?s=37&'.decode()

    a = blk.exists(url)
    print(a)
    # org.run()
