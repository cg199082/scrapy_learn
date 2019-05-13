# -*- coding: utf-8 -*-
import scrapy
from scrapy_learn.items import HouseRent
from scrapy_learn import utils


class HourserentspiderSpider(scrapy.Spider):
    name = 'HourseRentSpider'
    allowed_domains = ['cityhouse.cn']
    start_urls = ['http://sh.cityhouse.cn/ha/list/rentsort.html']

    def parse(self, response):
        #上海2019年4月租房信息
        post_nodes = response.css(".ha_detail_table>tr:not(:first-child)")
        for post_node in post_nodes:
            detail = HouseRent()
            # 初始化模型对象
            detail['community'] = post_node.xpath('td[2]/a/text()').extract_first()
            detail['region'] = post_node.xpath('td[3]/a/text()').extract_first()
            rent = post_node.xpath('td[4]/span/text()').extract_first()
            ratio = post_node.xpath('td[5]/span/text()').extract_first()
            detail['rent'] = utils.intTrans(rent, "")
            detail['ratio'] = utils.intTrans(ratio, "%")

            yield detail
