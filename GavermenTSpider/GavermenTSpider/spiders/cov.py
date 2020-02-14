# -*- coding: utf-8 -*-
import scrapy
import json
from GavermenTSpider.items import GavermentspiderItem
import re


class CovSpider(scrapy.Spider):
    name = 'cov'
    allowed_domains = ['gov.cn']
    start_urls = [
        'http://www.cbirc.gov.cn/cbircweb/DocInfo/SelectDocByItemIdAndChild?itemId=954&pageSize=18&pageIndex=2']

    def parse(self, response):
        jsonText = response.text
        dictTest = json.loads(jsonText)
        dict_list = dictTest['data']['rows']
        for data in dict_list:
            item = GavermentspiderItem()
            item['Title'] = data['docSubtitle']
            item['Publish_Date'] = data['publishDate']

            if data['docFileUrl'] is not None:
                item['Doc_File_DownLoad'] = "http://www.cbirc.gov.cn/{}".format(data['docFileUrl'])

            if data['pdfFileUrl'] is not None:
                item['Pdf_File_DownLoad'] = "http://www.cbirc.gov.cn/{}".format(data['pdfFileUrl'])

            if data['docTitle'] is not None:
                item['Doc_Title'] = data['docTitle']

            item['Article_Url'] = "http://www.cbirc.gov.cn/cn/view/pages/ItemDetail.html?docId={}".format(data['docId'])
            yield item

        '''请求下一页'''
        page = int(re.findall(r".*pageIndex=(\d+)", response.url)[0])
        print(page)
        if page * 18 - 9 <= int(dictTest['data']['total']):
            '''构造下一页请求'''
            url = "http://www.cbirc.gov.cn/cbircweb/DocInfo/SelectDocByItemIdAndChild?itemId=954&pageSize=18&pageIndex={}".format(
                page + 1)
            print(url)
            yield scrapy.Request(
                url=url,
                callback=self.parse
            )