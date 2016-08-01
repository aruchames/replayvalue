import scrapy

class MetacriticSpider(scrapy.Spider):
    name = "metacritic"
    allowed_domains = ["metacritic.com"]

    start_urls = [
            "http://www.metacritic.com/music/"
    ]

    def parse(self, response):

