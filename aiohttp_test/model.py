import time
import uvloop
import aiohttp
import asyncio
import random
import redis
import rediscluster
from setting import *
from threading import Thread
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


class Spider(object):
    def __init__(self, spider_proxy=False, redis_key=''):
        self.host = REDIS_HOST
        self.port = REDIS_PORT
        self.redis_key = redis_key
        redis_type = rediscluster.StrictRedisCluster if REDIS_CLUSTER else redis.StrictRedis
        self.redis = redis_type(host=self.host, port=self.port, max_connections=32)
        self.pipe = self.redis.pipeline()
        self.spider_proxy = spider_proxy
        self.thread_loop = asyncio.new_event_loop()
        self.t = Thread(target=self.start_loop, args=(self.thread_loop,))
        self.t.setDaemon(True)

    def start_loop(self, loop):
        asyncio.set_event_loop(loop)
        loop.run_forever()

    async def fetch(self, session, url):
        headers = dict()
        headers['User-Agent'] = random.choice(USER_AGENTS)
        if self.spider_proxy:
            async with session.get(url, headers=headers, proxy=random.choice(PROXIES)) as response:
                print('crawl over ', response.url, response.status)
                await response.text()
        else:
            async with session.get(url, headers=headers) as response:
                print('crawl over ', response.url, response.status)
                await response.text()

    async def main(self, url):
        async with aiohttp.ClientSession() as session:
            await self.fetch(session, url)

    def spider_begin(self):
        self.t.start()
        print('thread loop start')
        try:
            while True:
                try:
                    url = self.redis.lpop(self.redis_key).decode()
                except Exception as e:
                    print(e, '---- redis has not url')
                    url = ''
                if url:
                    print('from redis get url ', url)
                    asyncio.run_coroutine_threadsafe(self.main(url), self.thread_loop)
                else:
                    time.sleep(5)
        except Exception as e:
            print(e)
            self.thread_loop.stop()
        finally:
            self.thread_loop.run_until_complete(self.thread_loop.shutdown_asyncgens())
            self.thread_loop.close()


if __name__ == '__main__':
    s = Spider(redis_key='url')
    s.spider_begin()
    # p_num = 4
    # while True:
    #     with ThreadPoolExecutor(max_workers=p_num) as p_pool:
    #         p_pool.submit(s.spider_begin())

