import pymysql

conn = pymysql.connect(host='localhost', user='root', port=3306, database='test', password='rasp.0927')

cur = conn.cursor()

sql1 = "select * from pet where sex='f'"

cur.execute(sql1)

result = cur.fetchone()
resule_all = cur.fetchall()

print(result)
print(result_all)

cur.close()
conn.close()