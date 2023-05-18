import scrapy
from scrapy.http import Request

class SanetSpider(scrapy.Spider):
    name = 'rio'
    allowed_domains = ['raider.io']
    start_urls = ['https://raider.io/mythic-plus-rankings/season-df-2/all/world/leaderboards']

    def parse(self, response):
        yield {
            # parse
            'results': response.xpath('//h3[@class="posts-results"]/text()').extract_first()
        }
        # next_page = /page-{}/ where {} number of page.
        next_page = response.xpath('//a[@data-tip="Next page"]/@href').extract_first()

        # next_page = https://raider.io/mythic-plus-rankings/season-df-2/all/world/leaderboards/{} where {} number of page.
        next_page = response.urljoin(next_page)

        # If next_page have value
        if next_page:
            # Recall parse with url https://raider.io/mythic-plus-rankings/season-df-2/all/world/leaderboards/{} where {} number of page.
            yield scrapy.Request(url=next_page, callback=self.parse)
print(SanetSpider)