#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 27/4/2024 上午12:19
# @Author : G5116
import execjs
import json
import requests


class netease_musicSearch:

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
        self.csrf_token = csrf_token

    def search(self, name):
        # 参数
        ilx = {
            "hlpretag": "<span class=\"s-fc7\">",
            "hlposttag": "</span>",
            "s": str(name),
            "type": "1",
            "offset": "0",
            "total": "true",
            "limit": "30",
            "csrf_token": str(self.csrf_token)
        }
        with open('wangyiyun参数加密.js', 'r', encoding='utf-8') as f:
            js = f.read()
        data_dit = execjs.compile(js).call('d', json.dumps(ilx))
        param = data_dit.get('encText')
        encSecKey = data_dit.get('encSecKey')
        data = {
            'params': str(param),
            'encSecKey': str(encSecKey),
        }
        response = requests.post(
            'https://music.163.com/weapi/cloudsearch/get/web',
            params=self.params,
            cookies=self.cookies,
            headers=self.headers,
            data=data,
        )
        songs_json = json.loads(response.text)
        songs_list = songs_json['result']['songs']
        song_info_list = []  # 创建一个空列表用于存储歌曲信息
        for song in songs_list:
            song_id = song['id']
            song_name = song['name']
            singer_name = song['ar'][0]['name']
            # 创建一个字典，包含当前歌曲的标题和歌手名
            song_dict = {
                'name': song_name,
                'singer': singer_name,
                'id': song_id
            }
            # 将字典添加到song_info_list列表中
            song_info_list.append(song_dict)
        return song_info_list
