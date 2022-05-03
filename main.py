import scrapy

from myproject.items import MyItem
from scrapy import Request


class MySpider(scrapy.Spider):
    name = 'example.com'
    allowed_domains = ['https://docs.scrapy.org/en/latest/topics/spiders.html']

    def start_requests(self):
        url = 'https://docs.scrapy.org/en/latest/topics/spiders.html'
        yield Request(url, callback=self.parse)

    def parse(self, response):
        for title in response.css('div.mega-title').getall:
            yield title

