# -*- coding: utf-8 -*-

# 网易云音乐 歌单的歌曲下载
# By zsh
# Python 3.5

# 使用方法：
# 0.有 Python的环境。
# 1.在网页版网易云音乐上选一个歌单，在 url 上找到ID，
# 2.修改代码中的 id，
# 3.运行程序即可。
# 4.会在代码的同级目录下生成一个“folderName”文件夹，下载的歌曲就在里面。
# 5.付费歌曲则跳过。


import requests
import urllib.request,urllib.error
import os

id="640006772" # 歌单的ID
r = requests.get('http://music.163.com/api/playlist/detail?id='+id) # 去请求数据，返回 json 数据

arr = r.json()['result']['tracks']      # 歌曲的信息在 /result/tracks 中
num= r.json()['result']['trackCount']   # 要下载歌单中的歌曲数，下载是从第一首开始的。trackCount 是此歌单的歌曲数量
songListName=r.json()['result']['name']  # 歌单的名字

oldPath = os.getcwd()             # 获取当前文件所在文件夹的路径
folderName='歌单'+id              # 定义文件夹的名字
newFolder = os.path.join(oldPath,folderName) # 准备 “oldPath” 下创建 “folderName” 文件夹

if not os.path.isdir(newFolder):  # 判断是否已存在此文件夹
    os.makedirs(newFolder)        # 创建文件夹

number=0 # 用来计算有多少首歌曲不能下载
print('开始下载歌单，一共 '+str(num)+' 首歌曲。')

for i in range(num): # 默认下载整个歌单，也可以设置下载的个数，不能超过歌单的歌曲数量
    name = arr[i]['name'] + '.mp3' # 歌曲名字
    # name = str(i + 1) + ' ' + arr[i]['name'] + '.mp3'
    link = arr[i]['mp3Url'] # 歌曲的下载链接

    try:
        if link is None:
            print("没有mp3Url")
            number += 1
            continue
        else:
            response=urllib.request.urlopen(link) # 去加载歌曲下载的连接，得到返回的数据
    except urllib.error.HTTPError as e: # 异常处理
        if e.code != 200: # 404之类的
            number+=1
            print(name + ' 限制免费下载')
    except urllib.error.URLError as e:
        print("URLError")
    else:
        urllib.request.urlretrieve(link, folderName+'\\' + name)  # 提前要创建文件夹，在此文件目录下创建“name”文件
        print(name + ' 下载完成')
num=num-number
print('歌单 【'+songListName+'】 已下载完了,一共下载了 '+str(num)+' 首歌曲。 '+str(number)+' 首歌曲限制免费下载。')














