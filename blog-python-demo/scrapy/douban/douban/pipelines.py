# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
from itemadapter import ItemAdapter


class DoubanPipeline:
    def process_item(self, item, spider):
        return item


class MoviePipeline:
    def process_item(self, item, spider):
        movie = vars(item).get('_values')
        for k, v in movie.items():
            if isinstance(v, str):
                movie[k] = v.strip()
            if isinstance(v, list):
                movie[k] = list(map(lambda x: x.strip(), v))
        movie['rating'] = float(movie['rating'])
        movie['comments_num'] = int(movie['comments_num'])
        movie['summary'] = '\n'.join(movie['summary'])
        item._values = movie
        return movie


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
