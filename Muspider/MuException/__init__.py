# -*- coding: utf-8 -*-
# @Email: jqian_bo@163.com
# @Author: JingQian Bo
# @Create Time: 2018/10/23-10:22 AM


class MuspiderException(Exception):
    """ Base Exception for Muspider """
    pass


class Error(MuspiderException):
    """ Error for Parameter Exception
    _ParameterError_Key: You can see this Friendly Tips when error type for key.
    _ParameterError_Topic: You can see this Friendly Tips when error type for topic.
    _ParameterError_Consumer: You can see this Friendly Tips when use error Parameter to init init_consumer
    """
    ParameterError = "ParameterError- Type(s) for {Class}('{Parameter}'): '{Parameter}' must be {True_type}."
    _ParameterError_Topic = "ParameterError- type(s) for 'topic': must be bytes"
    _ParameterError_Consumer = "ParameterError- type(s) for 'topic': must be bytes; " \
                               "type(s) for 'group_id': must be str; 'offset_type' " \
                               "must be 'LATEST' or 'EARLIEST'"
    pass
