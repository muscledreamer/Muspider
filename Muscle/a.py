# -*- coding: utf-8 -*-
# @Email: jqian_bo@163.com
# @Author: JingQian Bo
# @Create Time: 2018/9/12-上午12:41

import chardet
import requests
from bs4 import UnicodeDammit
import factory


factory.a()
r = requests.get("http://www.sina.com.cn").content
dammit = UnicodeDammit(r)
print(dammit)

# char = chardet.detect(r)
# confidence = char['confidence']
# if "encoding" in char and confidence > 0.7:
#     print(char["encoding"])