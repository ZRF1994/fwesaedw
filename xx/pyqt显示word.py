from PyQt5.QAxContainer import QAxWidget
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog, QMessageBox


class AxWidget(QWidget):


    def __init__(self, *args, **kwargs):
        super(AxWidget, self).__init__(*args, **kwargs)
        self.resize(800, 600)
        layout = QVBoxLayout(self)
        self.axWidget = QAxWidget(self)
        layout.addWidget(self.axWidget)
        layout.addWidget(QPushButton('选择excel,word,pdf文件',
                                     self, clicked=self.onOpenFile))

    def onOpenFile(self):
        path, _ = QFileDialog.getOpenFileName(
            self, '请选择文件', '', 'excel(*.xlsx *.xls);;word(*.docx *.doc);;pdf(*.pdf)')

        return self.openOffice('E:/pycharm/xx/xx.doc', 'KWPS.Application')  # word 的接口

        # return self.openOffice('E:/pycharm/xx/xsas.xlsx', 'ket.Application')  # excel的接口



    def openOffice(self, path, app):
        self.axWidget.clear()
        if not self.axWidget.setControl(app):
            return QMessageBox.critical(self, '错误', '没有安装  %s' % app)
        self.axWidget.dynamicCall(
            'SetVisible (bool Visible)', 'false')  # 不显示窗体
        self.axWidget.setProperty('DisplayAlerts', False)
        self.axWidget.setControl(path)
        self.axWidget.show()



    def closeEvent(self, event):
        self.axWidget.close()
        self.axWidget.clear()
        self.layout().removeWidget(self.axWidget)
        del self.axWidget
        super(AxWidget, self).closeEvent(event)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = AxWidget()
    w.show()
    sys.exit(app.exec_())
