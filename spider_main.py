
# -*- coding: utf-8 -*-

import url_manager, html_parser, html_downloader, html_outputer


class Spider(object):
	def __init__(self):
		self.urls = url_manager.UrlManager()
		self.downloader = html_downloader.HtmlDownloader()
		self.outputer = html_outputer.HtmlOutputer()
		self.parser = html_parser.HtmlParser()

	def crawl(self, root_url):
		self.urls.add_new_url(root_url)
		count = 1
		while self.urls.has_new_url():
			try:
				new_url = self.urls.get_new_url()
				print "Crawl NO.%d: %s" %(count, new_url)
				html_cont = self.downloader.download(new_url)
				#print html_cont
				new_urls, new_data = self.parser.parse(new_url, html_cont)
				#print new_urls, new_data
				self.urls.add_new_urls(new_urls)
				self.outputer.collect(new_data)

				if count==20:
					break
				count += 1

			except:
				print "Oops, Crawl Faild :("

		self.outputer.output()


if __name__ == "__main__":
	root_url = "http://www.qiushibaike.com/"
	obj_spider = Spider()
	obj_spider.crawl(root_url)
