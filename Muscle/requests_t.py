# -*- coding: utf-8 -*-
# @Email: jqian_bo@163.com
# @Author: JingQian Bo
# @Create Time: 2018/9/6-上午12:19
import requests
from pyquery import PyQuery as pq
import gevent
import time
import gevent.monkey

gevent.monkey.patch_all()
headers = dict()
headers[
    "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36"

words = ['good', 'bad', 'cool',
         'hot', 'nice', 'better',
         'head', 'up', 'down',
         'right', 'left', 'east']


def fetch_word_info(word):
    url = "http://dict.youdao.com/w/eng/{}/".format(word)

    resp = requests.get(url, headers=headers)
    doc = pq(resp.text)

    pros = ''
    for pro in doc.items('.baav .pronounce'):
        pros += pro.text()

    description = ''
    for li in doc.items('#phrsListTab .trans-container ul li'):
        description += li.text()

    return {'word': word, '音标': pros, '注释': description}


def asynchronous(words):
    now = lambda: time.time()
    start = now()
    print('异步开始了')

    chunks = lambda seq, size: [seq[i: i + size] for i in range(0, len(seq), size)]

    for subwords in chunks(words, 3):
        events = [gevent.spawn(fetch_word_info, word) for word in subwords]
        wordinfos = gevent.joinall(events)
        for wordinfo in wordinfos:
            # 获取到数据get方法
            print(wordinfo.get())
        time.sleep(1)
    print("异步运行时间： %s 秒" % str(now() - start))


asynchronous(words)
