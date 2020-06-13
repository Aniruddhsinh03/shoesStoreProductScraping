# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import json


class ShoesstoreproductscrapingspiderSpider(scrapy.Spider):
    name = 'shoesStoreProductScrapingSpider'
    allowed_domains = ['asos.com']
    start_urls = ['https://www.asos.com/men/shoes-boots-trainers/boots/cat/?cid=5774&nlid=mw%7Cshoes%7Cshop%20by'
                  '%20product&page=1']

    def parse(self, response):
        # Extract shoes urls from page
        shoes_urls = response.xpath('//*[@data-auto-id="productTile"]//a/@href').extract()
        # Extract each of url one by one
        for shoes_url in shoes_urls:
            yield Request(shoes_url, callback=self.parse_product_details)
        # extract next page url load more
        next_page_url = response.xpath('//*[@data-auto-id="loadMoreProducts"]/@href').extract_first()
        if next_page_url:

            yield Request(next_page_url,
                          callback=self.parse)

    # extract product details
    def parse_product_details(self, response):
        product_title = response.xpath('//*[@class ="product-hero"]//h1/text()').extract_first()
        product_id = response.url.split('/prd/')[1].split('?')[0]
        product_price_json_request_url = 'https://www.asos.com/api/product/catalogue/v3/stockprice?productIds=' + product_id + '&store=ROW&currency=EUR'
        product_details = response.xpath('//*[@class ="product-description"]//p/text()')[-1].extract()
        product_code = response.xpath('//*[@class ="product-code"]//p/text()')[-1].extract()
        brand = response.xpath('//*[@class ="brand-description"]//p/text()')[-1].extract()
        look_after_me = response.xpath('//*[@class ="care-info"]//div/text()').extract()
        about_me = response.xpath('//*[@class ="about-me"]//div/text()').extract()
        yield Request(product_price_json_request_url,
                      meta={'product_title': product_title,'product_details': product_details,'product_code': product_code,'brand': brand,'look_after_me': look_after_me,'about_me': about_me},
                      callback=self.parse_product_price)

    # extract product price from json
    def parse_product_price(self, response):
        jsonresponse_from_request = json.loads(response.body.decode('utf-8'))

        product_price = jsonresponse_from_request[0]['productPrice']['current']['text']

        yield {'product_title': response.meta['product_title'],
               'product_details': response.meta['product_details'],
               'product_code': response.meta['product_code'],
               'brand': response.meta['brand'],
               'look_after_me': response.meta['look_after_me'],
               'about_me': response.meta['about_me'],
               'product_price': product_price}
