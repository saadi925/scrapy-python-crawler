import scrapy
from webcrawler.items import AhrefItem

class AhrefsBlogSpider(scrapy.Spider):
    name = 'ahrefs'
    allowed_domains = ['ahrefs.com']
    start_urls = ['https://ahrefs.com/blog/']
    page = None
    last_page_number = 23
   
    def parse(self, response):
        posts_selector = '.post-holder'
        for post in response.css(posts_selector):
            item = AhrefItem()
            item['category'] = post.css('.post-category a::text').get()
            item['title'] = post.css('h2 a::text, h3 a::text').get()
            author_avatar_url = post.css('.post-author-avatar img::attr(src)').get()
            if author_avatar_url and author_avatar_url.startswith('//'):
             author_avatar_url = 'https:' + author_avatar_url
            item['author_avatar'] = author_avatar_url
            item['publishedAt'] = post.css('.post-date::text').get()
            item['link'] = post.css('h2 a::attr(href), h3 a::attr(href)').get()

            # Follow the link to the full article to scrape the content
            request = response.follow(item['link'], callback=self.parse_article)
            request.meta['item'] = item
            yield request
    # Pagination handling
        if self.page is None :
           self.page = 1
        else :
           current_page_number = response.css('.wp-pagenavi .current::text').get()
           self.page = current_page_number
        next_page_number = int(self.page) + 1
        next_page_url = f'https://ahrefs.com/blog/archive/page/{next_page_number}/'
        # # Check if the next page exists by comparing it with the last page number in the pagination
         
        if next_page_number <= self.last_page_number:
         yield response.follow(next_page_url, callback=self.parse)
        else:
         self.log('Reached the last page.')
    def parse_article(self, response):
        item = response.meta['item']
        item['content'] = response.css('.post-content').getall()
        yield item
