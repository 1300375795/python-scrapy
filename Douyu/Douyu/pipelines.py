# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import os
from settings import IMAGES_STORE


class DouyuPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        imageLink = item["imageLink"]
        yield scrapy.Request(imageLink)

    def item_completed(self, results, item, info):
        imagesPath = [x["path"] for ok, x in results if ok][0]
        srcName = IMAGES_STORE + imagesPath
        dstName = IMAGES_STORE + item["nickname"].encode("utf-8") + ".jpg"
        os.rename(srcName, dstName)
        return item
