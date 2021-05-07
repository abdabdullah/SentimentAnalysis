from PyQt5 import QtCore, QtWidgets, QtGui
import searchscreen
from PyQt5.QtWidgets import QFileDialog
import json
import re
import tweepy
from tweepy import OAuthHandler
import sanalyser

import csv

ckey = 'lnLzHXLDvyxgLFSTpUGERWxNx'
csecret = 'L1In42TVUnBZx0oOr4yncAwgZxQ2CIuCdNcMSpXyYwwqfdz16X'
atoken = '1009323315779944448-0Fcp5egiTp1xeHGRguBdq82mIgV6iK'
asecret = 'Eja23RrzKmwNfbLjQ2bGpCbgQowNN6TquekNqrVNI9dfX'
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)


class Tweetss(QtWidgets.QMainWindow):
    def __init__(self, x):
        self.xx = x
        print("INSIDE SAVEF")
        print(self.xx)
        QtWidgets.QMainWindow.__init__(self)

        self.setupUi(self)
        self.confirm = None

    def saveInput(self, newtweet):

        # name = QtWidgets.QFileDialog.getSaveFileName(MainWindow, "Save File", 'C://Users//USER//PycharmProjects//DataAnalysiS//output', '.txt')[0]
        import os
        o = os.path.dirname(os.path.abspath(__file__)) + "\output.txt"
        name = o
        print(name)
        file = open(name, 'a+')
        text = newtweet
        file.write("THIS IS TWEET\n")
        file.write(text)
        file.close()
        self.flag = 0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Form")
        MainWindow.resize(720, 575)
        MainWindow.setStyleSheet("background:rgb(69, 255, 224)rgb(129, 232, 255)rgb(166, 217, 255)\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # neww

        self.TSA_label = QtWidgets.QLabel(self.centralwidget)
        '''
        self.centralwidget = QtWidgets.QWidget(QtWidgets)
        self.centralwidget.setObjectName("centralwidget")
        '''
        self.TSA_label.setGeometry(QtCore.QRect(155, -5, 446, 66))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(24)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.TSA_label.setFont(font)
        self.TSA_label.setStyleSheet("color:rgb(46, 39, 255);")
        self.TSA_label.setObjectName("TSA_label")
        self.label_MAINLINE = QtWidgets.QLabel(self.centralwidget)
        self.label_MAINLINE.setGeometry(QtCore.QRect(20, 50, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_MAINLINE.setFont(font)
        self.label_MAINLINE.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_MAINLINE.setObjectName("label_MAINLINE")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(15, 91, 691, 391))
        self.listWidget.setStyleSheet("background-color: rgb(121, 255, 251);\n"
                                      "background-color: rgb(98, 187, 255);\n"
                                      "font: 75 11pt \"MS Shell Dlg 2\";\n"
                                      "color: rgb(170, 0, 0);")
        self.listWidget.setObjectName("listWidget")
        self.button_back = QtWidgets.QPushButton(self.centralwidget)
        self.button_back.setGeometry(QtCore.QRect(160, 510, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button_back.setFont(font)
        self.button_back.setStyleSheet("color: rgb(0, 0, 0);\n"
                                       "background-color: rgb(93, 78, 255);")
        self.button_back.setObjectName("button_back")
        self.button_proceed = QtWidgets.QPushButton(self.centralwidget)
        self.button_proceed.setGeometry(QtCore.QRect(450, 510, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button_proceed.setFont(font)
        self.button_proceed.setStyleSheet("color: rgb(0, 0, 0);\n"
                                          "background-color: rgb(93, 78, 255);")
        self.button_proceed.setObjectName("button_proceed")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 431, 21))
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
        self.TSA_label.setText(_translate("Form", "Twitter Sentiment Analysis"))
        self.label_MAINLINE.setText(_translate("Form", "TWEETS"))
        self.button_back.setText(_translate("Form", "BACK"))
        self.button_proceed.setText(_translate("Form", "PROCEED"))
        self.button_back.clicked.connect(self.goback)
        self.button_proceed.clicked.connect(self.proceedd)
        self.func()

    def func(self):
        try:
            print(self.xx)
            searchquery = []
            searchquery = self.xx.split(",")
            print(searchquery)

            for str in searchquery:
                print(str)
                if (str[0] != '#'):
                    str = "#" + str

            print(searchquery)
            a = ""
            for i in searchquery:
                a = a + i + " AND "

            print(a)
            a = (a[0:-5])

            print(a)
            query = a

            f = 0
            text = ""
            listt = []
            limit = 1000
            import os
            o = os.path.dirname(os.path.abspath(__file__)) + "\opp.csv"
            csvFile = open(o, 'a')
            print("CSV FILE LOADED")
            print(query)
            # Use csv Writer
            csvWriter = csv.writer(csvFile)
            # Iterate through Twitter using Tweepy
            for tweet in tweepy.Cursor(api.search, q=query, language="en", tweet_mode='extended', count=200,
                                       since="2017-04-03").items(limit):
                if f == 100:
                    break
                else:
                    print(tweet.created_at)
                    csvWriter.writerow([tweet.created_at, tweet.full_text.encode('utf-8')])
                    print("f ====  ")
                    print(f)
                    if 'retweeted_status' in dir(tweet):
                        tweet = tweet.retweeted_status.full_text
                    else:
                        tweet = tweet.full_text
                    # print(tweet)
                    print("****************")
                    f = f + 1
                    newtweet = ""
                    # TO REMOVE SPECIAL CHARACTERS FROM TWEET
                    for k in tweet.split("\n"):
                        k = re.sub(r"[^a-zA-Z#./: ]+", '', k)
                        newtweet = newtweet + k + "\n"

                    newtweet = newtweet + "\n-------------------------------------\n"
                    newtweet.lower()
                    print("length")
                    print(len(newtweet))
                    if len(newtweet) > 100:
                        listt.append(newtweet)
                        # STORING TWEETS IN A FILE
                        try:

                            self.saveInput(newtweet)


                        except:
                            print("OUTISDE")
                            pass
            self.countt = len(listt)
            listt=list(set(listt))
            self.count=len(listt)
            print("BEFORE")
            print(self.countt)
            print("AFTER")
            print(self.count)
            for data in listt:
                print(data)
                self.listWidget.addItem(data)

            print(listt)
        except:
            self.flag=1
            QtWidgets.QMessageBox.warning(self, 'ERROR', 'CHECK YOUR INTERNET CONNECTION')
            self.close()

    def goback(self):
        self.entered = searchscreen.search()
        self.entered.show()
        self.close()

    def proceedd(self):
        print("======")
        if(self.flag==0):
            self.entered = sanalyser.analyse()
            self.entered.show()
            self.close()

    def rx(self, x):
        print(self.x)
        return self.x


'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tweetss()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
'''