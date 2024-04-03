import scrapy
from webcrawler.items import BBC_NEWS_ITEM
from scrapy_splash import SplashRequest
class BBCNews(scrapy.Spider):
    name = 'bbc_news'
    allowed_domains = ['bbc.com']
    start_urls = ['https://www.bbc.com']
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})
    def parse(self, response):
        # Define the selectors for the different elements
        posts_selector = '.sc-7d3a85f9-3.iJkJHb, [data-testid="edinburgh-card"], [data-testid="edinburgh-article"]'
        title_selector = 'h2::text'
        category_selector = '[data-testid="card-metadata-tag"]::text'
        link_selector = '[data-testid="internal-link"]::attr(href)'
        description_selector = '[data-testid="card-description"]::text'
        thumbnail_selector = '[data-testid="card-media"] img::attr(srcset)'
        date_selector = '[data-testid="card-metadata-tag"]::text'
        for post in response.css(posts_selector):
            item = BBC_NEWS_ITEM()
            item['title'] = post.css(title_selector).get()
            item['category'] = post.css(category_selector).get()
            item['publishedAt'] = post.css(date_selector).get()
            item['link'] = response.urljoin(post.css(link_selector).get())
            item['description'] = post.css(description_selector).get()
            item['thumbnail'] = post.css(thumbnail_selector).get().split(',')[0]
            yield item

