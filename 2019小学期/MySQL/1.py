import pymysql

# # 打开数据库连接
# db = pymysql.connect("localhost", "root", "19991104", "zxd1")
# cursor = db.cursor()  # 创建一个游标对象 cursor
# cursor.execute("SELECT VERSION()")  # 执行 SQL 查询
# data = cursor.fetchone()  # 获取单条数据.
# print("Database version : %s " % data)
# db.close()  # 关闭数据库连接

# import pymysql
#
# db = pymysql.connect("localhost", "root", "19991104", "zxd1")
# cursor = db.cursor()  # 一个游标对象 cursor
# # 使用预处理语句创建表
# sql = """CREATE TABLE `H_Email` (
#         `id`  int NOT NULL AUTO_INCREMENT ,
#         `sender`  varchar(50) NULL ,
#         `receiver`  varchar(50) NULL ,
#         `context`  varchar(1000) NULL ,
#         `p_date`  varchar(19) NULL ,
#         `title`  varchar(19) NULL ,
#          PRIMARY KEY (`id`)
#         )"""
# cursor.execute(sql)
# db.close()

import pymysql

db = pymysql.connect("localhost", "root", "19991104", "zxd1")
cursor = db.cursor()
sql = """INSERT INTO h_email(sender,
         receiver, context,p_date,title)
         VALUES('hh@163.com', 'hh@hit.edu.cn’,
                           ‘成功’, ‘2019-03-09 21:30:01’,’人生’)"""
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()
