'''
Author: zhaoshan
Date: 2022-06-23 11:26:25
LastEditTime: 2022-06-23 13:52:10
LastEditors: zhaoshan
Description: 
'''
import scrapy
import logging


class CaipiaoSpider(scrapy.Spider):
    name = 'caipiao'
    allowed_domains = ['cwl.gov.cn']
    start_urls = ['http://www.cwl.gov.cn/ygkj/wqkjgg/ssq/']

    def parse(self, response):
        for cell in response.css('.ssq table tr'):
            logging.info("=================================")
            logging.info(cell)
            logging.info(response.css('.ssq11 tbody').extract())
            logging.info("=================================")
            yield {
                'date': cell.css('td').extract_first(),
                # 'code': cell.css('.qiu .qiu-item').extract()
            }
