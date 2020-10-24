import scrapy

from scrapy_tutorial.items import ScrapyTutorialItem


class ItcastSpider(scrapy.Spider):
    """
    要建立一个Spider， 你必须用scrapy.Spider类创建一个子类，并确定了三个强制的属性 和 一个方法。
    1. name = "" ：这个爬虫的识别名称，必须是唯一的，在不同的爬虫必须定义不同的名字。

    2. allow_domains = [] 是搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页，不存在的URL会被忽略。

    3. start_urls = () ：爬取的URL元祖/列表。爬虫从这里开始抓取数据，所以，第一次下载的数据将会从这些urls开始。其他子URL将会从这些起始URL中继承性生成。

    4. parse(self, response) ：解析的方法，每个初始URL完成下载后将被调用，调用的时候传入从每一个URL传回的Response对象来作为唯一参数，主要作用如下：
        1)负责解析返回的网页数据(response.body)，提取结构化数据(生成item)
        2)生成需要下一页的URL请求(scrapy.http.request.Request)。

    注意！只有当调度器中不存在任何request了，整个程序才会停止，（也就是说，对于下载失败的URL，Scrapy也会重新下载。）
    """
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        """
        :param response: 类为scrapy.http.response.html.HtmlResponse
        :return: 一个list或者迭代器
        """
        # print("=========: " + str(response.__class__))  # <class 'scrapy.http.response.html.HtmlResponse'>
        # context = response.xpath('/html/head/title/text()')
        # print("=========: " + str(context))
        # title = context.extract_first()
        # print("=========: " + str(title))
        items = []
        for each in response.xpath("//div[@class='li_txt']"):
            # print("=======: " + str(each.__class__))  # <class 'scrapy.selector.unified.Selector'>
            item = ScrapyTutorialItem()
            name = each.xpath("h3/text()").extract()
            # print("=======: " + str(name.__class__))  # <class 'list'>
            title = each.xpath("h4/text()").extract()
            info = each.xpath("p/text()").extract()
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]
            items.append(item)
        return items
