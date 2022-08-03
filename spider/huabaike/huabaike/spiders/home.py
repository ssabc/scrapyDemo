'''
Author: zhaoshan
Date: 2022-06-30 17:17:45
LastEditTime: 2022-06-30 17:21:07
LastEditors: zhaoshan
Description: 
'''
import scrapy


class HomeSpider(scrapy.Spider):
    name = 'home'
    allowed_domains = ['huabaike.com']
    start_urls = ['https://www.huabaike.com/jingtian/']

    def parse(self, response):
        for quoteUl in response.css('div.zhiwuImg ul'):
            for quoteli in quoteUl.css('li'):
                yield {
                    'name': quoteli.css('a::text').extract_first(),
                    'img': quoteli.css('a img::attr(src)').extract()[0]
                }