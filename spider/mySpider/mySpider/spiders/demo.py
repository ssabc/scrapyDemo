'''
Author: zhaoshan
Date: 2022-06-29 19:11:37
LastEditTime: 2022-06-29 19:26:04
LastEditors: zhaoshan
Description: 
'''
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['www.huabaike.com']
    start_urls = ['https://www.huabaike.com/jingtian/']

    def parse(self, response):
        for cul in response.css("div.zhiwuImg ul"):
            for cli in cul.css('li'):
                yield {
                    'name': cli.css('a img::attr(title)').extract_first(),
                    'img': cli.css('a img::attr(src)').extract()[0]
                }
