# -*- coding: utf-8 -*-
# @Email: jqian_bo@163.com
# @Author: JingQian Bo
# @Create Time: 2018/10/19-9:30 AM

from aio import control_process

kk = "abc"
ll = "dfg"
result = [(kk, ll)]


def common_func(result):
    print(result)
    return result


control_process(result, func=common_func, process_count=1)
