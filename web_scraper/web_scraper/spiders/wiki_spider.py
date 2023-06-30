```python
import scrapy
from web_scraper.items import AreaCodeItem

class WikiSpider(scrapy.Spider):
    name = "wiki_spider"
    start_urls = ['https://en.wikipedia.org/wiki/List_of_area_codes']

    def parse(self, response):
        for row in response.css('table.wikitable tr'):
            item = AreaCodeItem()
            item['area_code'] = row.css('td::text').extract_first()
            item['place'] = row.css('td a::text').extract_first()
            yield item

        next_page = response.css('a.next::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
```