# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class GizmodoItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    thumbnail = scrapy.Field()
    content = scrapy.Field()
    category = scrapy.Field()
    author = scrapy.Field()
    link = scrapy.Field()
    publishedAt = scrapy.Field()
class AhrefItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    category = scrapy.Field()
    author = scrapy.Field()
    link = scrapy.Field()
    author_avatar = scrapy.Field()
    publishedAt = scrapy.Field()

class BBC_NEWS_ITEM(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    content = scrapy.Field()
    category = scrapy.Field()
    thumbnail = scrapy.Field()
    link = scrapy.Field()
    publishedAt = scrapy.Field()


# title 
# description
# thumbnail  
# source 
# content 
# category 
# link 
# author
    # author_name 
    # author_avatar
# publishedAt
 