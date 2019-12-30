# -*- coding: utf-8 -*-
# @Time    : 2019/12/24 1:54
# @Author  : 张茹飞
# @Email   : 1106815482@qq.com
# @File    : sql_class.py
# @Software: PyCharm

from pymysql import *

class Mysqlpython:
    def __init__(self, database='test', host='101.37.66.88', user="root",password='aszwaszw', port=3306, charset="utf8"):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database = database
        self.charset = charset# 数据库连接方法:
    def open(self):
        self.db = connect(host=self.host, user=self.user,password=self.password, port=self.port,database=self.database,charset=self.charset)# 游标对象
        self.cur = self.db.cursor()# 数据库关闭方法:
    def close(self):
        self.cur.close()
        self.db.close()# 数据库执行操作方法:
    def Operation(self, sql):
        try:
            self.open()
            self.cur.execute(sql)
            self.db.commit()

        except  Exception as e :
            self.db.rollback()

            self.close()# 数据库查询所有操作方法:

    def Search(self, sql):
        try:
            self.open()
            self.cur.execute(sql)
            result = self.cur.fetchall()

            return result
        except Exception as e:
            print("Failed", e)
            self.close()