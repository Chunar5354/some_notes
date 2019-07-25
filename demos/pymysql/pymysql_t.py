import pymysql

# 获取连接对象
conn = pymysql.connect(host='localhost', user='root', password='rasp.0927', database='test', port=3306)

# 获取执行工具
cur = conn.cursor()

# sql命令
sql1 = 'select * from pet'
#sql1 = 'select name, birth from pet'

# 返回受影响的行数
count = cur.execute(sql1)
print(count, '条数据')

# 获取第一行
dateOne = cur.fetchone()
print('dataOne:')
print(dateOne)

cur.scroll(-1)

cur.scroll(1)

cur.scroll(1, mode='absolute')
cur.scroll(1, mode='relative')

# 获取所有行的数据
dataAll = cur.fetchall()
print('dataAll:')
print(dataAll)

for temp in dataAll:
    print(temp)
    print(dataAll[1][1])

for temp in cur:
    print(temp)


cur.close()
conn.close()
