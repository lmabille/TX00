import scrapy
from scrapy import Request


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        url = "https://www.lemonde.fr/election-presidentielle-2022/"
        # yield Request(url=url, callback=self.parse_main_article)
        yield Request(url=url, callback=self.parse_sub_articles)

    def parse_main_article(self, response):
        main_article = response.css('div.article--main')
        title = main_article.css('p.article__title-label ::text').get()
        link = main_article.css('a ::attr(href)').get()
        article = {}
        article[title] = link
        yield article

    def parse_sub_articles(self, response):
        sub_articles = response.css('section.teaser')
        for sub_article in sub_articles:
            link = sub_article.css('a ::attr(href)').get()
            title = sub_article.css('.teaser__title ::text').get()
            article = {}
            article[title] = link
            yield article


#div[class*='article'] a