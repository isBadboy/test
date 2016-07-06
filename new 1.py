# coding=utf-8

import re
import urllib


def getCoder(url):
    page1 = urllib.urlopen(url)
    html = page1.read()
    rule = r'<a data=hash=.*? href="(.*?)" class=.*?>@.*?</a>'
    coderList = re.findall("rule", "html")
    #for coderName in coderList
        #print coderName
    print coderList


getCoder("http://www.zhihu.com/")
