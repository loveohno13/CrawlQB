# -*- coding: utf-8 -*-



class HtmlOutputer(object):
    """docstring for HtmlOutputer"""
    def __init__(self):
        self.datas = list()

    def collect(self, datas):
        if datas is None:
            return
        for data in datas:
            self.datas.append(data)
        #print self.datas
        return self.datas

    def output(self):

        with open("output.text", "a+") as f:
            for data in self.datas:
                data = f.write(data.encode("utf-8"))
            
