import requests


# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 17/4/2024 下午1:15
# @Author : G5116
class download:
    def download(self, song_name, purl):
        response = requests.get(
            'https://ws6.stream.qqmusic.qq.com/' + purl
        )
        print(response.url)
        with open(song_name + '.mp4', 'wb') as f:
            f.write(response.content)
        if response.status_code == 200:
            print('下载成功')
        else:
            print('下载失败')
