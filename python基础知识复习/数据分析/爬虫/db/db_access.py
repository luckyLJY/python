import logging
import pymysql

logger = logging.getLogger(__name__)

def insert_hisq_data(row):
    '''将股票数据插入数据库'''

    # 1. 建立数据库连接
    connection = pymysql.connect(host='localhost',
                                 user= 'root',
                                 password = '123456',
                                 database = 'nasdaq',
                                 charset = 'utf8')

    try:
        # 2. 创建游标对象
        with connection.cursor() as cursor:
            # 执行sql操作
            sql = 'insert into historicalquote ' \
                  '(HDate,Open,High,Low,Close,Volume,Symbol)' \
                  ' values (%(Date)s,%(Open)s,%(High)s,%(Low)s,%(Close)s,%(Volume)s,%(Symbol)s)'

            affectedcount = cursor.execute(sql,row)
            logger.debug('影响的数据行数{0}'.format(affectedcount))
            # 4. 提交数据库事物
            connection.commit()
        # with代码块结束，5关闭游标
    except pymysql.DatabaseError as error:
        # 4. 回滚数据库事务
        connection.rollback()
        logger.debug('插入数据失败'+error)
    finally:
        # 6. 关闭数据连接
        connection.close()