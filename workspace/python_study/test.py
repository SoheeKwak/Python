import pymysql

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='root123',
                       charset='utf8')
curs = conn.cursor()
sql = "select * from korcham.tbl_reply"
curs.execute(sql)

rows = curs.fetchall()
print(rows)


import cx_Oracle
connection = cx_Oracle.connect("System/7900@Localhost:1521/xe")
cursor = connection.cursor()
cursor.execute("select * from book")
for result in cursor:
    print("Values:",result)

cursor.close()
connection.close()
