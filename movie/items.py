# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movieTitle = scrapy.Field()
    link = scrapy.Field()
    alterName = scrapy.Field()
    playable = scrapy.Field()
    desc = scrapy.Field()
    star = scrapy.Field()
    starNum = scrapy.Field()
    quote = scrapy.Field()
