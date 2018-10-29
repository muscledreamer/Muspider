# -*- coding: utf-8 -*-
# @Email    : jqian_bo@163.com
# @Author  : bojingqian

import asyncio
import aiohttp
import pymysql
import re
import time
from pyquery import PyQuery as pq

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

# words = ['good', 'bad', 'cool',
#          'hot', 'nice', 'better',
#          'head', 'up', 'down',
#          'right', 'left', 'east']

headers = dict()
headers[
    "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36"


def control_thread(list_, *, func=None, thread_count=20):
    result = []
    if func and list_:
        if len(list_) < thread_count:
            result = thread_pool(list_, func=func)
        else:
            base_info_lists = [list_[i:i + thread_count] for i in range(0, len(list_), thread_count)]
            result = []
            for base_info in base_info_lists:
                base_info_list = thread_pool(base_info, func=func)
                result += base_info_list
    return result


def thread_pool(list_, *, func=None):
    result = []
    if func and list_:
        with ThreadPoolExecutor(max_workers=len(list_)) as get_pool:
            get_pool.map(func, list_)
            # for link in list():
            #     result += link
    return result


async def run(words):
    for url in words:
        # url = "http://dict.youdao.com/w/eng/{}/".format(word)
        # url = "http://www.sina.com.cn"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                res = await response.text(encoding='utf-8')
                # doc = pq(res)
                # pros = ''
                # for pro in doc.items('.baav .pronounce'):
                #     pros += pro.text()
                #
                # description = ''
                # for li in doc.items('#phrsListTab .trans-container ul li'):
                #     description += li.text()
                # tuple_ = ({'word': word, '音标': pros, '注释': description})
                print("okey")
    # return result


def aps(subwords):
    tasks = []
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    tasks.append(asyncio.ensure_future(run(subwords)))
    # loop = asyncio.set_event_loop(loop)  # 步骤2
    loop.run_until_complete(asyncio.wait(tasks))  # 步骤3


def asynchronous(words):
    now = lambda: time.time()
    start = now()
    print('begin')
    chunks = lambda seq, size: [seq[i: i + size] for i in range(0, len(seq), size)]
    list_ = chunks(words, 3)
    control_thread(list_, func=aps, thread_count=20)
    print("time： %s 秒" % str(now() - start))

# all_url = ["http://www.sina.com.cn" for _ in range(12)]

# asynchronous(all_url)
