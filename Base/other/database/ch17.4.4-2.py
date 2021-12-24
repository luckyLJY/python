'''
数据更新
1. 导入pymysql
2. 建立数据库连接
3. 创建游标对象
4. 执行sql操作
5. 提交数据库事务
6. 回滚，打印错误日志
7. 关闭数据库连接
'''

import pymysql

connection = pymysql.connect(host='localhost',user='root',password='123456',database='mydb',charset='utf8')

try:
    with connection.cursor() as cursor:
        sql = 'update user set name = %s where userid > %s'
        affectedcount = cursor.execute(sql,('Tom1',2))

        print('影响的数据行数：{0}'.format(affectedcount))
        connection.commit()

except pymysql.DatabaseError as e:
    connection.rollback()
    print(e)
finally:
    connection.close()