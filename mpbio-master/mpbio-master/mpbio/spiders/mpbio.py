from scrapy import Request
import json
import csv
import scrapy


class MpbioSpider(scrapy.Spider):
    name = "mpbio"
    allowed_domains=['mpbio.com']
    start_urls = ['https://www.mpbio.com/us/life-sciences/']
    # def start_requests(self):
    #     urls = ['https://www.mpbio.com/us/life-sciences'
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]

        print(response)
        li_div_elements=response.css('.main_ul')
        for li_div in li_div_elements:
            print(li_div)
            lis_element=li_div.css('ul li')
            for li in lis_element:
                req_url=li.css('a::attr(href)').get()
                yield scrapy.Request(url='https://www.mpbio.com//'+req_url, callback=self.parse_next)


    def parse_next(self,response):
        print(response)
        sub_categories_elements=response.css('.blue_bg')
        for sub_category in sub_categories_elements:
            next_url=sub_category.css('a::attr(href)').get()
            yield scrapy.Request(url=next_url, callback=self.parse_products)





    def parse_products(self,response):
        url = "https://hwo0nunfkk-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20" \
              "JavaScript%20(3.35.1)%3B%20Browser%3B%20instantsearch.js%20(4.15.0)%3B%20Magento2%20integ" \
              "ration%20(3.1.0)%3B%20JS%20Helper%20(3.4.4)&" \
              "x-algolia-application-id=HWO0NUNFKK&x-algolia-api-key=MjEwNzc3YjI4Yjk5OWY1" \
              "NTY4NzI3NjY0MjUyZjVmNWI1YzZjMWNkOWIzNDA0NDc2YTZlYzY4NDEyMmViMzk1N3RhZ0ZpbHRlcnM9"
        yield Request.from_curl(url= self.url  ,callback=self.parse)

        #print(response)
        #products_elements= Request.from_curl('.ais-InfiniteHits-list')
        #for product in products_elements:
           # print(product)

