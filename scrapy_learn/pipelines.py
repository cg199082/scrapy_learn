# -*- coding: utf-8 -*-
import json
from scrapy_learn.items import FundItem
from scrapy_learn.items import StockItem
import pymongo
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyLearnPipeline(object):
    def __init__(self):
        self.fund = open("F:/git-repo/scrapy_learn/scrapy_learn/data/fund.json", "wb")
        self.client = pymongo.MongoClient(host='10.100.97.88', port=27017)
        tdb = self.client['tuandai']
        self.stock = tdb['stock']
    def process_item(self, item, spider):
        if isinstance(item, FundItem):
            text = json.dumps(dict(item), ensure_ascii = False) + ",\n"
            self.fund.write(text.encode("utf-8"))
            return item
        if isinstance(item, StockItem):
            stokInfo = dict(item)
            self.stock.insert(stokInfo)
            return item
    def close_spider(self, spider):
        self.fund.close()
        self.client.close()
        
