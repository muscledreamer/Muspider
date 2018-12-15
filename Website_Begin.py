# -*- coding: utf-8 -*-
# @Email: jqian_bo@163.com
# @Author: JingQian Bo
# @Create Time: 2018/11/6-4:12 PM

import sys
import getopt
from MuException import Error
from conf import Allowed_Spider


if __name__ == '__main__':
    options, _ = getopt.getopt(sys.argv[1:], "N:", ['name='])
    des_job = {'-N': None, '--name': None}
    recv_job = {n: v for n, v in options}
    job = {**des_job, **recv_job}
    spider_name = job['-N'] if job['-N'] else job['--name']
    if spider_name not in Allowed_Spider:
        raise Error(Error.CmdError.format(spider_name=spider_name))
    print(spider_name)
