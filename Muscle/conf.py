# -*- coding: utf-8 -*-
# @Email: jqian_bo@163.com
# @Author: JingQian Bo
# @Create Time: 2018/9/11-上午9:51

PLACE = "TJ"

# 地区具体配置
place_config = {
    "WLMQ": {
        'REDIS_HOST': '10.10.20.91',
        'REDIS_PORT': 6381,
        'REDIS_CLUSTER': True,
        "REDIS_NUM": 5,
        "FDFS_NUM": 5,
        'CONCURRENT_REQUESTS': 16,
        'HBASE_ADDRESS_LIST': ['10.10.20.84', '10.10.20.85', '10.10.20.86', '10.10.20.87', '10.10.20.88'],
        'INFO_HBASE_ADDRESS_LIST': ['10.10.30.20', '10.10.30.21', '10.10.30.22', '10.10.30.24'],
        'FDFS_ADDRESS': 'http://10.10.20.21:8083/',
        "FDFS_CLIENT": "client_uq.conf"
    },
    "TJ": {
        # 'REDIS_HOST': '10.20.10.207',
        'REDIS_HOST': '127.0.0.1',
        'REDIS_PORT': 6379,
        'REDIS_CLUSTER': False,
        "REDIS_NUM": 5,
        "FDFS_NUM": 5,
        'CONCURRENT_REQUESTS': 16,
        'HBASE_ADDRESS_LIST': ['192.168.120.81', '192.168.120.82', '192.168.120.83', '192.168.120.84',
                               '192.168.120.85'],
        'INFO_HBASE_ADDRESS_LIST': ['192.168.120.81', '192.168.120.82', '192.168.120.83', '192.168.120.84',
                                    '192.168.120.85'],
        'FDFS_ADDRESS': 'http://192.168.120.81:8083/',
        "FDFS_CLIENT": "client_tj.conf"
    }
}
BJ_test = "tj:bjtest"
BJ_dfs_test = "tj:bjdfs"
config = place_config[PLACE]
REDIS_HOST = config["REDIS_HOST"]
REDIS_PORT = config["REDIS_PORT"]
REDIS_CLUSTER = config["REDIS_CLUSTER"]
REDIS_NUM = config["REDIS_NUM"]
FDFS_CLIENT = config["FDFS_CLIENT"]
FDFS_NUM = config["FDFS_NUM"]
