# -*- coding: utf-8 -*-
# @Email: jqian_bo@163.com
# @Author: JingQian Bo
# @Create Time: 2018/10/24-3:08 PM
import uvloop
import requests
import random
import asyncio
import aiohttp
from conf import Agents, PROXIES_POOL
from setting import YIELD_COUNT
from aio import group, control_thread

# import socket  # together with your other imports
#
# conn = aiohttp.TCPConnector(
#     family=socket.AF_INET,
#     verify_ssl=False,
# )
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


class Spider(object):
    def __init__(self, proxy=False):
        self.proxy = proxy

    def aio_spider(self, base_urls):
        if not base_urls:
            return
        else:
            urls = group(base_urls, YIELD_COUNT)
        urls_data = control_thread(urls, func=self.aps, thread_count=20)
        return urls_data

    def requests_spider(self, base_urls):
        pass

    def aps(self, url_for_thread):
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
            headers = {
                "User-Agent": random.choice(Agents)
            }
            print("Crawling --> {}".format(url_for_asyncio))
            async with aiohttp.ClientSession() as session:
                if self.proxy:
                    async with session.get(url_for_asyncio, headers=headers,
                                           proxy=random.choice(PROXIES_POOL)) as response:
                        res = await response.read()
                else:
                    async with session.get(url_for_asyncio, headers=headers) as response:
                        res = await response.read()
                print('Crawl Over --> {}:[{}]'.format(response.url, response.status))
                data = {"url": url_for_asyncio, "html": res}
                result.append(data)
        return result

    # return result
