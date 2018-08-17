import uuid
import pymysql.cursors
from xml.dom import minidom

issueTracker = [[0 for i in range(5)]]
doc = minidom.parse('issue.xml')
root = doc.documentElement
# print(root.nodeName)
issues = root.getElementsByTagName('tr')
for issue in issues:
    category = issue.getElementsByTagName('td')
    des = category[0].getElementsByTagName('a')
    name = des[0].getAttribute('href').strip('#')
    tool = 'findbugs'
    description = des[0].childNodes[0].nodeValue
    findbugs_category = category[1].childNodes[0].nodeValue
    id = str(uuid.uuid4())
    issueTracker.append([id, name, tool, findbugs_category, description])
issueTracker.remove([0, 0, 0, 0, 0])
# 连接数据库
conn = pymysql.connect(
    host='10.141.221.73',
    port=3306,
    user='root',
    passwd='root',
    db='issueTracker',
    charset='utf8')

try:
    with conn.cursor() as curson:
        for li in issueTracker:
            # print(li)
            sql = 'insert into issueType (uuid, name, tool, category, description) values(%s,%s,%s,%s,%s)'
            curson.execute(sql,tuple(li))
    conn.commit()
finally:
    curson.close()
    conn.close()
