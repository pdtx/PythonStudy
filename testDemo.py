# -*- coding: utf-8 -*-
'''
# 连接数据库
connect = pymysql.Connect(
    host='10..141.221.73',
    port=3306,
    user='root',
    passwd='root',
    db='issueTracker',
    charset='utf8'
)
# 获取游标
cursor = connect.cursor()

# 查询数据
sql = "SELECT * FROM issueType "
# data = ('13512345678',)
cursor.execute(sql)
for row in cursor.fetchall():
    print( row)
print('共查找出', cursor.rowcount, '条数据')
'''
'''

import pymysql
import time

conn = pymysql.connect(
    host='10.141.221.73',
    port=3306,
    user='root',
    passwd='root',
    db='issueTracker',
    charset='utf8')

time.sleep(1)

try:
    with conn.cursor() as cursor:
        # 执行sql语句
        sql = 'select * from issueType'
        cursor.execute(sql)
    conn.commit()
finally:
    conn.close()

print(cursor.fetchall())

conn = r.connect(host='aws-us-east-1-portal.1.dblayer.com',  
             port=23232,
             auth_key='[auth_key]',
             ssl={'ca_certs': './cacert'})
"rethinkdb://user:password@aws-us-east-1-portal.1.dblayer.com:23232".encode("idna")
'issueTracker://root:root@10.141.221.73:3306'.encode("idna")
             
'''
import requests
import json

url = "http://10.141.221.80:8002/project"

body = {
    "url":"https://github.com/mockito/mockito"
}
data = json.JSONEncoder().encode(body)

headers = {'token':'ec15d79e36e14dd258cfff3d48b73d35',
           'content-type':'application/json'}
response = requests.post(url, data=data, headers=headers).text
print(response)
