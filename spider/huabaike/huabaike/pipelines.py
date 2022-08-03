'''
Author: zhaoshan
Date: 2022-06-30 17:16:06
LastEditTime: 2022-08-03 15:20:33
LastEditors: zhaoshan
Description: 
'''
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class HuabaikePipeline:
    # def __init__(self):
    #     self.file = codecs.open('data.json', 'w', encoding='utf-8')

    # def process_item(self, item, spider):
    #     line = json.dumps(dict(item), ensure_ascii=False) + ",\n"
    #     self.file.write(line)
    #     return item 

    def open_spider(self, spider):
        host = spider.settings['MONGODB_HOST']
        port = spider.settings['MONGODB_PORT']
        db_name = spider.settings['MONGODB_NAME']
        # pymongo.MongoClient(host, port) 创建MongoDB链接
        self.client = pymongo.MongoClient(host=host, port=port)
        self.db = self.client[db_name]
        self.collection = self.db[spider.settings['MONGODB_DOCNAME']]
        self.item_list = []
 
    # def process_item(self, item ,spider):
    #     self.item_list.append(dict(item))
    #     return item
    def process_item(self, item, spider):
        self.item_list.append(dict(item))
        return item 
    
    def close_spider(self,spider):
        self.collection.insert_many(self.item_list)
        print('{}条数据已存入数据库'.format(len(self.item_list)))
        self.client.close()
        print('数据库已关闭')
