# -*- coding: utf-8 -*-
import scrapy
from scrapy_learn.items import FundItem
from scrapy_learn.items import StockItem
from scrapy_learn import utils
from scrapy.http.request import Request
from urllib import parse
import copy
import random


class TtfundspiderSpider(scrapy.Spider):
    name = 'ttFundSpider'
    allowed_domains = ['eastmoney.com']
    start_urls = ['http://fund.eastmoney.com/ZS_jzzzl.html#os_1;isall_0;ft_;pt_5']

    #获取基金列表
    def parse(self, response):
        post_nodes = response.css("#oTable>tbody>tr")
        for post_node in post_nodes:
            item = FundItem()
            # 初始化模型对象
            item['fundCode'] = post_node.xpath('./td[@class="bzdm"]/text()').extract_first()
            item['fundName'] = post_node.xpath('./td[@class="tol"]/nobr/a[1]/text()').extract_first()
            post_url = "http://fundf10.eastmoney.com/jbgk_"+ item['fundCode'] + ".html"

            yield Request(url=parse.urljoin(response.url,post_url),meta={"item":item},callback=self.parse_company)
    #获取基金公司相关信息
    def parse_company(self, response):
        item = response.meta.get("item")
        #基金公司相关信息
        post_nodes = response.css(".txt_in .box:nth-child(1) table tr")
        fundBegin = post_nodes[2].xpath('./td[1]/text()').extract_first()
        fundScale = post_nodes[3].xpath('./td[1]/text()').extract_first()
        item['fundManager'] = post_nodes[4].xpath('./td[1]/a/text()').extract_first()

        item['fundBegin'] = utils.parseDate(fundBegin)
        item['fundScale'] = utils.intTrans(fundScale, "亿")
        post_url = "http://fundf10.eastmoney.com/tsdata_"+ item['fundCode'] + ".html"

        yield Request(post_url,meta={"item":item},callback=self.parse_target)

    #获取基金跟踪相关信息
    def parse_target(self, response):
        item = response.meta.get("item")
        #基金公司相关信息
        post_nodes = response.css("#jjzsfj .fxtb tr")
        item['fundTarget'] = post_nodes[1].xpath('./td[1]/text()').extract_first()
        fundTrackPrec = post_nodes[1].xpath('./td[2]/text()').extract_first()


        item['fundTrackPrec'] = utils.intTrans(fundTrackPrec, "%")
        post_url = "http://fundf10.eastmoney.com/FundArchivesDatas.aspx?type=jjcc&code="+ item['fundCode'] + "&topline=10&year=&month=&rt="+ str(random.random())

        yield item
        yield Request(url=parse.urljoin(response.url,post_url),meta={"item":item},callback=self.parse_stock)
    
    #获取基金跟踪股票相关信息
    def parse_stock(self, response):
        item = response.meta.get("item")
        #相关股票信息
        post_nodes = response.css(".box .boxitem .tzxq tbody tr")
        for post_node in post_nodes:
            detail = StockItem()
            detail.update(item)
            # 初始化模型对象
            detail['stockCode'] = post_node.xpath('./td[2]/a/text()').extract_first()
            detail['stockName'] = post_node.xpath('./td[3]/a/text()').extract_first()
            stockPrec = post_node.xpath('./td[last()-2]/text()').extract_first()
            stockAmount = post_node.xpath('./td[last()-1]/text()').extract_first()
            detail['marketVal'] = post_node.xpath('./td[last()]/text()').extract_first()

            detail['stockPrec'] = utils.intTrans(stockPrec, "%")
            detail['stockAmount'] = utils.intTrans(stockAmount, "")


            yield detail