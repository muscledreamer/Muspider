import redis


r = redis.Redis(host='127.0.0.1')
url = 'http://www.dytt8.net/html/gndy/dyzz/list_23_{page_num}.html'


def insert_url():

    for i in range(1, 101):
        r.rpush('url', url.format(page_num=str(i)))


if __name__ == '__main__':
    insert_url()







