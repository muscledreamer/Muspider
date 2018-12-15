# 测试采集
class WebsiteDemo(object):
    def __init__(self):
        pass

    def run(self):
        import time
        from aio import Spider
        urls = ['http://www.sina.com.cn' for i in range(100)]
        _ = Spider(proxy=None, special_status=False)
        before_time = time.time()
        result = _.aio_spider(urls)
        print(len(result))
        print(time.time()-before_time)


if __name__ == '__main__':
    wd = WebsiteDemo()
    wd.run()