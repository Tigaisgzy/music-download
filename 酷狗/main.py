#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 5/5/2024 上午12:59
# @Author : G5116
from download import Download
from search import Search

if __name__ == '__main__':
    # 初始变量
    dfid = ''  # cookie中的kg_dfid 或 dfid
    mid = ''  # cookie中的kg_dfid 或 dfid
    token = ''  # cookie中的t
    userid = ''  # cookie中的KugooID

    # 搜索歌曲
    search = Search(dfid=dfid, mid=mid, token=token, userid=userid,
                    name=str(input('请输入搜索内容: ')))
    search.get_songs()

    # 获取歌曲
    encode_album_audio_id = str(input('请输入歌曲的encode_album_audio_id: '))
    get_music = Download(dfid=dfid, encode_album_audio_id=encode_album_audio_id, mid=mid, token=token, userid=userid)
    play_url, play_backup_url, lyrics = get_music.get_play_url()
    print(play_url, play_backup_url, lyrics)
