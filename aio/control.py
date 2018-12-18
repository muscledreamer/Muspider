# -*- coding: utf-8 -*-
# @Email: jqian_bo@163.com
# @Author: JingQian Bo
# @Create Time: 2018/10/22-3:34 PM

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


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
                result.append(link)
    return result

