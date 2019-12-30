# -*- coding: utf-8 -*-
# @Time    : 2019/12/25 11:32
# @Author  : 张茹飞
# @Email   : 1106815482@qq.com
# @File    : teachers.py
# @Software: PyCharm

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import sql_class
data=sql_class.Mysqlpython()
answer_question=[]
account_n=0
# self.dialog=Dialog
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1266, 850)
        self.dialog=Dialog
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setMinimumSize(QtCore.QSize(400, 600))
        self.textBrowser.setMaximumSize(QtCore.QSize(400, 600))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_3.addWidget(self.textBrowser)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setMinimumSize(QtCore.QSize(400, 600))
        self.textEdit.setMaximumSize(QtCore.QSize(400, 600))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_3.addWidget(self.textEdit)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setMinimumSize(QtCore.QSize(120, 25))
        self.pushButton_2.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setMinimumSize(QtCore.QSize(120, 25))
        self.pushButton.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setMinimumSize(QtCore.QSize(120, 25))
        self.pushButton_5.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setMinimumSize(QtCore.QSize(120, 25))
        self.pushButton_6.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setMinimumSize(QtCore.QSize(120, 25))
        self.pushButton_3.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setMinimumSize(QtCore.QSize(120, 25))
        self.pushButton_4.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 2)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem7, 1, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem8, 3, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem9, 5, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_2.setText(_translate("Dialog", "上一条"))
        self.pushButton.setText(_translate("Dialog", "下一条"))
        self.pushButton_5.setText(_translate("Dialog", "同意"))
        self.pushButton_6.setText(_translate("Dialog", "不同意"))
        self.pushButton_3.setText(_translate("Dialog", "提交答案"))
        self.pushButton_4.setText(_translate("Dialog", "退    出"))
        self.label.setText(_translate("Dialog", "教师答疑"))
        answer_question.clear()
        self.obtin()
        if len(answer_question)!=0:

            if answer_question[0][1] == None:
                self.textBrowser.setText(
                    "第" + str(account_n + 1) + "条，" + "共" + str(len(answer_question)) + "条" + '\n' +
                    "题目:       " + answer_question[account_n][0] + '\n' + "答案:       " + "无人作答")
            else:
                self.textBrowser.setText(
                    "第" + str(account_n + 1) + "条，" + "共" + str(len(answer_question)) + "条" + '\n' +
                    "题目:       " + answer_question[account_n][0] + '\n' + "答案:       " + answer_question[account_n][1])

        self.pushButton_4.clicked.connect(self.go_main)
        self.pushButton_2.clicked.connect(self.previous)
        self.pushButton.clicked.connect(self.Next)
        self.pushButton_5.clicked.connect(self.agree)
        self.pushButton_6.clicked.connect(self.reject)
        self.pushButton_3.clicked.connect(self.submit)

    #todo 获取所有faq的数据，并显示结果，
    def obtin(self):
        global answer_question
        answer_question.clear()
        sql_account = data.Search("SELECT question,answer FROM faq")
        regedit_information = list(sql_account)
        for i in regedit_information:
            answer_question.append(list(i))
        print(answer_question)
    def previous(self):
        global account_n
        if len(answer_question)!=0:
            if account_n != 0:
                account_n -= 1
                if answer_question[account_n][1]==None:
                    self.textBrowser.setText("第"+str(account_n+1)+"条，"+"共"+str(len(answer_question))+"条"+'\n'+
                        "题目:       " + answer_question[account_n][0] + '\n' + "答案:       " + "无人作答")
                else:
                    self.textBrowser.setText("第"+str(account_n+1)+"条，"+"共"+str(len(answer_question))+"条"+'\n'+
                        "题目:       " + answer_question[account_n][0] + '\n' + "答案:       " + answer_question[account_n][1])
            else:
                pass
    def Next(self):
        global  account_n
        if len(answer_question) != 0:
            if account_n < len(answer_question)-1:
                account_n += 1
                if answer_question[account_n][1]==None:
                    self.textBrowser.setText("第"+str(account_n+1)+"条，"+"共"+str(len(answer_question))+"条"+'\n'+
                        "题目:       " + answer_question[account_n][0] + '\n' + "答案:       " + "无人作答")
                else:
                    self.textBrowser.setText("第"+str(account_n+1)+"条，"+"共"+str(len(answer_question))+"条"+'\n'+
                        "题目:       " + answer_question[account_n][0] + '\n' + "答案:       " + answer_question[account_n][1])
            else:
                pass
    def agree(self):

        global account_n
        if len(answer_question) != 0:
            sql = "INSERT INTO questionbank(question,ansswer) VALUES ('%s','%s')" % (answer_question[account_n][0],answer_question[account_n][1] )

            print(sql)
            data.Operation(sql)

            sql = "DELEte FROM faq where question = '%s'" % answer_question[account_n][0]
            print(sql)
            data.Operation(sql)
            # 添加后刷新
            answer_question.clear()
            self.obtin()
            account_n = 0
            if len(answer_question) != 0:
                if answer_question[account_n][1] == None:
                    self.textBrowser.setText(
                        "第" + str(account_n + 1) + "条，" + "共" + str(len(answer_question)) + "条" + '\n' +
                        "题目:       " + answer_question[account_n][0] + '\n' + "答案:       " + "无人作答")
                else:
                    self.textBrowser.setText(
                        "第" + str(account_n + 1) + "条，" + "共" + str(len(answer_question)) + "条" + '\n' +
                        "题目:       " + answer_question[account_n][0] + '\n' + "答案:       " +
                        answer_question[account_n][1])
            else:
                self.textBrowser.setText("无消息")
        else:
            self.textBrowser.setText("无消息")
    def reject(self):
        global account_n
        if len(answer_question) != 0:
            sql = "DELEte FROM faq where question = '%s'" % answer_question[account_n][0]
            print(sql)
            data.Operation(sql)
            #删除后刷新
            answer_question.clear()
            self.obtin()
            account_n=0
            if len(answer_question)!=0:
                if answer_question[account_n][1] == None:
                    self.textBrowser.setText("第" + str(account_n + 1) + "条，" + "共" + str(len(answer_question)) + "条" + '\n' +
                                             "题目:       " + answer_question[account_n][0] + '\n' + "答案:       " + "无人作答")
                else:
                    self.textBrowser.setText("第" + str(account_n + 1) + "条，" + "共" + str(len(answer_question)) + "条" + '\n' +
                                             "题目:       " + answer_question[account_n][0] + '\n' + "答案:       " +
                                             answer_question[account_n][1])
            else:
                self.textBrowser.setText("无消息")
        else:
            self.textBrowser.setText("无消息")
    def submit(self):
        global account_n

        if answer_question:

                #有答案，覆盖

                if self.textEdit.toPlainText():
                    print("zhunb")
                    sql = "INSERT INTO questionbank(question,ansswer) VALUES ('%s','%s')" % ( answer_question[account_n][0], self.textEdit.toPlainText())
                    data.Operation(sql)
                    sql = "DELEte FROM faq where question = '%s'" % answer_question[account_n][0]
                    data.Operation(sql)
                    # 删除后刷新
                    answer_question.clear()
                    self.obtin()
                    account_n = 0
                    if len(answer_question) != 0:
                        if answer_question[account_n][1] == None:
                            self.textBrowser.setText(
                                "第" + str(account_n + 1) + "条，" + "共" + str(len(answer_question)) + "条" + '\n' +
                                "题目:       " + answer_question[account_n][0] + '\n' + "答案:       " + "无人作答")
                        else:
                            self.textBrowser.setText(
                                "第" + str(account_n + 1) + "条，" + "共" + str(len(answer_question)) + "条" + '\n' +
                                "题目:       " + answer_question[account_n][0] + '\n' + "答案:       " +
                                answer_question[account_n][1])
                    else:
                        self.textBrowser.setText("无消息")
                else:
                    self.textBrowser.setText("无消息")
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