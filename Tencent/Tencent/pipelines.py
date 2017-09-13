# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class TencentPipeline(object):
    def __init__(self):
        """打开一个写的文件"""
        self.f = open("tencent.json", "w")

    def process_item(self, item, spider):
        """处理爬虫类传递过来的item对象"""
        result = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.f.write(result)
        return item

    def close_spider(self, spider):
        """关闭文件"""
        self.f.close()
