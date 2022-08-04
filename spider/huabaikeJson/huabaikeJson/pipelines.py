'''
Author: zhaoshan
Date: 2022-08-04 10:35:40
LastEditTime: 2022-08-04 10:37:04
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

class HuabaikejsonPipeline:
    def __init__(self):
        self.file = codecs.open('data.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.file.write(line)
        return item 
