import requests
import xml.etree.ElementTree as ET
from xml.parsers.expat import ParserCreate
import time


class DefaultSaxHandler(object):
    def __init__(self, type):
        self.type = type

    # 处理标签开始
    def start_element(self, name, attrs):
        if name == 'a':
            name = attrs['href']
           # number = attrs['href']
            self.type.append(name)

    # 处理标签结束
    def end_element(self, name):
        pass

    # 文本处理
    def char_data(self, text):
        pass


# *args是非关键字参数，用于元组，**kw是关键字参数，用于字典
def get_province_entry(url):
    # 获取文本，并用gb2312解码
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0'}
    time.sleep(10)
    content = requests.get(url, headers=header).content
    time.sleep(1)
    # 确定要查找字符串的开始结束位置，并用切片获取内容。
    start = content.find('<tr bgcolor=\"#b9b9fe\"><th>Description</th><th>Category</th></tr>')
    end = content.find('</table>')
    content = content[start:end + len('</table>')].strip()
    type = []
    # 生成Sax处理器
    handler = DefaultSaxHandler(type)
    # 初始化分析器
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    # 解析数据
    parser.Parse(content)
    # 结果字典为每一页的入口代码
    return type


issue = get_province_entry('http://findbugs.sourceforge.net/bugDescriptions.html')
print(issue)
