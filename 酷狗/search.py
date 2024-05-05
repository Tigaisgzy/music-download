#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 5/5/2024 下午9:04
# @Author : G5116
import json

import requests
import time
from md5 import md5_encrypt
import re


class Search:
    def __init__(self, dfid, mid, token, userid, name):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
        }
        self.appid = 1014  # 固定
        self.clienttime = int(time.time() * 1000)  # 时间戳
        self.clientver = 1000  # 固定
        self.dfid = dfid  # cookie中的kg_dfid 或 dfid
        self.mid = mid  # cookie中的kg_mid 或 mid
        self.platid = 4  # 固定
        self.srcappid = 2919  # 固定
        self.token = token  # cookie中的t
        self.userid = userid  # cookie中的KugooID
        self.uuid = mid  # cookie中的kg_mid 或 mid
        self.name = name  # 搜索内容
        data = [
            f"appid={self.appid}",
            f"bitrate=0",
            f"callback=callback123",
            f"clienttime={int(time.time() * 1000)}",
            f"clientver={self.clientver}",
            f"dfid={self.dfid}",
            f"filter=10",
            f"inputtype=0",
            f"iscorrection=1",
            f"isfuzzy=0",
            f"keyword={self.name}",
            f"mid={self.mid}",
            f"page=1",
            f"pagesize=30",
            f"platform=WebFilter",
            f"privilege_filter=0",
            f"srcappid={self.srcappid}",
            f"token={self.token}",
            f"userid={self.userid}",
            f"uuid={self.uuid}"
        ]
        self.data = "".join(data)

    def get_songs(self):
        signature = md5_encrypt(self.data)
        # print(self.data)
        params = {
            'callback': 'callback123',
            'srcappid': str(self.srcappid),
            'clientver': str(self.clientver),
            'clienttime': str(int(time.time() * 1000)),
            'mid': str(self.mid),
            'uuid': str(self.uuid),
            'dfid': str(self.dfid),
            'keyword': str(self.name),
            'page': '1',
            'pagesize': '30',
            'bitrate': '0',
            'isfuzzy': '0',
            'inputtype': '0',
            'platform': 'WebFilter',
            'userid': str(self.userid),
            'iscorrection': '1',
            'privilege_filter': '0',
            'filter': '10',
            'token': str(self.token),
            'appid': str(self.appid),
            'signature': str(signature),
        }
        response = requests.get('https://complexsearch.kugou.com/v2/search/song', params=params, headers=self.headers)
        data = re.search('callback123\((.*)\)', response.text).group(1)
        json_data = json.loads(data)
        song_list = json_data['data']['lists']
        for song in song_list:
            print(song['FileName'] + ' - ' + song['EMixSongID'])
