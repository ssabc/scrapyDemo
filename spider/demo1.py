import scrapy


class Demo1Spider(scrapy.Spider):
    name = 'demo1'
    allowed_domains = ['demo1.cn']
    start_urls = ['http://demo1.cn/']

    def parse(self, response):
        pass
