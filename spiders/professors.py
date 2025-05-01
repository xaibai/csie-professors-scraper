import scrapy
from csie_scraper.items import ProfessorItem

class ProfessorsSpider(scrapy.Spider):
    name="professors"
    allowed_domains=["csie.asia.edu.tw"]
    start_urls=["https://csie.asia.edu.tw/zh_tw/associate_professors_2"]
    def parse(self,response):
        blocks=response.css('.i-member-item-inner.clearfix')
        self.logger.info(f"共找到 {len(blocks)} 位教授")
        for block in blocks:
            item=ProfessorItem()
            item['name']=block.css('.i-member-value.member-data-value-name::text').get()
            item['expertise']=block.css('.i-member-value.member-data-value-7::text').get()
            yield item
