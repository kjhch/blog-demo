[scrapy架构——官方文档](https://docs.scrapy.org/en/latest/topics/architecture.html)

个人理解：命令行启动spider；engine获取spider中的start_urls；然后将其分配给scheduler；scheduler准备完毕后返回给engine；engine将请求发送给Downloader，中间如果有Downloader middlewares的话，中间件会进行处理；然后Downloader拉取网页并将结果返回给engine，同样有中间件的话会处理；engine将response发送给spider（如果有spider middlewares的话会处理），然后调用parse方法该方法返回一个可迭代对象；engine遍历可迭代对象，若当前元素是一个request则将其发送给scheduler继续调度爬取，若是一个数据对象则发送给pipelines进行数据处理。若scheduler中没有request了则爬取结束。

```
# 创建新项目
scrapy startproject scrapy_tutorial

# 在spiders目录下生成itcast.py爬虫文件
scrapy genspider itcast "itcast.cn"

# 运行爬虫，结果仅仅控制台输出。以下命令都会输出控制台
scrapy crawl itcast
# 输出到json文件 [{},{}]
scrapy crawl itcast -o teachers.json  
# 输出json行，{}一行
scrapy crawl itcast -o teachers.jsonlines
# 输出csv
scrapy crawl itcast -o teachers.csv  
# 输出xml
scrapy crawl itcast -o teachers.xml 

# 注意：输出不会覆盖已存在的文件 
```
Scrapy 中的数据流由引擎控制，数据流的过程如下 。
1. Engine首先打开一个网站，找到处理该网站的 Spider，并向该 Spider请求第一个要爬取的 URL。 
2. Engine从 Spider中获取到第一个要爬取的 URL，并通过 Scheduler以 Request的形式调度。
3. Engine 向 Scheduler请求下一个要爬取的 URL。
4. Scheduler返回下一个要爬取的 URL给 Engine, Engine将 URL通过 DownloaderMiddJewares转
发给 Downloader下载。
5. 一旦页面下载完毕， Downloader生成该页面的 Response，并将其通过 DownloaderMiddlewares
发送给 Engine。
6. Engine从下载器中接收到lResponse，并将其通过 SpiderMiddlewares发送给 Spider处理。
7. Spider处理 Response，并返回爬取到的 Item及新的 Request给 Engine。
8. Engine将 Spider返回的 Item 给 Item Pipeline，将新 的 Request给 Scheduler。 
9. 重复第(2)步到第(8)步，直到 Scheduler中没有更多的 Request, Engine关闭该网站，爬取结束。

我们常用 Item Pipeline来做如下操作：
- 清理 HTML数据。
- 验证爬取数据，检查爬取字段。 
- 查重井丢弃重复内容。
- 将爬取结果保存到数据库。