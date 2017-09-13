# -*- coding: utf-8 -*-
import sys
import scrapy
from itcast.items import ItcastItem

reload(sys)
sys.setdefaultencoding("utf-8")


class ItcastdemoSpider(scrapy.Spider):
    name = 'itcastDemo'
    # 下面的这行代码是可选参数，表示爬虫会在这个域名下面进行爬取，其他的域名的不会被爬取
    allowed_domains = ['http://www.itcast.cn']
    # 起始的url地址列表，爬虫执行后第一批请求，将从这个列表获取
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        nodeList = response.xpath("//div[@class='li_txt']")

        # itemList = []
        for node in nodeList:
            # 创建item字段对象，用来存储信息
            item = ItcastItem()

            # 下面的返回的是一个xpath对象列表,所以需要使用extract()方法来将其转换成Unicode字符串
            name = node.xpath("./h3/text()").extract()
            title = node.xpath("./h4/text()").extract()
            info = node.xpath("./p/text()").extract()

            # 存储到item字段对象里面
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]

            # 返回提取的每一个item数据给管道，给管道处理，然后还回来继续执行当前的for循环里面的代码
            yield item
            # itemList.append(item)

            # return itemList
