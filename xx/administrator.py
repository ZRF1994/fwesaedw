# -*- coding: utf-8 -*-
# @Time    : 2019/12/25 10:01
# @Author  : 张茹飞
# @Email   : 1106815482@qq.com
# @File    : administrator.py
# @Software: PyCharm


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QApplication
import sys
import sql_class
date = sql_class.Mysqlpython()
regedit_account = []
regedit_password = []
regedit_remark = []
account_n=0
account_number=0
def opersql(sql_insert):

    date.Operation(sql_insert)
def Search(sqlsearch):
    return  date.Search(sqlsearch)
def add():
    pass

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(919, 657)
        self.dialog=Dialog
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem2 = QtWidgets.QSpacerItem(87, 32, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        spacerItem3 = QtWidgets.QSpacerItem(87, 32, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        spacerItem4 = QtWidgets.QSpacerItem(87, 32, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        spacerItem5 = QtWidgets.QSpacerItem(87, 32, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "账号审批"))
        self.pushButton_2.setText(_translate("Dialog", "上一条"))
        self.pushButton_3.setText(_translate("Dialog", "下一条"))
        self.pushButton_4.setText(_translate("Dialog", "同意"))
        self.pushButton_5.setText(_translate("Dialog", "不同意"))
        self.pushButton.setText(_translate("Dialog", "退出"))
        self.Obtain()

        self.pushButton_5.clicked.connect(self.Dele)
        self.pushButton_4.clicked.connect(self.Add)
        print(account_n)
        self.pushButton_3.clicked.connect(self.Previous)
        self.pushButton_2.clicked.connect(self.Next)
        self.pushButton.clicked.connect(self.go_main)
        #如果有账户，显示第一条


        if len(regedit_account)!=0:

            account_number=len(regedit_account)
            print(account_number)
            self.textBrowser.setText("第"+str(1)+"条," + "  共"+str(account_number)+"条"+"\n"+
                                        "账号"+regedit_account[0]+"\n"+
                                     "申请信息"+regedit_remark[0]+'\n')
        else:
            self.textBrowser.setText("无消息")
    def go_main(self):
        self.dialog.close()
#管理员查看申请为教师的账户，单条显示
    def Previous(self):#上一条信息
        global account_n

        if len(regedit_account)!=0:
            account_number=len(regedit_account)
            if account_n<account_number-1:
                account_n += 1
                self.textBrowser.setText("第"+str(account_n+1)+"条," + "  共"+str(account_number)+"条"+"\n"+
                                        "账号" + regedit_account[account_n] + "\n"+
                                         "申请信息" + regedit_remark[0] + '\n')

                print(account_number)
            else:
                pass
    def Next(self):
        global account_n
        if len(regedit_account) != 0:
            account_number = len(regedit_account)
            if account_n !=0:
                account_n -= 1
                self.textBrowser.setText("第"+str(account_n+1)+"条," + "  共"+str(account_number)+"条"+"\n"+
                                         "账号" + regedit_account[account_n] + "\n" +
                                         "申请信息" + regedit_remark[0] + '\n')
            else:
                pass
    def Add(self):
        global account_n
        if len(regedit_account) != 0:
            print(account_n, len(regedit_account), regedit_account[account_n])
            sql = "INSERT INTO account(account1,password,accounttype) VALUES ('%s','%s','教师')" % ( regedit_account[account_n], regedit_password[account_n] )
            opersql(sql)
            sql_ = "DELEte FROM regedit where account = " + "\'" + regedit_account[account_n] + "\'"
            opersql(sql_)


            self.Obtain()
            try:
                account_n = 0
                if len(regedit_account) != 0:
                    account_number = len(regedit_account)
                    self.textBrowser.setText(
                        "第" + str(account_n + 1) + "条," + "  共" + str(account_number) + "条" + "\n" +
                        "账号：" + regedit_account[account_n] + "\n" +
                        "申请信息：" + regedit_remark[account_n] + '\n')
                else:
                    self.textBrowser.setText("无消息")
            except:
                self.textBrowser.setText("第" + str(1) + "条," + "  共" + str(1) + "条" + "\n" +
                                         "账号：" + regedit_account[account_n] + "\n" +
                                         "申请信息：" + regedit_remark[account_n] + '\n')
        else:
            print("遇到错误")
    def Dele(self):
        global account_n
        if len(regedit_account)!=0:
            print(account_n,len(regedit_account),regedit_account[account_n])
            sql_ ="DELEte FROM regedit where account = "+"\'"+regedit_account[account_n]+"\'"
            print("已删除")
            opersql(sql_)
            self.Obtain()
            try:
                account_n=0
                if len(regedit_account) != 0:
                    account_number = len(regedit_account)
                    self.textBrowser.setText("第" + str(account_n + 1) + "条," + "  共" + str(account_number) + "条" + "\n" +
                                             "账号：" + regedit_account[account_n] + "\n" +
                                             "申请信息：" + regedit_remark[account_n] + '\n')
                else:
                    self.textBrowser.setText("无消息")
            except:
                self.textBrowser.setText("第" + str(1) + "条," + "  共" + str(1) + "条" + "\n" +
                                         "账号：" + regedit_account[account_n ] + "\n" +
                                         "申请信息：" + regedit_remark[account_n ] + '\n')
        else:
            print("遇到错误")
    def Obtain(self):#从数据库中获取申请为教师的账号信息
        regedit_account.clear()
        regedit_password.clear()
        regedit_remark.clear()
        sql_account =Search("SELECT account,password,remark FROM regedit")
        regedit_information=list(sql_account)
        ss=[]
        for i in regedit_information:#每个元素转为列表
            ss.append(list(i))
        for i in ss:
            regedit_account.append(i[0])
        for i in ss:
            regedit_password.append(i[1])
        for i in ss:
            regedit_remark.append(i[2])










    def go_main(self):
        self.dialog.close()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QtWidgets.QDialog()
    form.setWindowFlags(
        QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMaximizeButtonHint)
    ui = Ui_Dialog()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())


