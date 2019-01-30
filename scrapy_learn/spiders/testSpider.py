# -*- coding: utf-8 -*-
import scrapy
from scrapy_learn.items import StockItem
from scrapy.http.request import Request
from scrapy_learn import utils
import random

class TestspiderSpider(scrapy.Spider):
    name = 'testSpider'
    allowed_domains = ['eastmoney.com']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        }

    def start_requests(self):
        #start_url = 'http://fundf10.eastmoney.com/FundArchivesDatas.aspx?type=jjcc&code=160632&topline=10&year=&month=&rt=0.04071620608445459'
        start_url = "http://fundf10.eastmoney.com/FundArchivesDatas.aspx?type=jjcc&code=160632&topline=10&year=&month=&rt="+ str(random.random())
        yield Request(url=start_url, headers=self.headers)

    def parse(self, response):
        #相关股票信息
        post_nodes = response.css(".box .boxitem .tzxq tbody tr")
        for post_node in post_nodes:
            detail = StockItem()
            # 初始化模型对象
            detail['stockCode'] = post_node.xpath('./td[2]/a/text()').extract_first()
            detail['stockName'] = post_node.xpath('./td[3]/a/text()').extract_first()
            stockPrec = post_node.xpath('./td[last()-2]/text()').extract_first()
            stockAmount = post_node.xpath('./td[last()-1]/text()').extract_first()
            detail['marketVal'] = post_node.xpath('./td[last()]/text()').extract_first()

            detail['stockPrec'] = utils.intTrans(stockPrec, "%")
            detail['stockAmount'] = utils.intTrans(stockAmount, "")

            yield detail
