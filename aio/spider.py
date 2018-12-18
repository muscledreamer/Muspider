# -*- coding: utf-8 -*-
# @Email: jqian_bo@163.com
# @Author: JingQian Bo
# @Create Time: 2018/10/24-3:08 PM
import time
import logging
import requests
import random
import asyncio
import aiohttp
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# import socket  # together with your other imports
#
# conn = aiohttp.TCPConnector(
#     family=socket.AF_INET,
#     verify_ssl=False,
# )

import platform

if platform.system() != "Windows":
    import uvloop

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


def group(start_urls, size):
    return [start_urls[i: i + size] for i in range(0, len(start_urls), size)]


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
            result_ = get_pool.map(func, list_)
            for link in result_:
                result += link
    return result


def control_process(list_, *, func=None, process_count=5):
    result = []
    if func and list_:
        if len(list_) < process_count:
            result = process_pool(list_, func=func)
        else:
            base_info_lists = [list_[i:i + process_count] for i in range(0, len(list_), process_count)]
            result = []
            for base_info in base_info_lists:
                base_info_list = process_pool(base_info, func=func)
                result += base_info_list
    return result


def process_pool(list_, *, func=None):
    result = []
    if list_ and func:
        with ProcessPoolExecutor(max_workers=len(list_)) as p_pool:
            result_ = p_pool.map(func, list_)
            for link in result_:
                result += link

            # result_ = p_pool.map(func, list_)
            # for link in result_:
            #     result.append(link)
    return result


class Spider(object):
    def __init__(self, *, yield_count=10, headers=None, cookies=None,
                 proxy=None, special_status=False, log=None):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36"} \
            if not headers else headers
        self.yield_count = yield_count
        self.cookies = cookies if cookies else {}
        self.proxy = proxy
        self._status = special_status
        self.log = log if log else logging
        self.requests_func = lambda url: requests.get(url)

    def aio_spider(self, base_urls):
        if not base_urls:
            return
        else:
            urls = group(base_urls, self.yield_count)
            urls_data = control_thread(urls, func=self.aioaps, thread_count=20)
        return urls_data

    @staticmethod
    def super_requests(func, base_urls):
        import gevent.monkey
        gevent.monkey.patch_all()
        result_ = []
        events = [gevent.spawn(func, url) for url in base_urls]
        wordinfos = gevent.joinall(events)
        for wordinfo in wordinfos:
            # 获取到数据get方法
            result_.append(wordinfo.get())
        return result_

    def aioaps(self, url_for_thread):
        tasks = []
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        tasks.append(asyncio.ensure_future(self.aio_run(url_for_thread)))
        # loop = asyncio.set_event_loop(loop)
        loop.run_until_complete(asyncio.wait(tasks))
        result = tasks[0].result() if tasks else []
        return result

    async def aio_run(self, url_for_thread):
        result = []
        for url_for_asyncio in url_for_thread:
            self.log.info("Crawling --> {}".format(url_for_asyncio))
            async with aiohttp.ClientSession(cookies=self.cookies) as session:
                if self.proxy:
                    async with session.get(url_for_asyncio, headers=self.headers,
                                           proxy=random.choice(self.proxy)) as response:
                        html = await response.read()
                        status = response.status
                        data_url = str(response.url) if self._status else url_for_asyncio
                else:
                    async with session.get(url_for_asyncio, headers=self.headers) as response:
                        html = await response.read()
                        status = response.status
                        data_url = str(response.url) if self._status else url_for_asyncio
                self.log.debug('Crawl Over --> {}:[{}]'.format(response.url, response.status))
                data = {"url": data_url, "status": status, "html": html}
                result.append(data)
        return result

    # return result


if __name__ == '__main__':
    #
    spider = Spider(yield_count=10)
    base_url = ["http://www.baidu.com" for _ in range(1000)]
    r = lambda url: requests.get(url).content
    now = lambda: time.time()
    a = now()
    result = spider.super_requests(r, base_url)
    # result = spider.aio_spider(base_url)
    print(now() - a)
    print(len(result))
