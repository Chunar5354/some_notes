import pymysql
from my_helper import MysqlHelper as msh

ms1 = msh(host='localhost', user='root', password='rasp.0927', database='test')
ms1.connect()
sql1 = "select * from pet"
sql2 = "update pet set owner='CCb' where name='NewGuy'"

count = ms1.update(sql2)

data1 = ms1.fetchall(sql1)
for i in data1:
    print(i)
