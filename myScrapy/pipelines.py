# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import codecs


class MyscrapyPipeline:
    def process_item(self, item, spider):
        print("this is pipeline",end='\n')
        if item['message']=='':
            item['message']='ahpu'+item['title']
        item['message']=item['message'].replace('\r','').replace('\n','')
        print('这是pipeline输出',end='\n\n')
        return item

# -*- coding: utf-8 -*-
# import codecs
# import json

# class myScrapyPipeline(object):
#     def __init__(self):
#         self.file = codecs.open('data_cn.json', 'wb', encoding='utf-8')

#     def process_item(self, item, spider):
#         line = json.dumps(dict(item)) + '\n'
#         self.file.write(line.decode("unicode_escape"))
#         return item