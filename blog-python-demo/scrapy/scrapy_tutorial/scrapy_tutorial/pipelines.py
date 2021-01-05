# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class ScrapyTutorialPipeline:
    """
    需要在settings.py的ITEM_PIPELINES中配置一个数值来激活管道，数值范围[0,1000]，数值越低，越先执行
    """

    def process_item(self, item, spider):
        # print("====process item", item)
        if item['name'] == '张老师':
            raise DropItem('丢弃张老师')
        item['name'] += '==='
        return item


class QuotePipeline:
    def process_item(self, item, spider):
        item['text'] = item['text'].strip("“”")
        return item


class MongoPipeline:
    def __init__(self, mongo_uri, mongo_db, mongo_collection):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_collection = mongo_collection

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'spider'),
            mongo_collection=crawler.spider.mongo_collection
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.mongo_collection].insert_one(ItemAdapter(item).asdict())
        return item
