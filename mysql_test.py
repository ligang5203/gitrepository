# coding: UTF-8
import MySQLdb


# ip地址，用户名，密码，要连接的数据库名
db = MySQLdb.connect("localhost", "root", "", "lg")
cursor = db.cursor()
cursor.execute("select * from sc;")
das = cursor.fetchall()
for data in das:
    print data
db.close()