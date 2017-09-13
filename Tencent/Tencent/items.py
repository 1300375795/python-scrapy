# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # 职位名称
    positionName = scrapy.Field()

    # 职位详情的链接
    positionLink = scrapy.Field()

    # 职位类型
    positionType = scrapy.Field()

    # 人数
    peopleNumber = scrapy.Field()

    # 工作地点
    workLocation = scrapy.Field()

    # 发布时间
    publistTime = scrapy.Field()
