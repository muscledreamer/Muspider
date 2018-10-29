# -*- coding:utf-8 -*-
import os
from fdfs_client.client import *
from conf import FDFS_CLIENT


class FastDfsTask(object):
    def __init__(self):
        self.client = Fdfs_client(FDFS_CLIENT)

    def savefile(self, filepath):
        if os.path.exists(filepath):
            ret0 = self.client.upload_by_filename(filepath)
            if ret0['Status'] == 'Upload successed.':
                remote_file_id = ret0['Remote file_id'].decode()
                return remote_file_id

    def deletefile(self, dfs_name):
        ret1 = self.client.delete_file(dfs_name)
        return ret1

    def saveBuffer(self, buf, ext):
        try:
            ret = self.client.upload_by_buffer(buf, file_ext_name=ext)
            result = self.checkException(ret)
            if not result:
                self.client = Fdfs_client(FDFS_CLIENT)
                ret = self.client.upload_by_buffer(buf, file_ext_name=ext)
                result = self.checkException(ret)
        except Exception as e:
            self.client = Fdfs_client(FDFS_CLIENT)
            ret = self.client.upload_by_buffer(buf, file_ext_name=ext)
            result = self.checkException(ret)
        return result

    def checkException(self, ret):
        try:
            dfsName = ret['Remote file_id'].decode()
            if 'group' in dfsName:
                return dfsName
            else:
                return
        except:
            return


if __name__ == "__main__":
    file_text = b"123"
    fdfs = FastDfsTask()
    a = fdfs.saveBuffer(file_text, "html")
    print(a)
