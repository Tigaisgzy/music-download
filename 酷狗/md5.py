#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 5/5/2024 下午4:52
# @Author : G5116

import hashlib
def md5_encrypt(text):
    u = 'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt'
    text = u + text + u
    # 创建一个 MD5 对象
    md5 = hashlib.md5()

    # 更新 MD5 对象的内容，传入 bytes 类型的字符串
    md5.update(text.encode('utf-8'))

    # 获取 MD5 加密后的结果（32位小写）
    result = md5.hexdigest()

    return result
