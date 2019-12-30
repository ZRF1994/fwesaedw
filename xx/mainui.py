from PyQt5.QtWidgets import QMainWindow,  QApplication
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import sql_class
import administrator
import student
import teachers
date = sql_class.Mysqlpython()
def opersql(sql_insert):
    date.Operation(sql_insert)
def Search(sqlsearch):
    return  date.Search(sqlsearch)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        self.form = MainWindow
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(120, 30))
        self.pushButton_4.setMaximumSize(QtCore.QSize(120, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_5.addWidget(self.pushButton_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMinimumSize(QtCore.QSize(48, 0))
        self.label_5.setMaximumSize(QtCore.QSize(120, 48))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(120, 30))
        self.pushButton_5.setMaximumSize(QtCore.QSize(120, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_5.addWidget(self.pushButton_5)
        self.gridLayout.addLayout(self.horizontalLayout_5, 6, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(True)
        self.label_2.setMinimumSize(QtCore.QSize(50, 25))
        self.label_2.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(120, 25))
        self.lineEdit.setMaximumSize(QtCore.QSize(120, 25))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(50, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.horizontalLayout_4, 5, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(50, 25))
        self.label_4.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setEchoMode(2)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(120, 25))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(120, 25))
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(50, 25))
        self.label_3.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setMinimumSize(QtCore.QSize(120, 25))
        self.comboBox.setMaximumSize(QtCore.QSize(120, 25))
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(120, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(120, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_6.addWidget(self.pushButton_3)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(200, 30))
        self.textEdit.setMaximumSize(QtCore.QSize(120, 30))
        self.textEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_6.addWidget(self.textEdit)
        self.gridLayout.addLayout(self.horizontalLayout_6, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(400, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1400, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_4.setText(_translate("MainWindow", "2"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_5.setText(_translate("MainWindow", "3"))
        self.label_2.setText(_translate("MainWindow", "账号"))
        self.pushButton.setText(_translate("MainWindow", "注册"))
        self.pushButton_2.setText(_translate("MainWindow", "登录"))
        self.label_4.setText(_translate("MainWindow", "密码"))
        self.label_3.setText(_translate("MainWindow", "类型"))
        self.pushButton_3.setText(_translate("MainWindow", "1"))
        self.textEdit.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">备注:答疑者在此处填写申请信息</p></body></html>"))
        self.label.setText(_translate("MainWindow", "欢迎登录智能答疑系统"))
        self.pushButton_3.setVisible(False)
        self.pushButton_4.setVisible(False)
        self.pushButton_5.setVisible(False)
        self.comboBox.addItem("学生")
        self.comboBox.addItem("教师")
        self.comboBox.addItem("管理员")
        self.label_5.setVisible(False)#控件隐藏
        self.pushButton.clicked.connect(self.regedit_button)#注册按键监听
        self.pushButton_2.clicked.connect(self.log_in)  # 登录按键监听
    '''
该函数主要向数据库中添加注册人员账号，学生账号可以直接注册，
老师注册后需要提交申请，待管理员审核
管理员账号不允许注册
'''

    def jump_to_administrator(self):
        self.form.hide()
        form2 = QtWidgets.QDialog()
        form2.setWindowFlags(
            QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMaximizeButtonHint)
        ui = administrator.Ui_Dialog()
        ui.setupUi(form2)
        form2.show()
        form2.exec_()
        self.form.show()
    def jump_to_student(self):
        self.form.hide()
        form2 = QtWidgets.QDialog()
        form2.setWindowFlags(
            QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMaximizeButtonHint)
        ui = student.Ui_Dialog()
        ui.setupUi(form2)
        form2.show()
        form2.exec_()
        self.form.show()
    def jump_to_teachers(self):
        self.form.hide()
        form2 = QtWidgets.QDialog()
        form2.setWindowFlags(
            QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMaximizeButtonHint)
        ui = teachers.Ui_Dialog()
        ui.setupUi(form2)
        form2.show()
        form2.exec_()
        self.form.show()

    def regedit_button(self):

          #获取输入文本
        account  = self.lineEdit.text()
        password = self.lineEdit_2.text()
        account_type=self.comboBox.currentText()
        remark  = self.textEdit.toPlainText()
        if len(account)!=0  and len(password)!=0:#检查是否输入为空
            if account_type=="管理员":
                self.label_5.setVisible(True)
                self.label_5.setText("禁止注册为管理员")

            if account_type=="学生":
                #查询账号是否存在
                ss = []
                sql_account=Search("SELECT account1 FROM account")
                for i in list(sql_account):
                    ss.append(list(i)[0])
                if account in ss:
                    self.label_5.setVisible(True)
                    self.label_5.setText("账号已存在")
                else:
                    sql = "INSERT INTO account(account1,password,accounttype) VALUES ('%s','%s','%s')"%(account,password,account_type)
                    opersql(sql)
                    self.label_5.setVisible(True)
                    self.label_5.setText("注册成功")
            if account_type=="教师":
                ss = []
                sql_account = Search("SELECT account1 FROM account")
                for i in list(sql_account):
                    ss.append(list(i)[0])

                if account in ss:
                    self.label_5.setVisible(True)
                    self.label_5.setText("账号已存在")

                else:
                    sql = "INSERT INTO regedit(account,password,remark) VALUES ('%s','%s','%s')" % (
                    account, password, remark)
                    opersql(sql)
                    self.label_5.setVisible(True)
                    self.label_5.setText("注册完成，待审核")
        else:
            self.label_5.setVisible(True)
            self.label_5.setText("请输入账号和密码")
    '''
        该函数主要实现检查账号和密码是否相同
        '''
    def log_in(self):
        account = self.lineEdit.text()
        password = self.lineEdit_2.text()
        account_type = self.comboBox.currentText()
        remark = self.textEdit.toPlainText()
        if len(account)!=0 and len(password)!=0:
            xxx=[]#获取密码
            sql_account = Search("SELECT password, accounttype FROM account where (account1='%s')"%(account))
            try:
                for i in list(sql_account):
                    xxx.append(list(i))
                xxx=xxx[0]
                if password==xxx[0] and account_type==xxx[1]:
                    self.label_5.setVisible(True)
                    self.label_5.setText("正在登录")
                    if account_type=="学生":
                        self.jump_to_student()
                    if account_type=="教师":
                        self.jump_to_teachers()
                    if account_type=="管理员":
                        self.jump_to_administrator()

                else:
                    self.label_5.setVisible(True)
                    self.label_5.setText("账号或密码错误1")
            except Exception :
                self.label_5.setVisible(True)
                self.label_5.setText("账号或密码错误2")
        else:
            self.label_5.setVisible(True)
            self.label_5.setText("请输入账号和密码3")
if __name__ == '__main__':

    app=QApplication(sys.argv)
    winndow=QMainWindow()
    winndow.setWindowFlags( QtCore.Qt.WindowMinimizeButtonHint|QtCore.Qt.WindowCloseButtonHint|QtCore.Qt.WindowMaximizeButtonHint)
    #winndow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
    ui=Ui_MainWindow()
    ui.setupUi(winndow)
    winndow.show()
    sys.exit(app.exec_())
