
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets

class RES(QtWidgets.QMainWindow):

    def __init__(self,q,e,r,t,y,u,v,ccc,wf):
        print("insidde")
        self.qq=q
        self.cclassifier=ccc
        self.wff=wf
        self.qq="Accuracy:  " + str(self.qq)
        self.ee=e
        self.rr=r
        self.tt=t
        self.yy=y
        self.uu=u
        self.vv=v

        self.ee = 'F-measure [negative]: ' + str(self.ee)
        self.rr = 'F-measure [positive]:' + str(self.rr)
        self.tt ='Precision [negative]:'  + str(self.tt)
        self.yy = 'Precision [positive]:'+ str(self.yy)
        self.uu = 'Recall [negative]:'+ str(self.uu)
        self.vv = 'Recall [positive]:' + str(self.vv)

        print(self.qq)
        self.listt=[]
        self.listt.append(self.qq)
        self.listt.append(self.ee)
        self.listt.append(self.rr)
        self.listt.append(self.tt)
        self.listt.append(self.yy)
        self.listt.append(self.uu)
        self.listt.append(self.vv)
        print(self.listt)
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
        self.TSA_label = QtWidgets.QLabel(self.centralwidget)
        self.TSA_label.setGeometry(QtCore.QRect(155, -5, 466, 76))
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
        self.label_MAINLINE.setGeometry(QtCore.QRect(310, 70, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_MAINLINE.setFont(font)
        self.label_MAINLINE.setStyleSheet("color: rgb(0,0,0);")
        self.label_MAINLINE.setObjectName("label_MAINLINE")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 150, 341, 361))
        self.listWidget.setStyleSheet("background-color: rgb(121, 255, 251);\n"
"background-color: rgb(98, 187, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(170, 0, 0);")
        self.listWidget.setObjectName("listWidget")
        self.label_MAINLINE_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_MAINLINE_2.setGeometry(QtCore.QRect(80, 110, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_MAINLINE_2.setFont(font)
        self.label_MAINLINE_2.setStyleSheet("color: rgb(0, 0,0);")
        self.label_MAINLINE_2.setObjectName("label_MAINLINE_2")
        self.label_MAINLINE_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_MAINLINE_3.setGeometry(QtCore.QRect(450, 240, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_MAINLINE_3.setFont(font)
        self.label_MAINLINE_3.setStyleSheet("color: rgb(0,0,0);")
        self.label_MAINLINE_3.setObjectName("label_MAINLINE_3")
        self.BUTTON_LOAD = QtWidgets.QPushButton(self.centralwidget)
        self.BUTTON_LOAD.setGeometry(QtCore.QRect(490, 310, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BUTTON_LOAD.setFont(font)
        self.BUTTON_LOAD.setStyleSheet("color: rgb(0,0,0);\n"
"background-color: rgb(93, 78, 255);")
        self.BUTTON_LOAD.setObjectName("BUTTON_LOAD")
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
        self.TSA_label.setText(_translate("MainWindow", "Twitter Sentiment Analysis"))
        self.label_MAINLINE.setText(_translate("MainWindow", "OUTPUT"))
        self.label_MAINLINE_2.setText(_translate("MainWindow", "TRAINING SET PERFORMANCE"))
        self.label_MAINLINE_3.setText(_translate("MainWindow", "CLICK HERE FOR RESULT"))
        self.BUTTON_LOAD.setText(_translate("MainWindow", "LOAD"))
        self.BUTTON_LOAD.clicked.connect(self.plot)
        for data in self.listt:
            print("heere")
            print(data)
            self.listWidget.addItem(str(data))
        self.func()
    def func(self):
        import pandas as pd
        import numpy as np
        import pickle
        import string
        import re

        # LOADING CLASSIFIER

        '''
        if getattr(sys, 'frozen', False):
            # if you are running in a |PyInstaller| bundle
            extDataDir = sys._MEIPASS
            extDataDir = os.path.join(extDataDir, 'classifier_features.pickle')
            # you should use extDataDir as the path to your file Store_Codes.csv file
        else:
            # we are running in a normal Python environment
            extDataDir = os.getcwd()
            extDataDir = os.path.join(extDataDir, 'classifier_features.pickle')

        # LOADING THE LIST OF FEATURES USED IN THE CLASSIFIER
        with open(extDataDir, 'rb') as f:
            word_features = pickle.load(f)
        '''
        classifier=self.cclassifier
        word_features=self.wff
        # FEATURE EXTRACTOR

        def extract_features(Tweet):
            filtered_tweet_words = set(Tweet)

            # CREATES A EMPTY FEATURE DICTIONARY
            features = {}

            for word in word_features:
                # 'contains(word_feature)' IS A KEY FOR THE DICTIONARY
                features['contains(%s)' % str(word)] = (word in filtered_tweet_words)
                # IN FUNCTION WILL RETURN EITHER TRUE OR FALSE

            return features

        # initialize stopWords
        stopWords = []

        # start replaceTwoOrMore
        def replaceTwoOrMore(s):
            # look for 2 or more repetitions of character and replace with the character itself
            pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
            return pattern.sub(r"\1\1", s)

        # start getStopWordList   THIS WILL LOAD ALL THE STOP WORDS FROM THE STOPWORDLIST FILE
        def getStopWordList(stopWordListFileName):
            # read the stopwords file and build a list
            stopWords = []
            stopWords.append('AT_USER')
            stopWords.append('URL')

            fp = open(stopWordListFileName, 'r')
            line = fp.readline()
            while line:
                word = line.strip()
                stopWords.append(word)
                line = fp.readline()
            fp.close()
            return stopWords

        def processTweet(tweet):
            # process the tweets

            # Convert to lower case
            tweet = tweet.lower()
            # Convert www.* or https?://* to URL
            tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)
            # Convert @username to AT_USER
            tweet = re.sub('@[^\s]+', 'AT_USER', tweet)
            # Remove additional white spaces
            tweet = re.sub('[\s]+', ' ', tweet)
            # Replace #word with word
            tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
            # trim
            tweet = tweet.strip('\'"')
            return tweet

        # start getfeatureVector
        def getFeatureVector(tweet):
            featureVector = listvector
            # split tweet into words
            words = tweet.split()
            for w in words:
                # replace two or more with two occurrences
                w = replaceTwoOrMore(w)
                # strip punctuation
                w = w.strip('\'"?,.')
                # check if the word stats with an alphabet
                val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
                # ignore if it is a stop word
                if (w in stopWords or val is None):
                    continue
                else:
                    featureVector.append(w.lower())
            return featureVector

        # end

        # Read the tweets one by one and process it
        import sys
        import os
        if getattr(sys, 'frozen', False):
            # if you are running in a |PyInstaller| bundle
            extDataDir = sys._MEIPASS
            extDataDir = os.path.join(extDataDir, 'output.txt')
            # you should use extDataDir as the path to your file Store_Codes.csv file
        else:
            # we are running in a normal Python environment
            extDataDir = os.getcwd()
            extDataDir = os.path.join(extDataDir, 'output.txt')
        fp = open(extDataDir, 'r')
        line = fp.readline()

        if getattr(sys, 'frozen', False):
            # if you are running in a |PyInstaller| bundle
            extDataDir = sys._MEIPASS
            extDataDir = os.path.join(extDataDir, 'stop.txt')
            # you should use extDataDir as the path to your file Store_Codes.csv file
        else:
            # we are running in a normal Python environment
            extDataDir = os.getcwd()
            extDataDir = os.path.join(extDataDir, 'stop.txt')
        st = open(extDataDir, 'r')
        stopWords = getStopWordList(extDataDir)
        listvector = []
        x = 0
        y = 0
        while line:
            if (line == "THIS IS TWEET\n"):
                filtered_text = listvector
                print("--------THE FILTERED TEXT ------------- \n ")
                #print(filtered_text)
                # Evaluate the contains(word) statements EXTRACTS OUR TWEET FEATURES
                tweet_feats = extract_features(filtered_text)
                print("--------TWEET FEATURE ------------- \n ")
                #print(tweet_feats)
                # Add result to new sentimenet column in the dataframe
                # print("THE SENTIMENT IS  " + classifier.classify(tweet_feats))
                if (classifier.classify(tweet_feats) == "positive"):
                    x = x + 1
                else:
                    y = y + 1

                listvector = []
            else:
                if (line != '\n' and line != "THIS IS TWEET\n"):
                    processedTweet = processTweet(line)
                    featureVector = getFeatureVector(processedTweet)
                    '''
                    for x in featureVector:
                        print(x)
                        listvector.append(x)
                    '''

            line = fp.readline()
        # end loop
        fp.close()
        print("NUMBER OF POSITVE TWEETS")
        print(x)
        print("NUMBER OF NEGATIVE TWEETS")
        print(y)
        self.xx=x
        self.yy=y
        print("------------------------")



    def plot(self):
        # plotting of result
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = 'POSITIVE', 'NEGATIVE', 'NEUTRAL'
        sizes = [self.xx, self.yy, 0]
        explode = (0.1, 0.1, 0.1)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')

        plt.show()

'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = RES()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

'''

