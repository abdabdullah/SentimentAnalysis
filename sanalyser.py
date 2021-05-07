from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import *
import csv
import resultt
from PyQt5.QtWidgets import QMessageBox
import json
import nltk
from nltk.sentiment.util import mark_negation
from nltk.metrics import BigramAssocMeasures
from nltk.collocations import BigramCollocationFinder
import string
import itertools
import pandas as pd
from nltk.metrics import precision as prec
from nltk.metrics import recall as rec
from nltk.metrics import f_measure as fmeas
import collections


class analyse(QtWidgets.QMainWindow):
    def __init__(self):

        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.confirm = None
        self.q = 0
        self.e = 0
        self.r = 0
        self.t = 0
        self.y = 0
        self.u = 0
        self.v = 0
        self.pp = 0
        self.nn = 0
        self.fname = ""

    def sw(self):
        print("inside")
        fileName = QtWidgets.QFileDialog.getOpenFileName(None, "Save File", '', '')[0]
        self.textEdit.setText(fileName)
        self.fname = fileName

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 575)
        MainWindow.setStyleSheet("background:rgb(69, 255, 224)rgb(129, 232, 255)rgb(166, 217, 255)\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BUTTON_TRAIN = QtWidgets.QPushButton(self.centralwidget)
        self.BUTTON_TRAIN.setGeometry(QtCore.QRect(280, 410, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BUTTON_TRAIN.setFont(font)
        self.BUTTON_TRAIN.setStyleSheet("color: rgb(0, 0,0);\n"
                                        "background-color: rgb(93, 78, 255);")
        self.BUTTON_TRAIN.setObjectName("BUTTON_TRAIN")
        self.TSA_label = QtWidgets.QLabel(self.centralwidget)
        self.TSA_label.setGeometry(QtCore.QRect(158, -5, 459, 76))
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
        self.label_MAINLINE.setGeometry(QtCore.QRect(180, 80, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_MAINLINE.setFont(font)
        self.label_MAINLINE.setStyleSheet("color:rgb(0,0, 0);")
        self.label_MAINLINE.setObjectName("label_MAINLINE")
        self.radioButton_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_1.setGeometry(QtCore.QRect(210, 170, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_1.setFont(font)
        self.radioButton_1.setStyleSheet("color: rgb(0,0,0);")
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(210, 310, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("color: rgb(0,0,0);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(230, 220, 211, 31))
        self.textEdit.setStyleSheet("background-color: rgb(121, 255, 251);\n"
                                    "background-color: rgb(98, 187, 255);\n"
                                    "font: 75 10pt \"MS Shell Dlg 2\";\n"
                                    "color: rgb(170, 0, 0);")
        self.textEdit.setObjectName("textEdit")
        self.BUTTON_LOAD = QtWidgets.QPushButton(self.centralwidget)
        self.BUTTON_LOAD.setGeometry(QtCore.QRect(490, 220, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BUTTON_LOAD.setFont(font)
        self.BUTTON_LOAD.setStyleSheet("color: rgb(0,0,0);\n"
                                       "background-color: rgb(93, 78, 255);")
        self.BUTTON_LOAD.setObjectName("BUTTON_LOAD")
        self.label_SECONDARY = QtWidgets.QLabel(self.centralwidget)
        self.label_SECONDARY.setGeometry(QtCore.QRect(230, 260, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_SECONDARY.setFont(font)
        self.label_SECONDARY.setStyleSheet("COLOR:rgb(0,0,0)\n"
                                           "")
        self.label_SECONDARY.setObjectName("label_SECONDARY")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
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
        self.BUTTON_TRAIN.setText(_translate("MainWindow", "TRAIN"))
        self.TSA_label.setText(_translate("MainWindow", "Twitter Sentiment Analysis"))
        self.label_MAINLINE.setText(_translate("MainWindow", "TRAIN YOUR SENTIMENT ANALYSER"))
        self.radioButton_1.setText(_translate("MainWindow", "USE YOUR OWN TRAINING SET"))
        self.radioButton_2.setText(_translate("MainWindow", "USE DEFAULT TRAINING SET"))
        self.BUTTON_LOAD.setText(_translate("MainWindow", "LOAD"))
        self.label_SECONDARY.setText(_translate("MainWindow", "(ONLY CSV FILE)"))
        self.BUTTON_LOAD.clicked.connect(self.loadfile)
        self.BUTTON_TRAIN.clicked.connect(self.trainn)
        self.radioButton_1.toggled.connect(self.sw)

        # self.radioButton_2.toggled.connect(self.radio2_clicked)

    def trainn(self):
        if (self.radioButton_2.isChecked()):
            print("hey there ")
            self.train2()
            print("hey there ")
        if (self.radioButton_1.isChecked()):
            print("hey there ")
            self.train1()
            print("hey there ")

    def train1(self):
        try:
            import tweepy
            import csv

            """
            Created on Fri Jul  6 11:23:39 2018
    
            @author: DARAKSHA
            """
            import re

            import pandas as pd
            import nltk
            import matplotlib.pyplot as plt

            print("Fffa")

            def processTweet2(tweet):
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

                ###get stopword list

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

            import os
            stopWords = []
            o = os.path.dirname(os.path.abspath(__file__)) + "\stop.txt"
            st = open(o, 'r')
            stopWords = getStopWordList(o)
            print("Fafaafaf")

            def replaceTwoOrMore(s):
                # look for 2 or more repetitions of character and replace with the character itself
                pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
                return pattern.sub(r"\1\1", s)

            # end
            print("Fafaafaf")

            # sepearating the meaningful words
            def getFeatureVector(tweet):
                featureVector = []
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

            print("THIS IS THE FILE NAME")
            ###load airline sentiment training data
            print(self.fname)

            airlinetrain = pd.read_csv(self.fname,
                                       encoding="ISO-8859-1")
            print("READ THE FILE WITH EASE")
            tweets = []
            featureList = []
            for i in range(len(airlinetrain)):
                sentiment = airlinetrain['Sentiment'][i]
                tweet = airlinetrain['text'][i]
                processedTweet = processTweet2(tweet)
                featureVector = getFeatureVector(processedTweet)
                featureList.extend(featureVector)
                tweets.append((featureVector, sentiment))

            print("HERE")

            # tokenization of each words to get feature list
            def extract_features(tweet):
                tweet_words = set(tweet)
                features = {}
                for word in featureList:
                    features['contains(%s)' % word] = (word in tweet_words)
                return features

            # end
            print("fafnjana")
            ### Remove featureList duplicates
            featureList = list(set(featureList))

            training_set = nltk.classify.util.apply_features(extract_features, tweets)
            # Train the classifier Naive Bayes Classifier
            NBClassifier = nltk.NaiveBayesClassifier.train(training_set)

            # count of positive,negative and neutral tweets
            pos = 0
            neg = 0
            neu = 0
            import os
            # u1 is a dataframe containing all the united airline tweets
            o = os.path.dirname(os.path.abspath(__file__)) + "\opp.csv"
            u1 = pd.read_csv(o, header=0)

            # applying each tweets to naive bayes classifier
            for i in range(len(u1)):
                print("soneth")
                tweet = u1.iloc[i, 1]
                processedTweet = processTweet2(tweet)
                x = NBClassifier.classify(extract_features(getFeatureVector(processedTweet)))
                if (x == 'positive'):
                    pos += 1
                elif (x == 'negative'):
                    neg += 1
                else:
                    neu += 1

            print(pos)
            print(neg)
            print(neu)

            # plotting of result
            # Pie chart, where the slices will be ordered and plotted counter-clockwise:
            labels = 'POSITIVE', 'NEGATIVE', 'NEUTRAL'
            sizes = [pos, neg, neu]
            explode = (0.1, 0.1, 0.1)

            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            ax1.axis('equal')

            plt.show()
        except:
            QtWidgets.QMessageBox.warning(self, 'ERROR', 'PLEASE MAKE SURE YOUR CSV FILE HAVE A Sentiment AND text COLUMN')


    def train2(self):
        # LOADING OUR TRAINING TWEETS
        print("IN TRAIN 2")
        import os
        import sys
        if getattr(sys, 'frozen', False):
            # if you are running in a |PyInstaller| bundle
            extDataDir = sys._MEIPASS
            extDataDir = os.path.join(extDataDir, 'train.csv')
            # you should use extDataDir as the path to your file Store_Codes.csv file
        else:
            # we are running in a normal Python environment
            extDataDir = os.getcwd()
            extDataDir = os.path.join(extDataDir, 'train.csv')
            # you should use extDataDir as the path to your file Store_Codes.csv file

        df = pd.read_csv(extDataDir, encoding='utf-8')
        # print(df.head(n=5))
        print("OPENED FILE")

        Training_Tweets = df.ix[:10000]
        o = os.path.dirname(os.path.abspath(__file__)) + "\TrainingTweets_excel.csv"
        Training_Tweets.to_csv(o)

        o = os.path.dirname(os.path.abspath(__file__)) + 'AllTweets.csv'

        df.to_csv(o)

        # CREATING A TUPLE OF THE TWEET AND THE CORRESPONDING SENTIMENT
        # POSITIVE TWEETS

        pos_tweets = [(Training_Tweets.ix[row, 'tweet'], 'positive') for row in range(len(Training_Tweets)) if \
                      Training_Tweets.ix[row, 'label'] == 0]

        neg_tweets = [(Training_Tweets.ix[row, 'tweet'], 'negative') for row in range(len(Training_Tweets)) if \
                      Training_Tweets.ix[row, 'label'] == 1]

        print("WE ARE PRINTING THE NUMBER OF POSITIVE TWEETS AND NEGATIVE TWEETS\n\n")
        print(len(pos_tweets))
        print(len(neg_tweets))

        # half the negative tweets go in training
        # Downsampling the positive tweets at 1 pos:1 neg
        len_train = int(round(len(neg_tweets) / 2) * 2)
        train_tweets = neg_tweets[:int(len_train / 2)] + pos_tweets[:int(len_train / 2)]

        # half of the remaining half go in cv
        cv_negc = int((len_train / 2) + round((len(neg_tweets) - len_train / 2) / 2))
        cv_posc = int((len_train / 2) + round((len(pos_tweets) - len_train / 2) / 2))
        cv_tweets = neg_tweets[int(len_train / 2):cv_negc] + pos_tweets[int(len_train / 2):cv_posc]

        # rest go into testing
        test_tweets = neg_tweets[cv_negc:] + pos_tweets[cv_posc:]

        print("\n\n")
        print("LENGTH OF TRAIN TWEETS , CV TWEETS , TEST TWEETS")
        print(len(train_tweets))
        print(len(cv_tweets))
        print(len(test_tweets))

        exclude = set(string.punctuation)
        excluded_words = []

        # Function that provides a list of filtered unigrams and bigrams from each tweet
        def filter_tweets(tweets):
            filtered_tweets = []
            for (words, sentiment) in tweets:
                words_filtered = []
                for word in words.split():
                    word = ''.join(ch for ch in word if ch not in exclude)

                    if len(word) >= 1:
                        if word[:4] == 'http':
                            word = 'http'

                        # remove hashtags
                        if word[0] == '#':
                            word = word[1:]

                        # REMOVE ANY EXCLUDED WORDS
                        if (word.lower() not in excluded_words):
                            words_filtered.append(word.lower())

                try:
                    bigram_finder = BigramCollocationFinder.from_words(words_filtered)
                    bigrams = bigram_finder.nbest(BigramAssocMeasures.chi_sq, 200)
                    filtered_tweets.append(([ngram for ngram in itertools.chain(words_filtered, bigrams)], sentiment))
                except:
                    pass
            # Returnt he filtered list for all tweets
            return filtered_tweets

        print("TRAIN_TWEETS BEFORE FUNCTION FILTER_TWEETS")
        # print(train_tweets)
        train_tweets = filter_tweets(train_tweets)
        cv_tweets = filter_tweets(cv_tweets)
        test_tweets = filter_tweets(test_tweets)

        print("-----------------------------")

        # print(train_tweets)

        # THIS FUNCTION BUILD A LIST OF FEATURES
        def get_word_features(tweets, frequency):
            wordlist = []
            for (words, sentiment) in tweets:
                wordlist.extend(words)

            # COUNT THE FREQUENCY
            wordlist = nltk.FreqDist(wordlist)

            print("WORDLIST KEY AND VALUE PAIR")
            # for key,val in wordlist.items():
            #   print(str(key) + " : " + str(val))
            print("sorted WORDLIST")
            sorted_word_list = sorted(wordlist.items(), key=lambda x: x[1], reverse=True)
            # print(sorted_word_list)
            # USING THE VALUE OF FREQUECY PASSED
            word_features = [sorted_word_list[word][0] for word in \
                             range(len(sorted_word_list)) if sorted_word_list[word][1] >= frequency]
            print("NUMBER OF WORD FEATURES")
            # print(word_features)
            # print(len(word_features))
            return word_features

        # FUNCTION CALL TO GET THE FEATURES FROM TRAIN TWEETS
        word_features = get_word_features(train_tweets, 3)

        print("------------------------------")

        # print(train_tweets)

        # HERE WE WILL DETERMINE THE HOW MANY FEATURES IN OUR TWEET
        def extract_features(TWEETS_FILTERED):
            # LIST OF WORDS I OUR TWEET
            filtered_tweet_words = set(TWEETS_FILTERED)

            features = {}

            for word in word_features:
                features['contains(%s)' % str(word)] = (word in filtered_tweet_words)

            return features

        # Extract features from each tweets
        training_set = nltk.classify.apply_features(extract_features, train_tweets)
        cv_set = nltk.classify.apply_features(extract_features, cv_tweets)
        test_set = nltk.classify.apply_features(extract_features, test_tweets)

        print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
        tweet_number = 1
        print("THE FIRST ELEMENT OF OUR TRAINING SET AFTER APPLYING NLTK.CLASSIFY.APPLY_FEATURES FUNCTION")
        # print(training_set[tweet_number][0])
        # print(training_set[tweet_number][1])

        # TRAINING THE CLASSIFIER
        classifier = nltk.NaiveBayesClassifier.train(training_set)
        self.ccc = classifier
        print("CLASSIFIER TRAINED")

        print("+=====================================================+")

        # USING OUR CLASSIFIER ON OUR CROSS VALIDATION SET AND TEST SET
        def eval_classifier(data_set):
            cross_valid_accuracy = nltk.classify.accuracy(classifier, data_set)

            # Create two sets which we'll use to count positive and negative tweets
            ref_set = collections.defaultdict(set)
            obs_set = collections.defaultdict(set)

            # Loop over each tweet in our cross validation set
            u = 0
            for i, (feats, label) in enumerate(data_set):
                # Classify the tweet by feeding the classifier the tweet's features
                observed = classifier.classify(feats)

                # Add the current tweet to the "reference" set under the actual class
                ref_set[label].add(i)

                # Add the current tweet to the "observation" set under the predicted class
                obs_set[observed].add(i)
                # print("FOR THE FIRST 10 TWEETS WE PRINT THE ACTUAL SENTIMENT AND THE OBSERVED SENTIMENT")
                if (u < 10):
                    # FOR THE FIRST 10 TWEETS WE PRINT THE ACTUAL SENTIMENT AND THE OBSERVED SENTIMENT
                    print(label + "   " + observed)
                    u = u + 1
            print("THE ACTUAL SENTIMENTS WHICH WERE POSITIVE AND NEGATIVE")
            # print(ref_set)
            print("THE OBSERVED SENTIMENTS WHICH WERE POSITIVE AND NEGATIVE")
            # print(obs_set)
            # print("end")
            print("ACCURACY PRECISION AND RECALL OF OUR SENTIMENT ANALYSER")
            self.q = cross_valid_accuracy
            self.e = fmeas(ref_set['negative'], obs_set['negative'])
            self.r = fmeas(ref_set['positive'], obs_set['positive'])
            self.t = prec(ref_set['negative'], obs_set['negative'])
            self.y = prec(ref_set['positive'], obs_set['positive'])
            rec_neg = rec(ref_set['negative'], obs_set['negative'])
            rec_pos = rec(ref_set['positive'], obs_set['positive'])
            self.u = rec_neg
            self.v = rec_pos

        eval_classifier(cv_set)
        '''

        import pickle

        # SAVING THE CLASSIFIER
        import sys
        if getattr(sys, 'frozen', False):
            # if you are running in a |PyInstaller| bundle
            extDataDir = sys._MEIPASS
            extDataDir = os.path.join(extDataDir, 'tweet_classifier.pickle')
            # you should use extDataDir as the path to your file Store_Codes.csv file
        else:
            # we are running in a normal Python environment
            extDataDir = os.getcwd()
            extDataDir = os.path.join(extDataDir, 'tweet_classifier.pickle')
        f = open(extDataDir, 'wb')
        pickle.dump(classifier, f)
        f.close()

        # Save document_words as well
        if getattr(sys, 'frozen', False):
            # if you are running in a |PyInstaller| bundle
            extDataDir = sys._MEIPASS
            extDataDir = os.path.join(extDataDir, 'classifier_features.pickle')
            # you should use extDataDir as the path to your file Store_Codes.csv file
        else:
            # we are running in a normal Python environment
            extDataDir = os.getcwd()
            extDataDir = os.path.join(extDataDir, 'classifier_features.pickle')
        with open(extDataDir, 'wb') as f:
            pickle.dump(word_features, f)

        print("============================")
        # eval_classifier(test_set)
        '''
        self.wf = word_features
        QtWidgets.QMessageBox.warning(self, 'SUCCESS', 'CLASSIFIER TRAINED')
        print(self.q)

        self.entered = resultt.RES(self.q, self.e, self.r, self.t, self.y, self.u, self.v, self.ccc, self.wf)
        self.entered.show()
        self.close()

    def rx(self, x):
        print(self.x)
        return self.x

    def loadfile(self):
        self.x = self.textEdit.toPlainText()
        print("HERE IN LOADFILE")
        print(self.x)
        if (self.x[-4:] == ".csv"):
            import shutil
            import os
            dir_path = os.path.dirname(os.path.realpath(__file__))

            print(dir_path)
            print(self.x)
            shutil.copy2(self.x, dir_path)
            print("yessss")
            QtWidgets.QMessageBox.warning(self, 'SUCCESS', 'FILE SUCCESSFULLY LOADED')
        else:
            QtWidgets.QMessageBox.warning(self, 'FAIL', 'THIS IS NOT IN RIGHT FORMAT')


'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = analyse()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

'''