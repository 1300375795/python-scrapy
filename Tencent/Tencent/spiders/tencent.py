# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem
import collections


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    baseUrl = "http://hr.tencent.com/position.php?&start="
    offset = 0
    start_urls = [baseUrl + str(offset)]

    def getOrderedDict(self):
        """得到存放了页面结构信息的有序字典"""
        itemMap = collections.OrderedDict()
        itemMap["positionName"] = "./td[1]/a/text()"
        itemMap["positionLink"] = "./td[1]/a/@href"
        itemMap["positionType"] = "./td[2]/text()"
        itemMap["peopleNumber"] = "./td[3]/text()"
        itemMap["workLocation"] = "./td[4]/text()"
        itemMap["publistTime"] = "./td[5]/text()"
        return itemMap

    def parse(self, response):
        """解析页面"""
        """根据xpath语法得到相应的需要解析的节点列表"""
        nodeList = response.xpath(" //tr[@class='even'] "
                                  " | "
                                  " //tr[@class='odd'] ")

        """得到需要抓取的数据的字段名和相应的xpath路径的有序字典"""
        itemMap = self.getOrderedDict()
        """得到需要抓取的数据的字段名"""
        keys = itemMap.keys()

        """判断是否抓取的数据是否为空(即只抓取到最后一页,最后一页后面的那些都不抓取)"""
        if nodeList:
            """循环遍历全部的节点列表然后得到每一个节点对象列表，再将的第一个对象转换成字符串保存在item中"""
            for node in nodeList:
                item = TencentItem()
                """循环遍历所有的键然后取出这个键所对应的值保存在item中,如果为空的话那么就保存NULL"""
                for key in keys:
                    """具体拥有需要抓取的数据的值的节点集合"""
                    goalNodeList = node.xpath(itemMap.get(key))
                    if goalNodeList:
                        item[key] = goalNodeList.extract()[0].encode("utf-8")
                    else:
                        item[key] = "NULL"

                """交给管道去处理"""
                yield item

            """"下面的这几行代码是通过拼接url的形式发送请求的"""
            # """获取下一页的连接"""
            # self.offset += 10
            # url = self.baseUrl + str(self.offset)
            # yield scrapy.Request(url, callback=self.parse)


            """下面的这几行代码通过点击下一页的形式获取页面数据的"""
            """判断是否存在能点击的下一页的按钮"""
            if not response.xpath("//a[@class='noactive'  and @id='next']"):
                """存在的话那么就得到下一页所对应的url地址"""
                url = response.xpath("//*[@id='next']/@href").extract()[0]
                """将下一页的地址和域名拼接起来,发送请求"""
                yield scrapy.Request("http://hr.tencent.com/" + url, callback=self.parse)
