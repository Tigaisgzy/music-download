import requests
import time
import execjs


# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 17/4/2024 下午1:15
# @Author : G5116
class Search:
    def __init__(self, uin, qm_keyst):
        self.url = ''
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
        }
        self.cookies = {
            'uin': str(uin),
            'qm_keyst': qm_keyst,

        }

    def get_song_id_and_mid(self, song_name, uin):
        current_time = int(time.time() * 1000)
        data = f'''
        {{
            "comm": {{
                "cv": 4747474,
                "ct": 24,
                "format": "json",
                "inCharset": "utf-8",
                "outCharset": "utf-8",
                "notice": 0,
                "platform": "yqq.json",
                "needNewCode": 1,
                "uin": {str(uin)},
                "g_tk_new_20200303": 196929301,
                "g_tk": 196929301
            }},
            "req_1": {{
                "method": "DoSearchForQQMusicDesktop",
                "module": "music.search.SearchCgiService",
                "param": {{
                    "remoteplace": "txt.yqq.center",
                    "searchid": "55965219239838785",
                    "search_type": 0,
                    "query": "{song_name}",
                    "page_num": 1,
                    "num_per_page": 10
                }}
            }}
        }}
        '''

        with open('./sign.js', 'r', encoding='utf-8') as f:
            js = f.read()
        sign = execjs.compile(js).call('main', data)

        params = {
            '_': str(current_time),
            'sign': str(sign),
        }

        response = requests.post('https://u6.y.qq.com/cgi-bin/musics.fcg', params=params, cookies=self.cookies,
                                 headers=self.headers,
                                 data=data.encode()).json()

        song_id = response['req_1']['data']['body']['song']['list'][0]['id']
        song_mid = response['req_1']['data']['body']['song']['list'][0]['mid']
        return song_id, song_mid
