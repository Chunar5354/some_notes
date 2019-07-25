import pymysql

class MysqlHelper():
    def __init__(self, host, user, password, database, port=3306):
        '''
        初始化参数
        :param host:            主机
        :param user:            用户名
        :param password:        密码
        :param database:        数据库
        :param port:            端口号，默认是3306
        '''

        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port

    def connect(self):
        '''
        获取连接对象和执行对象
        :return:            None
        '''

        self.conn = pymysql.connect(host=self.host,
                                    user=self.user,
                                    password=self.password,
                                    port=self.port,
                                    database=self.database
                                    )
        self.cur = self.conn.cursor()

    def fetchall(self, sql):
        '''
        根据sql命令获取数据
        :param sql:             sql语句
        :return:                查询到的数据
        '''

        dataall = 0
        try:
            count = self.cur.execute(sql)
            if count != 0:
                dataall = self.cur.fetchall()
        except Exception as ex:
            print(ex)
        #finally:
        #    self.close()  # 这里为啥self.close？
        return dataall

    def __item(self, sql):
        '''
        执行增删改操作的内置函数
        :param sql:              sql语句
        :return:                 受影响的行数
        '''

        count = 0
        try:
            count = self.cur.execute(sql)
            self.conn.commit()  # 增删改操作需要加一个commit
        except Exception as ex:
            print(ex)
        #finally:
        #    self.close()
        return count

    def update(self, sql):
        '''
        执行修改，调用内部的__item()
        :param sql:              sql语句
        :return:                 受影响的行数
        '''

        return self.__item(sql)

    def insert(self, sql):
        '''
        执行增加，调用内部的__item()
        :param sql:              sql语句
        :return:                 受影响的行数
        '''

        return self.__item(sql)

    def delete(self, sql):
        '''
        执行修改，调用内部的__item()
        :param sql:              sql语句
        :return:                 受影响的行数
        '''

        return self.__item(sql)

    def close(self):
        '''
        关闭工具和连接对象
        '''
        if self.cur != None:
            self.cur.close()
        if self.conn != None:
            self.conn.close()