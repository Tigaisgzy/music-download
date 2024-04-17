import requests
import time
import execjs
import re


# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 17/4/2024 下午1:15
# @Author : G5116
class get:
    def __init__(self, uin, qm_keyst):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
        }
        self.cookies = {
            'uin': str(uin),
            'qm_keyst': qm_keyst,
        }

    def get_purl(self, song_mid, song_id, uin):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
        }
        cookies = {
            'uin': str(uin),
            'qm_keyst': 'Q_H_L_63k3NxNUv0FEXWWNggRDl_uYTIEneal5m4wM3uHGqksc-UGZRg9bbpCD7aYcXpNwQUJJRYOgO1bMSC7o',
        }
        album_mid = "000I5jJB3blWeN"
        with open('guid.js', 'r', encoding='utf-8') as f:
            js = f.read()

        guid = execjs.compile(js).call('f')
        data = f'{{"comm":{{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":{uin},"g_tk_new_20200303":196929301,"g_tk":196929301}},"req_1":{{"module":"music.musicasset.SongFavRead","method":"IsSongFanByMid","param":{{"v_songMid":["{song_mid}"]}}}},"req_2":{{"module":"music.musichallSong.PlayLyricInfo","method":"GetPlayLyricInfo","param":{{"songMID":"{song_mid}","songID":{song_id}}}}},"req_3":{{"method":"GetCommentCount","module":"music.globalComment.GlobalCommentRead","param":{{"request_list":[{{"biz_type":1,"biz_id":"{song_id}","biz_sub_type":0}}]}}}},"req_4":{{"module":"music.musichallAlbum.AlbumInfoServer","method":"GetAlbumDetail","param":{{"`albumMid`":"{album_mid}"}}}},"req_5":{{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{{"guid":"{guid}","songmid":["{song_mid}"],"songtype":[0],"uin":"{uin}","loginflag":1,"platform":"20"}}}},"req_6":{{"module":"music.trackInfo.UniformRuleCtrl","method":"CgiGetTrackInfo","param":{{"ids":[{song_id}],"types":[0]}}}}}}'

        current_time = int(time.time() * 1000)
        with open('./sign.js', 'r', encoding='utf-8') as f:
            js = f.read()
        sign = execjs.compile(js).call('main', data)
        params = {
            '_': str(current_time),
            'sign': str(sign),
        }
        response2 = requests.post('https://u6.y.qq.com/cgi-bin/musics.fcg', params=params, cookies=cookies,
                                  headers=headers,
                                  data=data).text

        purl = re.search(r'"purl":"(.*?)"', response2, re.DOTALL).group(1).encode('utf-8').decode('unicode_escape')
        return purl
