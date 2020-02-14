# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GavermentspiderItem(scrapy.Item):
    # define the fields for your item here like:
    Title = scrapy.Field()
    Publish_Date = scrapy.Field()
    Doc_File_DownLoad = scrapy.Field()
    Pdf_File_DownLoad = scrapy.Field()
    Doc_Title = scrapy.Field()
    Article_Url = scrapy.Field()

