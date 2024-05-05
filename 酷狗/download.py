#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 5/5/2024 下午5:56
# @Author : G5116
import requests
from md5 import md5_encrypt
import time

class Download:
    def __init__(self, dfid, encode_album_audio_id, mid, token, userid):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
        }
        self.appid = 1014  # 固定
        self.clienttime = int(time.time() * 1000)  # 时间戳
        self.clientver = 20000  # 固定
        self.dfid = dfid  # cookie中的kg_dfid 或 dfid
        self.encode_album_audio_id = encode_album_audio_id  # 歌曲id
        self.mid = mid  # cookie中的kg_mid 或 mid
        self.platid = 4  # 固定
        self.srcappid = 2919  # 固定
        self.token = token  # cookie中的t
        self.userid = userid  # cookie中的KugooID
        self.uuid = mid  # cookie中的kg_mid 或 mid
        self.data = f"appid={self.appid}clienttime={self.clienttime}clientver={self.clientver}dfid={self.dfid}encode_album_audio_id={self.encode_album_audio_id}mid={self.mid}platid={self.platid}srcappid={self.srcappid}token={self.token}userid={self.userid}uuid={self.uuid}"

    def get_play_url(self):
        signature = md5_encrypt(self.data)
        params = {
            'srcappid': self.srcappid,
            'clientver': self.clientver,
            'clienttime': str(int(time.time() * 1000)),
            'mid': str(self.mid),
            'uuid': str(self.uuid),
            'dfid': str(self.dfid),
            'appid': str(self.appid),
            'platid': str(self.platid),
            'encode_album_audio_id': self.encode_album_audio_id,
            'token': str(self.token),
            'userid': str(self.userid),
            'signature': signature,
        }
        response = requests.get('https://wwwapi.kugou.com/play/songinfo', params=params, headers=self.headers)
        lyrics = response.json()['data']['lyrics']  # 歌词
        play_url = response.json()['data']['play_url']
        play_backup_url = response.json()['data']['play_backup_url']
        return play_url, play_backup_url, lyrics
