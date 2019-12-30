# -*- coding: utf-8 -*-
# @Time    : 2019/12/25 11:32
# @Author  : 张茹飞
# @Email   : 1106815482@qq.com
# @File    : student.py
# @Software: PyCharm

from PyQt5.QtWidgets import  QApplication
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import sql_class
data=sql_class.Mysqlpython()
obtinfromsql=[]
strkey=''
questionandanswer=[]
questionandanswer_number=0
account_n=0
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1421, 840)
        Dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.dialog=Dialog
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setMinimumSize(QtCore.QSize(500, 50))
        self.textEdit.setMaximumSize(QtCore.QSize(500, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.textEdit.setFont(font)
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setMinimumSize(QtCore.QSize(700, 500))
        self.textBrowser_2.setMaximumSize(QtCore.QSize(700, 500))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayout_3.addWidget(self.textBrowser_2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setMinimumSize(QtCore.QSize(700, 150))
        self.textEdit_2.setMaximumSize(QtCore.QSize(700, 150))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout_2.addWidget(self.textEdit_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setMinimumSize(QtCore.QSize(130, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setMinimumSize(QtCore.QSize(130, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setMinimumSize(QtCore.QSize(130, 30))
        self.pushButton_4.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setMinimumSize(QtCore.QSize(130, 30))
        self.pushButton_5.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_4.addWidget(self.pushButton_5)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "搜索"))
        self.textEdit_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">回复:</p></body></html>"))
        self.pushButton_2.setText(_translate("Dialog", "上一条"))
        self.pushButton_3.setText(_translate("Dialog", "下一条"))
        self.pushButton_4.setText(_translate("Dialog", "提交"))
        self.pushButton_5.setText(_translate("Dialog", "退出"))

        self.pushButton_5.clicked.connect(self.go_main)
        self.pushButton_4.clicked.connect(self.submit)
        self.pushButton_3.clicked.connect(self.Next)
        self.pushButton_2.clicked.connect(self.Previous)
        self.pushButton.clicked.connect(self.search)
    def go_main(self):
        self.dialog.close()
    def search(self):
        global obtinfromsql,strkey,questionandanswer,questionandanswer_number,account_n
        self.textEdit_2.setText("回复:")
        obtinfromsql = []
        strkey = ''
        questionandanswer = []
        questionandanswer_number = 0
        account_n = 0

        strkey=self.textEdit.toPlainText()
        print("点击搜索按钮",strkey)
        if len(strkey)!=0:
            xx=self.obtinAllData()
            for i in xx:
                if strkey in list(i)[1]:
                    questionandanswer.append(list(i))
            if len(questionandanswer)!=0:
                self.textBrowser_2.setText("第" + str(account_n + 1) + "条," + "  共" + str(len(questionandanswer)) + "条" + "\n" +"\n"+
                    questionandanswer[0][1]+"\n   "+questionandanswer[0][2].replace('\r\n\r\n\u3000\u3000',''))
            else:
                self.textBrowser_2.setText("未找到,已提交由老师作答")
                #todo 提交有老师答疑
                search = self.textEdit.toPlainText()
                print(search)
                sql = "INSERT INTO faq(question) VALUES ('%s')" % (search)
                data.Operation(sql)

        else:
            self.textBrowser_2.setText("请输入要搜索的词")
#上一条
    def Previous(self):  # 上一条信息
        global questionandanswer_number,account_n
        questionandanswer_number = len(questionandanswer)
        if questionandanswer_number != 0:
            if account_n !=0:
                account_n -= 1
                self.textBrowser_2.setText("第" + str(account_n + 1) + "条," + "  共" + str(len(questionandanswer)) + "条" + "\n" +"\n"+
                                         questionandanswer[account_n][1]+"\n   "+questionandanswer[account_n][2].replace('\r\n\r\n\u3000\u3000',''))
            else:
                pass
   #下一条
    def Next(self):
        global questionandanswer_number, account_n
        questionandanswer_number = len(questionandanswer)
        if questionandanswer_number != 0:
            if account_n < questionandanswer_number - 1:
                account_n += 1
                self.textBrowser_2.setText(
                    "第" + str(account_n + 1) + "条," + "  共" + str(len(questionandanswer)) + "条" + "\n" + "\n" +
                    questionandanswer[account_n][1] + "\n   " + questionandanswer[account_n][2].replace(
                        '\r\n\r\n\u3000\u3000', ''))
            else:
                pass
       #提交新答案，交于老师审核
    #
    def submit(self):
        global account_n,questionandanswer_number,questionandanswer

        if questionandanswer:#未找到答案，
            print("yes")
            search = questionandanswer[account_n][1]
            answer = self.textEdit_2.toPlainText()
            if len(answer)!=0and answer!="回复:"and len(search)!=0:
                print('补充', search, answer)
                #添加到临时回答数据库
                sql = "INSERT INTO faq(question,answer) VALUES ('%s','%s')" % ( search,answer)
                data.Operation(sql)
                self.textEdit_2.setText("提交完成")
        else:
            print('no')
            search = self.textEdit.toPlainText()  # 题目
            answer = self.textEdit_2.toPlainText()
            if len(answer)!=0and answer!="回复:"and len(search)!=0:
                print('添加', search, answer)
                sql = "INSERT INTO faq(question,answer) VALUES ('%s','%s')" % (search, answer)
                data.Operation(sql)
                print(sql)
                self.textEdit_2.setText("提交完成")
        #获取当前问题和答案， 进行提交
    def obtinAllData(self):
        global question
        global answer
        sqlData = list(data.Search("SELECT * FROM questionbank"))
        return sqlData
    #遇到空答案，老师解答
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QtWidgets.QDialog()
    form.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMaximizeButtonHint)
    ui = Ui_Dialog()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())