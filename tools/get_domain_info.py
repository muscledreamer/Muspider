# -*- coding: utf-8 -*-
# @Email    : jqian_bo@163.com
# @Author  : bojingqian
from tld import get_tld
from factory.Redis import RedisClient
from conf import NEWS_DOMAIN, SD_DOMAIN, JW_DOMAIN, BBS_DOMAIN, BBS_DOMAIN_NAME, All_news_info, Gundong_news_info, \
    Add_Jw_A_info, Add_Sd_A_info


# 获取网站域名与首页地址对应关系
def get_domain(hget_name): return {k.decode(): v.decode() for k, v in RedisClient.redis.hgetall(hget_name).items()}


# 获取论坛域名与论坛名对应关系
def get_bbs_name(domian=BBS_DOMAIN_NAME): return {k.decode(): v.decode() for k, v in
                                                  RedisClient.redis.hgetall(domian).items()}


# 获取URL域名
def get_url_domain(url):
    try:
        url_domain = get_tld(url)
    except Exception as e:
        url_domain = ""
    return url_domain


def get_base_list():
    result_list = set()
    for key in [All_news_info, Gundong_news_info, Add_Jw_A_info, Add_Sd_A_info]:
        # result_list += [i.decode() for i in RedisClass().hgetall(key).keys()]
        [result_list.add(i.decode()) for i in RedisClient.redis.hgetall(key).keys()]
    return result_list


domain_info = {
    "news": get_domain(NEWS_DOMAIN),
    "sd": get_domain(SD_DOMAIN),
    "jw": get_domain(JW_DOMAIN),
    "bbs": get_domain(BBS_DOMAIN),
    "bbs_name": get_bbs_name()
}

base_url_list = get_base_list()
# for kind_name, dic in domain_info.items():
#     if kind_name != "bbs_name":
#         for _, url in dic.items():
#             base_url_list.append(url)
#
if __name__ == "__main__":
    a = get_base_list()
    print(a)
