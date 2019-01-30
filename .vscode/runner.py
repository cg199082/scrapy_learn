from scrapy.cmdline import execute

try:
    execute(
        [
            'scrapy',
            'crawl',
            'ttFundSpider',
            '-o',
            'out.json'
        ]
    )
except SystemExit:
    pass