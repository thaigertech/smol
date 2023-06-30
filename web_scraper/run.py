from scrapy.crawler import CrawlerProcess
from web_scraper.web_scraper.spiders.wiki_spider import WikiSpider

process = CrawlerProcess(settings={
    'FEED_FORMAT': 'json',
    'FEED_URI': 'result.json'
})

process.crawl(WikiSpider)
process.start()