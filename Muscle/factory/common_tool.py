# -*- coding: utf-8 -*-
# @Email    : jqian_bo@163.com
# @Author  : bojingqian
import re
import time
import chardet
import requests
import datetime
from tld import get_tld
from urllib.parse import urljoin
from bs4 import UnicodeDammit

# 采集通用工具集


# 时间戳获取
def get_timestamp():
    time_format = "%Y-%m-%d %H:%M:%S"
    now_datetime = str(datetime.datetime.now().strftime(time_format))
    now = datetime.datetime.strptime(now_datetime, time_format)
    time_tuple = now.timetuple()
    ntc_now = int(time.mktime(time_tuple))
    return str(ntc_now)


# 域名拼凑
def dealUrl(base, url):
    if url.startswith('javascript'):
        return None
    url = url.split('#')[0]
    if not url.startswith(('http:', 'https:')):
        url = urljoin(base, url)
    return url.strip('/')


# 自定正则匹配
def re_compile_bj(re_word, re_aim):
    re_result_list = re.compile(re_word).findall(re_aim)
    return re_result_list


# 解析页面
def decode_content(html):
    gbk_list = ["gb2312", "GB2312", "GBK"]
    if isinstance(html, bytes):
        # char = chardet.detect(html)
        # confidence = char['confidence']
        # if "encoding" in char and confidence > 0.7:
        #     items = [char["encoding"]]
        # dammit = UnicodeDammit(html)
        # if dammit:
        #     items = dammit
        # else:
        items = re.compile(r'charset=([^\'\"]*?)[\'\"/\s]*?>').findall(str(html))
        if not items:
            items = re.compile(r'charset=[\'\"](.*?)[\'\"]').findall(str(html))
        if not items:
            items = re.compile(r'charset=(.*?)[\'\"]').findall(str(html))
        if items:
            charset = 'gbk' if items[0] in gbk_list else items[0]
            try:
                res = html.decode(charset)
            except Exception as e:
                if charset == 'gbk':
                    try:
                        res = html.decode('gbk', 'ignore')
                    except Exception as e:
                        res = ""
                else:
                    try:
                        res = html.decode('utf-8', 'ignore')
                    except Exception as e:
                        res = ""
        else:
            try:
                res = html.decode('utf-8')
            except Exception as e:
                try:
                    res = html.decode('gbk')
                except Exception as e:
                    try:
                        res = html.decode('utf-8', 'ignore')
                    except Exception as e:
                        res = ""
        return res
    return html


def check_file(file):
    items = re_compile_bj(r'charset=([^\'\"]*?)[\'\"/\s]*?>', str(file))
    if not items:
        items = re_compile_bj(r'charset=[\'\"]*(.*?)[\'\"]', str(file))
    # print('*' * 50, items)
    if items:
        charset = items[0]
        new_file = file.replace(charset, "utf-8")
        return new_file
    else:
        mate_info = '<head> \n<meta charset="utf-8"/>'
        new_file = file.replace("<head>", mate_info)
        return new_file
