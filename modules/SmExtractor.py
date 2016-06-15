# coding: utf-8
import urlparse
import urllib2 as url
from lxml import etree as et
import os
import re
from Dao import *
from LxmlExtractor import *

#def get1stLevel(cur,line):
#    if True:
#        cur.execute('select item from smemory where ref like ''%strong%'' ')
#        cur.fetchone()


#------------------------
d=Dao()
d.resetDb()

#------------------------
lextractor=LxmlExtractor("https://opensource.com/business/15/7/five-open-source-nlp-tools")
textlines=lextractor.getTextLines()

#------------------------
for line in textlines:
    #shortpath=re.sub(r'/div[\[\d+\]]*',"",tree.getpath(line.getparent()))
    path=lextractor.getLinePath(line)
    style=''
    parent=''
    if re.search(r'/em|/strong',path):
        style='strong'
    elif re.search(r'/h\d+',path):
        style='header'
    if re.search(r'/p',path):
        parent+='p'
    if re.search(r'/ol|/ul',path):
        parent+=','+re.sub(r'(?<=[/ol\[\d+\]*|/ul\[\d+\]*])/li.*',"",path)
    if len(line.strip())>0:
        d.insertSmemory((line,path,style,parent))
