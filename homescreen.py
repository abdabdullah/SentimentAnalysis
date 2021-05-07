# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homescreen.ui'
#
# Created by: PyQt5 UI code generator 5.9
#

# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import searchscreen

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 575)
        MainWindow.setStyleSheet("background:rgb(69, 255, 224)rgb(129, 232, 255)rgb(166, 217, 255)\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(280, 250, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button.setFont(font)
        self.button.setStyleSheet("color: rgb(0,0,0);\n"
"background-color: rgb(93, 78, 255);")
        self.button.setObjectName("button")
        self.TSA_label = QtWidgets.QLabel(self.centralwidget)
        self.TSA_label.setGeometry(QtCore.QRect(155, 80, 456, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(24)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.TSA_label.setFont(font)
        self.TSA_label.setStyleSheet("color:rgb(46, 39, 255);")
        self.TSA_label.setObjectName("TSA_label")
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
        self.button.setText(_translate("MainWindow", "ENTER"))
        self.TSA_label.setText(_translate("MainWindow", "Twitter Sentiment Analysis"))
        self.button.clicked.connect(self.go)

    def go(self):
        self.entered = searchscreen.search()
        self.entered.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


