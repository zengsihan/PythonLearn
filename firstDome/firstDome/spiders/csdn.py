# !/usr/bin/python
# -*- coding: UTF-8 -*-
import scrapy

from firstDome.items import FirstdomeItem

class CsdnSpider(scrapy.Spider):
    name = "csdn"
    allowed_domains = ["blog.csdn.net"]
    start_urls = ['http://blog.csdn.net/']

    def parse(self, response):
        item = FirstdomeItem()
        item['title'] = response.xpath("//h3[@class='tracking-ad']/a/text()").extract()
        item['detail'] = response.xpath("//div[@class='blog_list_c']/text()").extract()
        item['link'] = response.xpath("//h3[@class='tracking-ad']/a/@href").extract()
        yield item
