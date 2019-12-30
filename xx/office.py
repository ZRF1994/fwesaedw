import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyPDF2 import PdfFileReader, PdfFileWriter



class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)



    def get_info(self):
        path = 'xdd1111111ddx.pdf'
        filename, filetype = QFileDialog.getOpenFileName(self, 'Open file')
        with open(filename, 'rb') as f:
            pdf = PdfFileReader(f)
            info = pdf.getDocumentInfo()
            number_of_pages = pdf.getNumPages()

        print(number_of_pages)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())