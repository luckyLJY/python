'''
删除数据
1. 导入pymysql
2. 建立数据库连接
3. 查询最大值
4. 创建游标对象
5. 执行sql
6. 提交事务
7. 回滚事务
8. 关闭连接
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
def delete():
    maxid = read_max_userid()
    try:
        with connection.cursor() as cursor:
            sql = 'delete from user where userid = %s'
            affectedcount = cursor.execute(sql,(maxid))

            print("影响行数：{0}".format(affectedcount))

            connection.commit()
    except pymysql.DatabaseError as e:
        connection.rollback()
        e.print
    finally:
        connection.close()

delete()