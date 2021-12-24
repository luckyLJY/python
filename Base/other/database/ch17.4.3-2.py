# 无条件查询
'''
1.导入pymysql
2.建立数据库连接
3.创建游标对象
4.执行sql
5.提取结果集
6.关闭游标
'''

import pymysql

connection = pymysql.connect(host='localhost',user='root',password='123456',database='mydb',charset='utf8')

try:
    with connection.cursor() as cursor:
        sql = 'select max(userid) from user'
        cursor.execute(sql)
        row = cursor.fetchone()
        if row is not None:
            print("最大用id:{0}".format(row[0]))
finally:
    connection.close()