# !/usr/bin/python
# -*- coding: UTF-8 -*-

import scrapy

#从核心目录firstdemo定位到items.py文件里的FirstdemoItem函数
from firstDome.items import FirstdomeItem

class BaiduSpider(scrapy.Spider):
    name = "baidu" #爬虫名字
    allowed_domains = ["baidu.com"] #目标站点
    start_urls = ['http://baidu.com/'] #网站

    def parse(self, response): #默认回调函数
        item=FirstdomeItem()
        item['title']=response.xpath('/html/head/title/text()').extract()
        yield item