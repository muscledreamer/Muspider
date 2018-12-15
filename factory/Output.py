# -*- coding: utf-8 -*-
# @Email    : jqian_bo@163.com
# @Author  : bojingqian

import logging
from setting import _DEBUG


# 日志系统-可生成指定日志文件


class Logger(object):
    def __init__(self, *, logger_name="Default_log", log_path="demo.log",
                 log_format=1, log_level="DEBUG", console_output=True):
        """Logging Class.
            Args:
                logger_name: 日志名称
                log_path: 日志存放路径
                log_format: 日志格式序号
                log_level: 日志最低级别
                console_output: 是否控制台输出
            """
        format_dict = {
            1: logging.Formatter('%(asctime)s - %(message)s'),
            2: logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
            3: logging.Formatter('%(asctime)s [%(name)s:%(module)s:%(funcName)s:%(lineno)s] %(message)s'),
        }
        logging_level_dict = {
            "DEBUG": logging.DEBUG,
            "INFO": logging.INFO,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
            "CRITICAL": logging.CRITICAL,
        }
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging_level_dict[log_level])
        formatter = format_dict[log_format]

        fh = logging.FileHandler(log_path)
        fh.setLevel(logging_level_dict[log_level])
        fh.setFormatter(formatter)
        if console_output:
            ch = logging.StreamHandler()
            ch.setLevel(logging_level_dict[log_level])
            ch.setFormatter(formatter)
            self.logger.addHandler(ch)
        else:
            ...
        self.logger.addHandler(fh)

    def log(self):
        return self.logger


class PRINT(object):
    def debug(self, info):
        return print("DEBUG: {}".format(info))

    def info(self, info):
        return print("INFO: {}".format(info))

    def warning(self, info):
        return print("WARNING: {}".format(info))

    def error(self, info):
        return print("ERROR: {}".format(info))

    def critical(self, info):
        return print("CRITICAL: {}".format(info))


def output(**parameter):
    if _DEBUG:
        return PRINT()
    else:
        logger = Logger(log_path=parameter["log_path"], log_format=parameter["log_format"],
                        logger_name=parameter["logger_name"], console_output=parameter["console_output"],
                        log_level=parameter["log_level"]).log()
        return logger


if __name__ == "__main__":
    op = output(log_path='demo.log', log_format=3, logger_name="requests_log", console_output=True,
                      log_level="INFO")
    op.warning("asd")
# logger = Logger(log_path='log_requests.txt', log_format=3,
#                 logger_name="requests_log", console_output=True,
#                 log_level="INFO").log()
# logger.debug("debug")
# logger.warning("warning")
# logger.error("error")
