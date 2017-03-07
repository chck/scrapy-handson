# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup

from my_crawler.items import MyCrawlerItem


class ExampleSpider(scrapy.Spider):
    name = "example"
    # allowed_domains = ["example.com"]
    start_urls = [
        # 'https://tabelog.com/tokyo/A1303/A130301/13134660/',
        # 'https://tabelog.com/tokyo/A1303/A130301/13033421/',
        # 'https://tabelog.com/tokyo/A1303/A130301/13009318/',
        # 'http://www.library.shimonoseki.yamaguchi.jp/',
        'https://tabelog.com/tokyo/A1303/A130301/R4698/rstLst/ZZ/',
    ]

    def parse(self, response):
        soup = BeautifulSoup(response.body, "lxml")

        for store_tag in soup.find_all("a", class_="list-rst__rst-name-target cpy-rst-name"):
            store_url = store_tag.attrs['href']
            # print("###################################")
            # print(store_url)
            # print("###################################")
            yield scrapy.Request(store_url, callback=self.parse_store)

    def parse_store(self, response):
        soup = BeautifulSoup(response.body, "lxml")

        url = response.url
        title = soup.find("h2", class_="display-name").a.span.text
        rate = soup.find("b", class_="tb-rating__val rdheader-rating__score-val").span.text
        review = soup.find("span", class_="rdheader-rating__review-target").a.text
        nearest_station = soup.find("span", class_="linktree__parent-target-text").text
        budget_of_dinner = soup.find("p", class_="rdheader-budget__icon rdheader-budget__icon--dinner").a.text
        budget_of_lunch = soup.find("p", class_="rdheader-budget__icon rdheader-budget__icon--lunch").a.text

        # print("###################################")
        # print("{}\n{}\n{}\n{}\n{}\n{}\n{}".format(url, title, rate, review, nearest_station, budget_of_dinner, budget_of_lunch))
        # print("###################################")
        return MyCrawlerItem(url=url,
                             title=title,
                             rate=rate,
                             review=review,
                             nearest_station=nearest_station,
                             budget_of_dinner=budget_of_dinner,
                             budget_of_lunch=budget_of_lunch)
