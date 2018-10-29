# -*- coding: utf-8 -*-
# @Email: jqian_bo@163.com
# @Author: JingQian Bo
# @Create Time: 2018/9/11-上午11:16
import time
import asyncio
import aiohttp
from factory.fastdfs_factory import FastDFS
from factory.common_tool import decode_content, check_file
from factory.redis_factory import RdsConnection
from conf import BJ_dfs_test
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

headers = dict()
headers[
    "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36"


# rds = RdsConnection().redis


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
                base_info_list = thread_pool(base_info, func=func)
                result += base_info_list
    return result


def process_pool(list_, *, func=None):
    result = []
    if list_ and func:
        with ProcessPoolExecutor(max_workers=len(list_)) as p_pool:
            result_ = p_pool.map(func, list_)
            for link in result_:
                result.append(link)
    return result


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


def asynchronous(all_url):
    now = lambda: time.time()
    start = now()
    chunks = lambda seq, size: [seq[i: i + size] for i in range(0, len(seq), size)]
    url_for_thread = chunks(all_url, 3)
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
