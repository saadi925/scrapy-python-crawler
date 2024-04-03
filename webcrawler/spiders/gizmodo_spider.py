import scrapy
from webcrawler.items import GizmodoItem

class GizmodoSpider(scrapy.Spider):
    name = 'gizmodo'
    allowed_domains = ['gizmodo.com']
    start_urls = ['https://gizmodo.com/']

    def parse(self, response):
        article_selector = 'article.sc-1pw4fyi-6'
        title_selector = 'h4.sc-1qoge05-0::text'
        description_selector = 'p.sc-1d3a351-0::text'
        thumbnail_selector = 'picture.sc-epkw7d-0 img::attr(src)'
        category_selector = 'a.sc-1hjwdsc-0::text,a[data-ga*="Story Type Click"]::text'
        author_selector = 'a.sc-1out364-0[href*="/author/"]::text'
        # Loop through each article on the homepage
        for article in response.css(article_selector):
            item = GizmodoItem()
            item['title'] = article.css(title_selector).get()
            item['description'] = article.css(description_selector).get()
            item['thumbnail'] = article.css(thumbnail_selector).get()
            item['category'] = article.css(category_selector).get()
            item['author'] = article.css(author_selector).get()
            # Extract the link to the full article
            article_url = article.css('a.sc-1out364-0.dPMosf.sc-1pw4fyi-5.bnwMct.js_link::attr(href)').get()
            if article_url is not None:
                yield response.follow(article_url, callback=self.parse_article, meta={'item': item})

    def parse_article(self, response):
        # Retrieve the item passed as meta
        item = response.meta['item']
        content_selector = 'div.sc-xs32fe-0.gKylik.js_post-content p.sc-77igqf-0.fnnahv'
        # Extract content from the full article page
        item['content'] = ' '.join(response.css(content_selector).getall())
        
        yield item
