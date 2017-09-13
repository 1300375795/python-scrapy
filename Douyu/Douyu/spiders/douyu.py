# -*- coding: utf-8 -*-
import scrapy
import json
from Douyu.items import DouyuItem


class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['douyucdn.cn']
    baseUrl = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    offset = 0
    start_urls = [baseUrl + str(offset)]

    def parse(self, response):
        result = json.loads(response.body)
        dataList = result.get("data")
        if dataList:
            for data in dataList:
                item = DouyuItem()
                item["nickname"] = data.get("nickname")
                item["imageLink"] = data.get("vertical_src")
                yield item

            self.offset += 20
            url = self.baseUrl + str(self.offset)
            yield scrapy.Request(url, callback=self.parse)
