# -*- coding: utf-8 -*-
# @Email: jqian_bo@163.com
# @Author: JingQian Bo
# @Create Time: 2018/11/8-10:20 AM
import time
from conf import *
from tools.common import *
from pipelines.pipeline import PipeBase
from factory.Redis import RedisClient
from factory.FastDFS import FastDFSClient


class PipeWebCommon(PipeBase):
    def __init__(self, web_type, links_go, all_link, items_func=None):
        super(PipeWebCommon, self).__init__()
        self.FastDFS = FastDFSClient
        self.ty = web_type
        self.links_go = links_go
        self.all_link = all_link
        self.items_func = items_func

    def pipe_up_dfs(self, content):
        url_fdfs_pwd = self.FastDFS.save_buffer(content.encode(), "html")
        return url_fdfs_pwd

    def common_func(self, result):
        pipe = RedisClient.pipe
        items = {}
        html = result["html"]
        content = super().pipe_decode_content(html)
        title = super().pipe_get_title(content)
        if len(content) >= 200 and len(title) >= 5:
            url = super().pipe_url_correction(result["url"])
            domain, source_url = get_domain_sourse(url, ty=self.ty)
            if self.links_go and domain:
                links = link_list(url, content, domain, self.all_link)
            else:
                links = []
            streaming = not check_exists(url)
            if streaming:
                spider_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                update_content = replace_charset(content)
                news_md5 = getmd5_str(url)
                address = self.pipe_up_dfs(update_content)
                while True:
                    time.sleep(1)
                    fastdfs_status = fastdfs_check(address)
                    if fastdfs_status != 200:
                        # print("error")
                        address = self.pipe_up_dfs(update_content)
                    else:
                        break
                if self.ty == "news":
                    items["news_boo"] = 1
                items["address"] = address
                items["updatetime"] = spider_time
                items["news_url"] = url
                items["website_url"] = source_url
                items["FDFS_address"] = FDFS_ADDRESS
                items["news_update"] = 1
                items["news_md5"] = news_md5
                items["check_fdfs"] = False
                if self.items_func:
                    items.update(self.items_func())
                if self.links_go:
                    [pipe.rpush(self.links_go, link) for link in links]
                if self.ty == "news_one":
                    pipe.rpush("NewsOne:Data_Streaming", items)
                elif self.ty == "news":
                    pipe.rpush("News:Data_Streaming", items)
                elif self.ty == "abroad_one":
                    pipe.rpush("JwOne:Data_Streaming", items)
                elif self.ty == "abroad":
                    pipe.rpush("Jw:Data_Streaming", items)
                elif self.ty == "sd_one":
                    pipe.rpush("SdOne:Data_Streaming", items)
                elif self.ty == "sd":
                    pipe.rpush("Sd:Data_Streaming", items)
            else:
                if "news" in self.ty:
                    pipe.incr(NEWS_DAY_NOCHANGE_COUNT, 1)
                elif "abroad" in self.ty:
                    pipe.incr(JW_DAY_NOCHANGE_COUNT, 1)
                elif "sd" in self.ty:
                    pipe.incr(SD_DAY_NOCHANGE_COUNT, 1)
            pipe.execute()

        return items
