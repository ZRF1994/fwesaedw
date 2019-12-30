# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 17:21
# @Author  : 张茹飞
# @Email   : 1106815482@qq.com
# @File    : download.py
# @Software: PyCharm
import sql_class
def write_file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)
    f.close()
data=sql_class.Mysqlpython()
result = data.Search(sql="SELECT ansswer FROM questionbank where id=11")
write_file(result[0][0], "xdd1111111ddx.pdf")

