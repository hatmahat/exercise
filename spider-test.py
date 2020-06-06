import scrapy
from scrapy.crawler import CrawlerProcess

class DCspider(scrapy.Spider):
    name = 'dcspider'

    def start_rquests(self):
        
        urls = ['https://ww.datacamp.com/courses/all']
        for url in urls:
            yield scrapy.Request(
                url=url, callback = self.parse
            )

    def parse(self, response):
        links = response.css('div.course-block > a::attr(href)').extract()
        filepath = 'DC_links.csv'
        with open(filepath, 'w') as f:
            f.writelines([link + '\n' for link in links])