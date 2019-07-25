import pymysql

conn = pymysql.connect(host='localhost', port=3306, db='test', password='rasp.0927')
cs1 = conn.cursor()

sql1 = "insert into pet(name) values('NewGuy')"

count = cs1.execute(sql1)
print(count)

conn.commit()

cs1.close()
conn.close()