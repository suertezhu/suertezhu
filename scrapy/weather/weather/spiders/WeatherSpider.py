#!/usr/bin/python
# encoding: utf-8
import scrapy
from scrapy.http import Request
from weather.items import WeatherItem


class WeatherSpider(scrapy.Spider):
    name = 'WeatherSpider'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://weather.sina.com.cn/china/']
    provinces = []

    def parse(self, response):
        selector = scrapy.Selector(response)
        for num in selector.xpath('//div[@class="wd_piC"]'):
            for province in num.xpath('a'):
                self.provinces.append(province.xpath('@href').extract()[0])
        yield Request(self.provinces.pop(), callback=self.getCountyWeather)

    def getCountyWeather(self, response):
        item = WeatherItem()
        selector = scrapy.Selector(response)
        for table in selector.xpath('//table[@class="wd_cm_table"]'):
            for each_row in table.xpath('tr'):
                tds = each_row.xpath('td')
                item['county'] = tds[0].xpath('a/text()').extract()[0]
                item['weather_day'] = tds[1].xpath('p/text()').extract()[0]
                item['wind_day'] = tds[2].xpath('text()').extract()[0]
                item['temperate_max'] = tds[3].xpath('text()').extract()[0]
                item['weather_night'] = tds[4].xpath('p/text()').extract()[0]
                item['wind_night'] = tds[5].xpath('text()').extract()[0]
                item['temperate_min'] = tds[6].xpath('text()').extract()[0]
                yield item
        if len(self.provinces) > 0:
            yield Request(self.provinces.pop(), callback=self.getCountyWeather)
        else:
            print 'The Spider Has Finished Its Work! Wish To Meet U Later!'

