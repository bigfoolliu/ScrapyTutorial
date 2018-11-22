# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html


"""
Item 是保存爬取到的数据的容器, 其使用方法和python字典类似,
并且提供了额外保护机制来避免拼写错误导致的未定义字段错误。
"""
import scrapy


class ScrapytutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ItcastItem(scrapy.Item):
    """
    ItcastSpider的管道, 定义需要抓取的结构化数据字段
    """
    name = scrapy.Field()  # 姓名
    level = scrapy.Field()  # 职称
    info = scrapy.Field()  # 介绍
    img = scrapy.Field()  # 头像
