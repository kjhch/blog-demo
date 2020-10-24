# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
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

