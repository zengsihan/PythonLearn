# -*- coding: utf-8 -*-
import scrapy #创建一个爬虫必须继承的类

"""
    先使用 scrapy startproject WangyiMusic 创建项目
    项目结构文件说明：
        scrapy.cfg          项目的配置文件
        tutorial/           项目名字
            __init__.py     
            items.py        项目中的item文件
            pipelines.py    项目中的管道文件
            settings.py     项目中的设置文件
            spiders/        项目的爬虫文件
                __init__.py
                ...
    
    再创建 music.py 来爬网易云音乐
    20170428 zsh
"""

class MusicSpider(scrapy.Spider):
    name="music" #用于区别Spider（爬虫），名字必须唯一。
    allowed_domains=["163.com"] #目标站点
    start_url=["http://music.163.com"] #spider在启动时爬取的url列表

    def parse(self, response): #用于解析返回的数据，生成item以及下一步处理的url
        pass