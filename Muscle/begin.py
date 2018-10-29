# -*- coding: utf-8 -*-
# @Email: jqian_bo@163.com
# @Author: JingQian Bo
# @Create Time: 2018/9/11-上午9:49
from conf import BJ_test
from factory.redis_factory import RdsConnection
from aio_request import asynchronous

R = RdsConnection()
rds = R.redis
pipe = R.pipe



def run():
    while True:
        url_count = rds.llen(BJ_test)
        if url_count >= 12:
            download()


def download():
    count = 12
    while count > 0:
        pipe.lpop(BJ_test)
        count -= 1
    all_data = pipe.execute()
    all_url = [url.decode() for url in all_data if url]
    print("Get len {}".format(len(all_url)))
    asynchronous(all_url)


if __name__ == '__main__':
    run()
