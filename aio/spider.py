# -*- coding: utf-8 -*-
# @Email: jqian_bo@163.com
# @Author: JingQian Bo
# @Create Time: 2018/10/24-3:08 PM
import requests
import random
import asyncio
import aiohttp
from conf import Agents, PROXIES_POOL, LOG_PATH_REQUESTS
from setting import YIELD_COUNT
from aio import group, control_thread
from factory.Output import output

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


class Spider(object):
    def __init__(self, *, proxy=None, special_status=False):
        self.proxy = proxy
        self._status = special_status
        self.log = output(log_path=LOG_PATH_REQUESTS, log_format=3, logger_name="requests_log", console_output=True,
                          log_level="INFO")

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
            self.log.info("Crawling --> {}".format(url_for_asyncio))
            async with aiohttp.ClientSession() as session:
                if self.proxy:
                    async with session.get(url_for_asyncio, headers=headers,
                                           proxy=random.choice(self.proxy)) as response:
                        res = await response.read()
                        data_url = str(response.url) if self._status else url_for_asyncio
                else:
                    async with session.get(url_for_asyncio, headers=headers) as response:
                        res = await response.read()
                        data_url = str(response.url) if self._status else url_for_asyncio
                self.log.debug('Crawl Over --> {}:[{}]'.format(response.url, response.status))
                data = {"url": data_url, "html": res}
                result.append(data)
        return result

    # return result
