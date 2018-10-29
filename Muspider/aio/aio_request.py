# -*- coding: utf-8 -*-
# @Email: jqian_bo@163.com
# @Author: JingQian Bo
# @Create Time: 2018/9/11-上午11:16
import time
import asyncio
import aiohttp
from factory.common_tool import decode_content, check_file
from aio import *

headers = dict()
headers[
    "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36"


# rds = RdsConnection().redis


async def run(url_for_thread):
    result = []
    for url_for_asyncio in url_for_thread:
        async with aiohttp.ClientSession() as session:
            async with session.get(url_for_asyncio, headers=headers) as response:
                res = await response.read()
                data = {"url": url_for_asyncio, "text": res}
                result.append(data)
                # content = decode_content(res)
                # fdfs = FastDFS()
                # news_code = check_file(content)
                # url_fdfs_pwd = fdfs.saveBuffer(news_code.encode(), "html")
                # rds.rpush(BJ_dfs_test, url_fdfs_pwd)
    return result

    # return result


def aps(url_for_thread):
    tasks = []
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    tasks.append(asyncio.ensure_future(run(url_for_thread)))
    # loop = asyncio.set_event_loop(loop)  # 步骤2
    loop.run_until_complete(asyncio.wait(tasks))  # 步骤3
    result = tasks[0].result() if tasks else []
    return result


def save_fdfs(base_data):
    html_text = base_data["text"]
    content = decode_content(html_text)
    # content = html_text.decode()
    return content


def asynchronous(urls):
    now = lambda: time.time()
    start = now()
    chunks = lambda seq, size: [seq[i: i + size] for i in range(0, len(seq), size)]
    url_for_thread = chunks(urls, 3)
    print('begin')
    base_data_list = control_thread(url_for_thread, func=aps, thread_count=20)
    print("time： %s 秒" % str(now() - start))

    data_list = control_process(base_data_list, func=save_fdfs, process_count=20)

    # print("time： %s 秒" % str(now() - start))
    # control_process(url_for_thread, func=aps, process_count=5)
    # aps(all_url)
    print("time： %s 秒" % str(now() - start))


all_url = ["http://www.sina.com.cn" for _ in range(100)]
asynchronous(all_url)
