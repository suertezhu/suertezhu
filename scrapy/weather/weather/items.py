# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    county = scrapy.Field() # 县/区
    weather_day = scrapy.Field() # 白天天气
    wind_day = scrapy.Field() # 白天风向
    temperate_max = scrapy.Field() # 最高温度
    weather_night = scrapy.Field() # 夜间天气
    wind_night = scrapy.Field() # 夜间风向
    temperate_min = scrapy.Field() # 最低温度








