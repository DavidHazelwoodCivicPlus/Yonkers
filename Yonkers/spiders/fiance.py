import scrapy


class FianceSpider(scrapy.Spider):
    name = "fiance"
    allowed_domains = ["www.yonkersny.gov"]
    start_urls = ["https://www.yonkersny.gov/government/departments/purchasing/purchasing-faq-s"]

    def parse(self, response):
        headers = response.css('.listfaq_answers ul li')
        for header in headers:
            yield {
                'question' : header.css('h3 ::text').get(),
                'awnser' : header.css('.listfaq_a_right ::text').get()
            }
