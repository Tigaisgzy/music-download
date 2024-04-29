#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 27/4/2024 上午12:42
# @Author : G5116
import execjs
import json
import requests


class NeteaseMusicGetUrl:
    def __init__(self, MUSIC_U, csrf_token):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
        }
        self.cookies = {
            'MUSIC_U': str(MUSIC_U),
        }
        self.params = {
            'csrf_token': str(csrf_token),
        }
        self.csrf_token = str(csrf_token)

    def get_url(self, song_id):
        data = {
            "ids": f"[{song_id}]",
            "level": "standard",
            "encodeType": "aac",
            "csrf_token": self.csrf_token
        }
        with open('wangyiyun参数加密.js', 'r', encoding='utf-8') as f:
            js = f.read()
        data_dit = execjs.compile(js).call('d', json.dumps(data))
        param = data_dit.get('encText')
        encSecKey = data_dit.get('encSecKey')
        data = {
            'params': str(param),
            'encSecKey': str(encSecKey),
        }

        response = requests.post(
            'https://music.163.com/weapi/song/enhance/player/url/v1',
            params=self.params,
            cookies=self.cookies,
            headers=self.headers,
            data=data,
        )
        # print(response.text)
        download_url = response.json()['data'][0]['url']
        # print(download_url)
        return download_url
