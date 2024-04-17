#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 17/4/2024 下午1:15
# @Author : G5116


from download import download
from searchSong import Search
from get_purl import get

if __name__ == '__main__':
    print('欢迎使用QQ音乐下载工具')
    uin = ''  # qq号
    qm_keyst = ''  # 从登录cookie中获取 一天有效期
    search = Search(uin=uin, qm_keyst=qm_keyst)
    song_name = input('请输入歌曲名：')
    # 搜索歌曲id与mid
    song_id, song_mid = search.get_song_id_and_mid(song_name=song_name, uin=uin)
    # 获取purl
    get = get(uin=uin, qm_keyst=qm_keyst)
    purl = get.get_purl(song_mid=song_mid, song_id=song_id, uin=uin)
    # 下载
    download = download()
    download.download(song_name, purl)
