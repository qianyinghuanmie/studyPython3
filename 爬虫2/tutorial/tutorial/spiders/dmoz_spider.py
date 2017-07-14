# -*- coding: utf-8 -*-

import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz"  #用于区别Spider。 该名字必须是唯一的，您不可以为不同的Spider设定相同的名字。
    allowed_domains = ["dmoztools.net"]
    start_urls = [
        "http://dmoztools.net/Computers/Programming/Languages/Python/Books/",
        "http://dmoztools.net/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)