# coding: utf-8
import urlparse
import urllib2 as urllib2
from lxml import etree as et

class LxmlExtractor():

    def __init__(self,url):
        self.url=url
        response=urllib2.urlopen(self.url)
        self.root=et.fromstring(response.read(),et.HTMLParser())
        self.tree=et.ElementTree(self.root)
    def getTextLines(self):
        textlines=self.root.xpath("//body//text()")
        return textlines
    def getTree(self):
        return self.tree
    def getLinePath(self,line):
        return self.tree.getpath(line.getparent())
