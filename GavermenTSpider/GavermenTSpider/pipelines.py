# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
import logging
from time import time

logger = logging.getLogger(__name__)


class GavermentspiderPipeline(object):
    def open_spider(self, spider):
        client = MongoClient()
        self.conn = client['covn']['cov']
        self.start_T = time()

    def process_item(self, item, spider):
        self.conn.insert(dict(item))
        logger.warning(item)
        return item

    def close_spider(self, spider):
        finall_T = time()
        print("总耗时 {} 秒".format(finall_T - self.start_T))
