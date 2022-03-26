import os
import cv2
import pytesseract
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from tkinter.filedialog import askopenfilename, asksaveasfilename


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(502, 609)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(180, 80, 131, 71))
        self.label.setText("")
        self.label.setPixmap(QPixmap("icon.png"))
        self.label.setObjectName("label")

        self.btn = QPushButton(self.centralwidget)
        self.btn.setGeometry(QRect(200, 130, 88, 27))
        self.btn.setObjectName("pushButton")

        self.output = QTextBrowser(self.centralwidget)
        self.output.setGeometry(QRect(10, 170, 481, 431))
        self.output.setObjectName("textBrowser")


        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ImTXT"))
        self.btn.setText(_translate("MainWindow", "Upload"))
   


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
