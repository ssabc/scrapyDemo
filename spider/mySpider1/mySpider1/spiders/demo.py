import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['demo.cn']
    start_urls = ['http://demo.cn/']

    def parse(self, response):
        pass
