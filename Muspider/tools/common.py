# -*- coding: utf-8 -*-
# @Email: jqian_bo@163.com
# @Author: JingQian Bo
# @Create Time: 2018/10/22-3:44 PM
import re


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
