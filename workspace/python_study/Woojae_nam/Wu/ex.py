import pymysql
con = pymysql.connect(host='192.168.5.131', user='biguser',
                      password='1234', db='USERDB')  # 데이터베이스 지정(또는 연결)
cur = con.cursor()  # 연결 통로 생성 (쿼리문을 날릴 통로)

sql  = "select * from userTable2"
cur.execute(sql)

