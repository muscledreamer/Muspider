# -*- coding: utf-8 -*-
# @Email: jqian_bo@163.com
# @Author: JingQian Bo
# @Create Time: 2018/11/6-10:24 AM
from factory import RedisClient

# p = RedisClient.pipe
#
# for i in range(100):
#     url = "http://www.sina.com.cn"
#     p.rpush("Muspider:crawl_list", url)
#     p.execute()


r = RedisClient.redis

print(type(r.type("abc")), r.type("abc"))
