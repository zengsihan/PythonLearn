# -*- coding: utf-8 -*-
# By zsh
# 网易云音乐 歌单下载
# 获取歌单的ID，保存到一个文件里。

from bs4 import BeautifulSoup
import urllib.request
import urllib
import os



#解析音乐列表网页
def parsehtmlMusicList(html):
    soup = BeautifulSoup(html, 'lxml')
    list_nameUrl = soup.select('ul#m-pl-container li div a.msk')
    list_num = soup.select('div.bottom span.nb')
    n = 0
    length = len(list_nameUrl)
    while n < length:
        f=open(filename,'a') # 以追加模式打开文件，不存在则创建。
        f.write('歌单地址：'+list_nameUrl[n]['href']+'\n')
        print('歌单名称：'+list_nameUrl[n]['title']+'\n歌单地址：'+list_nameUrl[n]['href']+'\n')
        # print('歌单播放量：'+list_num[n].text+'\n\n')
        n += 1

# 获取网页
def gethtml(url, headers={}):
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    content = response.read().decode('utf-8')
    response.close()
    return content

#创建新文件
def file_create():
    oldPath = os.getcwd()  # 获取当前文件所在文件夹的路径
    filename =oldPath+'\歌单.txt'  # 定义文件的名字
    # os.mknod("test.txt") # 创建空文件，这个方法在windoes下面运行报错。
    f = open(filename,'w') # 以写方式打开文件，存在则清空，不存在则创建。
    f.close()              # 关闭文件
    print("文件创建成功！\n")
    return filename

filename=file_create()
url = 'http://music.163.com/discover/playlist'
gethtml(url, headers={
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'music.163.com'
})

url = 'http://music.163.com/discover/playlist'
url = gethtml(url, headers={
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'music.163.com'
})

parsehtmlMusicList(url)








