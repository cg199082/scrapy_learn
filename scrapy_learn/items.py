# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseRent(scrapy.Item):
    # 上海各区域小区租房价格
    
    community = scrapy.Field()   #小区
    region = scrapy.Field()   #行政区
    rent = scrapy.Field()  #租金
    ratio = scrapy.Field()  #环比上月

class FundItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    fundCode = scrapy.Field()   #基金代码
    fundName = scrapy.Field()   #基金名称
    fundScale = scrapy.Field()  #基金规模
    fundBegin = scrapy.Field()  #基金成立时间
    fundManager = scrapy.Field()    #基金管理公司
    fundTarget = scrapy.Field() #基金跟踪目标
    fundTrackPrec = scrapy.Field()  #基金跟踪误差


class StockItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    fundCode = scrapy.Field()   #基金代码
    fundName = scrapy.Field()   #基金名称
    fundScale = scrapy.Field()  #基金规模
    fundBegin = scrapy.Field()  #基金成立时间
    fundManager = scrapy.Field()    #基金管理公司
    fundTarget = scrapy.Field() #基金跟踪目标
    fundTrackPrec = scrapy.Field()  #基金跟踪误差
    stockName = scrapy.Field()  #股票名称
    stockCode = scrapy.Field()  #股票代码
    stockCurrPrize = scrapy.Field() #股票最新价
    stockRang = scrapy.Field()  #股票涨跌幅度
    stockPrec = scrapy.Field()  #股票占基金比率
    stockAmount = scrapy.Field()    #持股数量(万股)
    marketVal = scrapy.Field()   #持仓市值（万元）

