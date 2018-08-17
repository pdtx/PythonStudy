import json
from xml.dom import minidom

import string
from xml.parsers.expat import ParserCreate

import time
from selenium import webdriver
import re
'''
def json
obj = {'one': '一', 'two': '二'}
# 编码转化成str
encoded = json.dumps(obj)
print(type(encoded))
print(encoded)
# 解码
decoded = json.loads(encoded)
print(type(decoded))
print(decoded)
'''

'''
DOM 把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
SAX 流模式，边读边解析，占用内存小，解析快，缺点是需要自己处理事件。
'''


def dom():
    doc = minidom.parse('book.xml')
    root = doc.documentElement
    print(type(root))
    # dir 查看有哪些方法
    # print(dir(root))
    print(root.nodeName)
    books = root.getElementsByTagName('book')
    print(type(books))
    for book in books:
        titles = book.getElementsByTagName('title')
        print(titles[0].childNodes[0].nodeValue)


class DefaultSaxHandler:
    def start_element(self,name,attrs):
        self.element = name
        print('element: %s,attrs: %s' % (name,str(attrs)))

    # @staticmethod
    def end_element(self,name):
        print('end element : %s ' % name)

    def date(self,text):
        if text.strip():
            print("%s's text is %s" % (self.element,text))


def eg_sax():
    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.date
    with open('book.xml','r') as f:
        parser.Parse(f.read())


def eg_re():
    m = re.match(r'\d{3}\-\d{3,8}','010-12345')
    print(m.string)
    print(m.pos,m.endpos)


def eg_selenium():
    pass

if __name__ == '__main__':
    eg_re()



