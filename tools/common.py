# -*- coding: utf-8 -*-
# @Email: jqian_bo@163.com
# @Author: JingQian Bo
# @Create Time: 2018/10/22-3:44 PM
import re
import hashlib
import datetime
import requests
from conf import no_type_list, FDFS_ADDRESS
from urllib.parse import urljoin
from factory.Bloomfilter import BloomFilter
from scrapy import Selector
from tools.get_domain_info import domain_info, get_url_domain
from factory.hbase_factory import InfoHbase


# 解析标题
def get_title(content):
    pattern = re.compile(r'<title[^>]*?>([\s\S]*?)</title>', re.I)
    title = pattern.findall(content)
    if not title:
        pattern = re.compile(r'<h1>([\s\S]*?)</h1>', re.I)
        title = pattern.findall(content)
    return title[0] if title else ''


# 解析页面
def decode_content(html):
    # import cchardet as chardet
    import chardet
    gbk_list = ["gb2312", "GB2312", "GBK", "GB18030"]
    if isinstance(html, bytes):
        char = chardet.detect(html)
        confidence = char['confidence']
        if "encoding" in char and confidence > 0.7:
            items = [char["encoding"]]
        else:
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


# 获取域名、源链接
def get_domain_sourse(url, ty=None):
    news_domain_dict = domain_info[ty]
    request_url_domain = get_url_domain(url)
    if request_url_domain:
        if request_url_domain in news_domain_dict:
            source_url = news_domain_dict[request_url_domain]
        else:
            source_url = url
    else:
        source_url = url
    return request_url_domain, source_url


# 域名拼凑
def deal_url(base, url):
    if url.startswith('javascript'):
        return None
    url = url.split('#')[0]
    if not url.startswith(('http:', 'https:')):
        url = urljoin(base, url)
    return url.strip('/')


# 获取页面链接(限制域名不过滤数据库)
def link_list(url, content, domain, all_links):
    crawl_links = list()
    links = Selector(text=content).xpath('//a[@href]')
    for link in links:
        link = deal_url(url, str(link.re('href="(.*?)"')[0]))
        if link:
            startswith_correction = [link.startswith('http') or link.startswith('https')][0]
            endswith_correction = list(filter(lambda _: _, [link.endswith(__) for __ in no_type_list]))
            domain_correction = True if get_url_domain(link) == domain else False
            check_exists_boo = True if all_links else not check_exists(link)
            if startswith_correction and not endswith_correction and domain_correction and check_exists_boo:
                crawl_links.append(link)
    return crawl_links


# 验证INFO Hbase是否存在此条
def check_exists(url):
    infotable = InfoHbase()
    return infotable.exists(url)


# 自定正则匹配
def re_compile_bj(re_word, re_aim):
    return re.compile(re_word).findall(re_aim)


def replace_charset(file):
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


def fastdfs_check(address):
    try:
        print("{}{}".format(FDFS_ADDRESS, address))
        status_code = requests.get("{}{}".format(FDFS_ADDRESS, address)).status_code
    except Exception as e:
        status_code = 404
    return status_code


def url_boo_hour(url):
    bf_key = "Website:bloom_{}".format(datetime.datetime.now().strftime("%H"))
    return True if BloomFilter(key=bf_key).isContains(url.encode()) else False


def save_url_boo(url):
    bf_key = "Website:bloom_{}".format(datetime.datetime.now().strftime("%H"))
    BloomFilter(key=bf_key).insert(url.encode())


def getmd5_str_boo(check_md5_html, bf_key):
    '''Check same files by Bloomfilter

        :param filename:
        :param bf_key:
        :return:
            boo True 存在
            boo False 不存在
    '''
    bf = BloomFilter(key=bf_key)
    m = hashlib.md5()
    m.update(str(check_md5_html).encode('utf-8'))
    md5 = m.hexdigest()
    md5_en = md5.encode()
    boo = True if bf.isContains(md5_en) else False
    return boo, md5_en


# 计算md5值
def getmd5_str(check_md5_html):
    m = hashlib.md5()
    m.update(str(check_md5_html).encode('utf-8'))
    md5 = m.hexdigest()
    md5_en = md5.encode()
    return md5_en


def save_md5_bf(info, bf_key):
    bf = BloomFilter(key=bf_key)
    bf.insert(info)


if __name__ == '__main__':
    pass