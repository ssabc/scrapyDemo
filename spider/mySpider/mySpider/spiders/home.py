import scrapy


class HomeSpider(scrapy.Spider):
    name = 'home'
    allowed_domains = ['huabaike.com']
    start_urls = ['http://huabaike.com/']

    def parse(self, response):
        pass
