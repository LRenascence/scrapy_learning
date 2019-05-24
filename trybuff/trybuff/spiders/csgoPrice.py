import scrapy
import re

class PriceSpider(scrapy.Spider):
    name = "csgoPrice"

    # start urls is the first page
    start_urls = ['https://www.igxe.cn/csgo/730?is_buying=0&is_stattrak%5B%5D=0&is_stattrak%5B%5D=0&price_from=50&price_to=300&sort=0&'
                  'ctg_id=0&type_id=0&page_no=1&page_size=20&rarity_id=0&exterior_id=0&quality_id=0&capsule_id=0&_t=1558656052321']


    def parse(self, response):
        # add next page to url list

        page = response.css("div.mod-pagination")
        nextPage = page.xpath('//a[contains(@class,"next")]/@page_no').getall()
        if nextPage:
            curUrl = response.url
            curPage = re.findall('page_no=\d+',curUrl)
            newPage = 'page_no=' + nextPage[0]
            newUrl = curUrl.replace(curPage[0], newPage)
            yield response.follow(newUrl, self.parse)

        # add price detailed page to list
        for href in response.xpath('//a[contains(@href, "product")]/@href').getall():
            yield response.follow(href, self.price_parse)

    def price_parse(self, response):
        # only crawl stock >= 10
        stock = response.css('div.stock::text')[1].get()
        stockNum = int(re.findall('\d+', stock)[0])
        if stockNum >= 10:

            # get the name div
            nameDiv = response.css('div.txt')[0]
            # get the steam price
            steamPriceDiv = response.css('div.proposedPrice')[0]
            # get the price
            priceDiv = response.css('div.averagePrice')
            yield {
                'name':  nameDiv.css("div.name::text").get(),
                'steamPrice': steamPriceDiv.css("span.c-4::text").get(),
                'Price': priceDiv.css("span.c-4::text").get()
            }