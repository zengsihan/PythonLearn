# !/usr/bin/python
# -*- coding: UTF-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstdomeItem(scrapy.Item):
    # define the fields for your item here like:
    #  name = scrapy.Field()

    title=scrapy.Field()#??是要取网页title？
    detail=scrapy.Field()
    link=scrapy.Field()
    pass
