
from PyQt5 import QtCore, QtGui, QtWidgets
import savef
from PyQt5.QtWidgets import QMessageBox
class search(QtWidgets.QMainWindow):

    def __init__(self):

        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.confirm = None
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 575)
        MainWindow.setStyleSheet("background:rgb(69, 255, 224)rgb(129, 232, 255)rgb(166, 217, 255)\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(480, 220, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button.setFont(font)
        self.button.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(93, 78, 255);")
        self.button.setObjectName("button")
        self.TSA_label = QtWidgets.QLabel(self.centralwidget)
        self.TSA_label.setGeometry(QtCore.QRect(160, 20, 441, 81))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(24)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.TSA_label.setFont(font)
        self.TSA_label.setStyleSheet("color:rgb(46, 39, 255);")
        self.TSA_label.setObjectName("TSA_label")
        self.SEARCHBOX = QtWidgets.QTextEdit(self.centralwidget)
        self.SEARCHBOX.setGeometry(QtCore.QRect(80, 220, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.SEARCHBOX.setFont(font)
        self.SEARCHBOX.setStyleSheet("\n"
"background-color: rgb(202, 255, 242);")
        self.SEARCHBOX.setObjectName("SEARCHBOX")
        self.label_MAINLINE = QtWidgets.QLabel(self.centralwidget)
        self.label_MAINLINE.setGeometry(QtCore.QRect(80, 160, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_MAINLINE.setFont(font)
        self.label_MAINLINE.setStyleSheet("color: rgb(0, 0,0);")
        self.label_MAINLINE.setObjectName("label_MAINLINE")
        self.label_SECONDARY = QtWidgets.QLabel(self.centralwidget)
        self.label_SECONDARY.setGeometry(QtCore.QRect(80, 260, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_SECONDARY.setFont(font)
        self.label_SECONDARY.setStyleSheet("COLOR:rgb(0,0,0)\n"
"")
        self.label_SECONDARY.setObjectName("label_SECONDARY")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 21))
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
        self.button.setText(_translate("MainWindow", "SEARCH"))
        self.TSA_label.setText(_translate("MainWindow", "Twitter Sentiment Analysis"))
        self.SEARCHBOX.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:400;\"><br /></p></body></html>"))
        self.label_MAINLINE.setText(_translate("MainWindow", "SEARCH HASHTAGS FOR TWEEETS"))
        self.label_SECONDARY.setText(_translate("MainWindow", "(MULTIPLE HASHTAGS SEPARATED BY A COMMA)"))

        self.button.clicked.connect(self.searchquery)
        import os
        o=os.path.dirname(os.path.abspath(__file__))+"\output.txt"
        fName=open(o, 'w')
        fName.seek(0)
        fName.truncate()
        fName.close()
        o = os.path.dirname(os.path.abspath(__file__)) + "\opp.csv"
        fName = open(o, 'w')
        fName.seek(0)
        fName.truncate()
        fName.close()

    def searchquery(self):
        print("here")
        self.x= self.SEARCHBOX.toPlainText()
        print(self.x)
        if self.x== "":
            print("inside")
            QtWidgets.QMessageBox.warning(self, 'ERROR', 'EMPTY SEARCH QUERY')
        else:
            self.proceed= savef.Tweetss(self.rx(self.x))
            self.proceed.show()
            self.close()

    def rx(self, x):
        print(self.x)
        return self.x


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = search()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
