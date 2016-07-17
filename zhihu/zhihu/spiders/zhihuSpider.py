import scrapy
from settings import USERNAME,PASSWORD

class ZhihuSpider(scrapy.Spider):
    name = "zhihu"
    start_urls = [
        "http://www.zhihu.com/#signin"
    ]

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={"email":USERNAME,"password":PASSWORD},
            method="POST",
            url="http://www.zhihu.com/login/email",
            callback=self.after_login
        )

    def after_login(self, response):
        return scrapy.Request("https://www.zhihu.com/", self.parse_index)

    def parse_index(self, response):
        for item in response.xpath('(//a[@class="post-link"]|//a[@class="question_link"])/text()').extract():
            print item

