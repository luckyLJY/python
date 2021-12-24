'''
数据库修改操作
1. 导入pymsql
2. 建立数据库connection连接
3. 执行sql:insert into user (userid,name) values (%s,%s)
4. 提交数据库事务
5. 异常回滚数据库事务
6. 关闭数据库连接
'''

import pymysql

connection = pymysql.connect(host='localhost',user='root',password='123456',database='mydb',charset='utf8')

# 查询用户最大id
def read_max_userid():

    with connection.cursor() as cursor:
        sql = 'select max(userid) from user'
        cursor.execute(sql)
        row = cursor.fetchone()
        if row is not None:
            print("最大用id:{0}".format(row[0]))
            return row[0]




def insert():
    maxid = read_max_userid()
    try:
        with connection.cursor() as cursor:
            sql = 'insert into user (userid,name) values (%s,%s)'
            nextid = maxid + 1
            name = 'Tony' + str(nextid)
            affetedcount = cursor.execute(sql,(nextid,name))
            print('影响的数据行数：{0}'.format(affetedcount))

            connection.commit()
    except pymysql.DatabaseError:
        connection.rollback()
    finally:
        connection.close()

insert()