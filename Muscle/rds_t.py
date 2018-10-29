# -*- coding: utf-8 -*-
# @Email: jqian_bo@163.com
# @Author: JingQian Bo
# @Create Time: 2018/9/11-上午10:00
from conf import BJ_test
from factory.redis_factory import RdsConnection

R = RdsConnection()
rds = R.redis

for _ in range(12):
    rds.rpush(BJ_test, "http://www.sina.com.cn")
