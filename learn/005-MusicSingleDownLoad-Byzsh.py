# -*- coding: utf-8 -*-

# 网易云音乐 单首歌曲下载
# By zsh
# Python 3.5




import requests
import urllib.request,urllib.error
import os

link='http://m2.music.126.net/alLDa1rvtYhzTnpJCKN2-Q==/2534374306603713.mp3'
name='1.mp3'
oldPath = os.getcwd()             # 获取当前文件所在文件夹的路径
folderName='歌曲下载'             # 定义文件夹的名字
newFolder = os.path.join(oldPath,folderName) # 准备 “oldPath” 下创建 “folderName” 文件夹

if not os.path.isdir(newFolder):  # 判断是否已存在此文件夹
    os.makedirs(newFolder)        # 创建文件夹

urllib.request.urlretrieve(link, folderName+'\\' + name)  # 提前要创建文件夹，在此文件目录下创建“name”文件







