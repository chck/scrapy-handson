# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyCrawlerItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    rate = scrapy.Field()
    review = scrapy.Field()
    nearest_station = scrapy.Field()
    budget_of_dinner = scrapy.Field()
    budget_of_lunch = scrapy.Field()

