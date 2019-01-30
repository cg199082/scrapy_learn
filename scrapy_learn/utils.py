import time
import math

#中文日期解析
def parseDate(date):
    timeStruct = time.strptime(date, "%Y年%m月%d日")
    strTime = time.strftime("%Y-%m-%d", timeStruct)
    return strTime
#普通字符串截取
def strTrans(str, target):
    index = str.index(target)
    return str[0:index]

#两位小数点数据升级int
def intTrans(str, target):
    if len(target) >0:
        str = strTrans(str, target)
    orign = float(str) * 100
    return math.ceil(orign)
