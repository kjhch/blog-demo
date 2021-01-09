# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random
import urllib.parse

from scrapy import signals, Request
from scrapy.downloadermiddlewares.retry import RetryMiddleware
from scrapy.http import HtmlResponse
from scrapy.utils.response import response_status_message

from douban.utils import del_proxy, get_proxy


class DoubanSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class DoubanDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class RandomUserAgentMiddleware:
    def __init__(self, agents):
        self.user_agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls(crawler.settings['USER_AGENTS'])
        return s

    def process_request(self, request, spider):
        ua = random.choice(self.user_agents)
        # print('RandomUserAgentMiddleware process_request', ua)
        request.headers['User-Agent'] = ua

    # def process_response(self, request, response: HtmlResponse, spider):
    #     print('RandomUserAgentMiddleware process_response')
    #     return response


class ForbiddenRespMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        return s

    # def process_request(self, request, spider):
    #     print('ForbiddenRespMiddleware process_request')

    def process_response(self, request: Request, response: HtmlResponse, spider):
        print(response.status, response.url, '->', response.headers['Location'])

        if 300 < response.status < 500:
            proxy = request.meta.get('proxy')
            print(response.url, response.status, request.meta)
            if proxy:
                del_proxy(urllib.parse.urlparse(proxy).netloc)
            request.meta['proxy'] = "203.198.94.132:80"
            # request.dont_filter = True
            return request
        return response

    # def process_exception(self, request, exception, spider):
    #     print('ForbiddenRespMiddleware process_exception',request.dont_filter)
    #     return request


class CustomRetryMiddleware(RetryMiddleware):

    def switch_proxy(self, request: Request):
        proxy = request.meta.get('proxy')
        if proxy:
            del_proxy(urllib.parse.urlparse(proxy).netloc)
        request.meta['proxy'] = get_proxy()

    def process_response(self, request, response, spider):
        if request.meta.get('dont_retry', False):
            return response
        # 注意配置RETRY_HTTP_CODES
        if response.status in self.retry_http_codes:
            if response.status % 300 < 100:
                print(response.status, response.url, '->', response.headers['Location'])
            else:
                print(response.status, response.url)
            reason = response_status_message(response.status)
            self.switch_proxy(request)
            return self._retry(request, reason, spider) or response

        return response

    def process_exception(self, request, exception, spider):
        # RetryMiddleware类里有个常量，记录了连接超时那些异常
        # EXCEPTIONS_TO_RETRY = (defer.TimeoutError, TimeoutError, DNSLookupError,
        #                       ConnectionRefusedError, ConnectionDone, ConnectError,
        #                       ConnectionLost, TCPTimedOutError, ResponseFailed,
        #                       IOError, TunnelError)
        if isinstance(exception, self.EXCEPTIONS_TO_RETRY) and not request.meta.get('dont_retry', False):
            self.switch_proxy(request)
            return self._retry(request, exception, spider)
        # _retry是RetryMiddleware中的一个私有方法，主要作用是
        # 1.对request.meta中的retry_time进行+1
        # 2.将retry_times和max_retry_time进行比较，如果前者小于等于后者，利用copy方法在原来的request上复制一个新request，并更新其retry_times，并将dont_filter设为True来防止因url重复而被过滤。
        # 3.记录重试reason
