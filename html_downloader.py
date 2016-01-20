# -*- coding: utf-8 -*-
import urllib2 


class HtmlDownloader(object):


    def download(self, url):
        if url is None:
            return

        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
        response = urllib2.urlopen(req)
        html_cont = response.read()
        return html_cont
        #print html_cont

        
'''test = HtmlDownloader()
url = "http://www.qiushibaike.com/"
test.download(url)
'''

