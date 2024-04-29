#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 29/4/2024 下午6:54
# @Author : G5116
from netease_music_get_url import *
from netease_music_search import *

if __name__ == '__main__':
    MUSIC_U = ''  # cookie 里面的 MUSIC_U
    csrf_token = ''  # cookie 里面的 __csrf
    search = netease_musicSearch(MUSIC_U, csrf_token)
    get_url = NeteaseMusicGetUrl(MUSIC_U, csrf_token)
    # 搜索结果 默认三十条
    name = input("请输入要搜索的歌曲名或者歌手名：")
    songs_list = search.search(name)
    for song in songs_list:
        print(song['name'] + "---" + song['singer'] + "---" + str(song['id']))
    # 通过歌曲id获取歌曲url
    music_url = get_url.get_url(int(input("请输入要下载的歌曲id：")))
    print(music_url)
