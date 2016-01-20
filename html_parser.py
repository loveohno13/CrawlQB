# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re 
import urlparse


class HtmlParser(object):
    def __init__(self):
        self.new_urls = []
        self.new_data = []



    def _get_new_urls(self, url, soup):
        links = soup.find_all("a", href=re.compile("/8hr/page/\w*"))
        for link in links:
            new_full_link = urlparse.urljoin(url, link['href'])
            self.new_urls.append(new_full_link)
        return self.new_urls

    def _get_new_data(self, url, soup):
        res_data = soup.find_all("div", class_="fs-l mlr mt10")
        for res in res_data:
            self.new_data.append(res.get_text())
        return self.new_data

    def parse(self, url, html_cont):

        soup = BeautifulSoup(html_cont, "html.parser", from_encoding="utf-8")

        #解析出新的URLS
        self.new_urls = self._get_new_urls(url, soup)
        self.new_data = self._get_new_data(url, soup)

        return self.new_urls, self.new_data
        #print self.new_urls, self.new_data







