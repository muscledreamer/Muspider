# -*- coding: utf-8 -*-
# @Email    : jqian_bo@163.com
# @Author  : bojingqian
from random import choice
from hbase.ttypes import *
from hbase import THBaseService
from thrift.transport import TSocket
from thrift.protocol import TBinaryProtocol
from conf import HBASE_ADDRESS_LIST, INFO_HBASE_ADDRESS_LIST, HBASE_PORT


class BaseHbase(object):
    def __init__(self, *, adderss=choice(HBASE_ADDRESS_LIST), port=HBASE_PORT):
        super(BaseHbase, self).__init__()
        self.table = ""
        self.address = adderss
        self.port = port
        self.client = self.init_client()

    def init_client(self):
        transport = TSocket.TSocket(self.address, self.port)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        transport.open()
        client = THBaseService.Client(protocol)
        return client

    def exists(self, rowkey):
        get = TGet()
        get.row = rowkey.encode()
        try:
            result = self.client.exists(self.table.encode(), get)
        except:
            self.client = self.init_client()
            result = self.client.exists(self.table.encode(), get)
        return result


class DataBaseHbase(object):
    def __init__(self, *, adderss=choice(INFO_HBASE_ADDRESS_LIST), port=HBASE_PORT):
        super(DataBaseHbase, self).__init__()
        self.table = ""
        self.address = adderss
        self.port = port
        self.client = self.init_client()

    def init_client(self):
        transport = TSocket.TSocket(self.address, self.port)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        transport.open()
        client = THBaseService.Client(protocol)
        return client

    def exists(self, rowkey):
        get = TGet()
        get.row = rowkey.encode()
        try:
            result = self.client.exists(self.table.encode(), get)
        except:
            self.client = self.init_client()
            result = self.client.exists(self.table.encode(), get)
        return result

# if __name__ == "__main__":
#     # pass
#     rowkey = "163.com_http://money.163.com/17/1110/00/D2RD7237002580S6.html'"
#     # org = OrgHbase()
#     # org_dict = org.getResultByRowkey(rowkey)
#     info = InfoHbase()
#     info_dict = info.getResultByRowkey(rowkey)
#     # print(org_dict)
#     print(info_dict)
