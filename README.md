# scrapy_learn
scrapy learn with fund.eastmoney.com

编写某个网址的爬虫：
1. 在items.py中创建对应item模型类
2. 在项目根目录下用命令执行创建spider的文件：
> scrapy genspider itcast "itcast.cn"
进入itcast.py文件修改parse()方法
3. 修改piplines.py文件里相关数据保存逻辑

手动开始爬取命令：scrapy crawl HourseRentSpider
debug方式爬取：https://www.cnblogs.com/weixuqin/p/9074448.html

参考文档
Scrapy 入门教程：https://www.runoob.com/w3cnote/scrapy-detail.html

