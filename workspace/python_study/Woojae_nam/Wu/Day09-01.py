#  SQLite 접속하기, 로컬DD 내 테이블 생성
import sqlite3
con = sqlite3.connect('c:/temp/userDB') #데이터베이스 지정(또는 연결). 만약 그냥 'userDB'로 지정하면 파이참 내에 생성됨
cur = con.cursor() #연결 통로 생성(쿼리문을 날릴 통로)
# 테이블 만들기
try:
    sql = "CREATE TABLE userTable(userID CHAR(10), userName CHAR(5), userAge INT);"
    cur.execute(sql)

except:
    pass

sql = "INSERT INTO userTable VALUES('AAA', '에이', 21);"
cur.execute(sql)
sql = "INSERT INTO userTable VALUES('BBB', '삐이', 23);"
cur.execute(sql)
sql = "INSERT INTO userTable VALUES('CCC', '씨이', 35);"
cur.execute(sql)

con.commit()

cur.close()
con.close() # 데이터베이스 연결 종료
print('ok')