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
