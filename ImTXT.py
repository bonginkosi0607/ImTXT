import os
import sys
import subprocess
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

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QRect(200, 130, 88, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.oncl)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QRect(10, 170, 481, 431))
        self.textBrowser.setObjectName("textBrowser")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def oncl(self):
        file_ = askopenfilename(title="Image Only ")
        self.textBrowser.setText("reading...")
        process = subprocess.Popen([r'python', "./hh.py", file_],\
         stdout = subprocess.PIPE, stdin = subprocess.PIPE)
        res = str(process.stdout.read()).replace("\\n", "\n").replace("b'", "")\
         .replace("\n", "").replace("\\x0c\\x0c", "").replace("\\x0c", "\n *** \n")
        self.textBrowser.setText(res.strip())

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Upload"))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
