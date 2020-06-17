## -*- coding: utf-8 -*-
#"""
#Created on Sun Apr 19 00:58:56 2020
#
#@author: Fitz
#"""
#
### training sms classifier ## 
#
### Import natural language toolkits and data science tools
#
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from math import log, sqrt
import pandas as pd
import numpy as np
import re
import string

import pickle

## Load training data

msgs = pd.read_csv('ham_spam_data.csv',encoding = 'latin1')
msgs.head()


## Begin data processing ##

## Remove redundant columns and renanme 'label' and 'message'

msgs.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis = 1, inplace = True)
msgs.head()

msgs.rename(columns = {'v1': 'labels', 'v2': 'message'}, inplace = True)
msgs.head()
msgs['labels'].value_counts()


## Map label value of 1 & 0 to existing 'Ham'/'Spam' labels

## Ham = 0 // Spam = 1

msgs['label'] = msgs['labels'].map({'ham': 0, 'spam': 1})
msgs.head()

## Remove 'Ham/Spam labels
msgs.drop(['labels'], axis = 1, inplace = True)
msgs.head()

## ## Split train and test data at random to a ratio of 75% train 15% test
#
## totalMsgs = 4825+747
#
## train, test = list(), list()
## for i in range(msgs.shape[0]):
##     if np.random.uniform(0, 1) < 0.75:
##         train += [i]
##     else:
##         test += [i]
#        
## ## Convert train and test data to Data Frames
## trainData = msgs.loc[train]
## testData = msgs.loc[test]
#
## ## Remove existing index from test and train data sets
#
## ## Train
## trainData.reset_index(inplace = True)
## trainData.drop(['index'], axis = 1, inplace = True)
## trainData.head()
#
## ## Test
## testData.reset_index(inplace = True)
## testData.drop(['index'], axis = 1, inplace = True)
## testData.head()
#
## trainData['label'].value_counts()
## testData['label'].value_counts()
#
## ## Visualise regularly occuring spam words 
## spam_words = ' '.join(list(msgs[msgs['label'] == 1]['message']))
## spam_wc = WordCloud(width = 512,height = 512).generate(spam_words)
## plt.figure(figsize = (10, 8), facecolor = 'k')
## plt.imshow(spam_wc)
## plt.axis('off')
## plt.tight_layout(pad = 0)
## plt.show()
#
## ## Visualise ham words
## ham_words = ' '.join(list(msgs[msgs['label'] == 0]['message']))
## ham_wc = WordCloud(width = 512,height = 512).generate(ham_words)
## plt.figure(figsize = (10, 8), facecolor = 'k')
## plt.imshow(ham_wc)
## plt.axis('off')
## plt.tight_layout(pad = 0)
## plt.show()
#
#
#
#
def process_text(text):
    
    #1 Remove punctuaation
    #2 Remove stopwords
    #3 return a list of clean text words
    
    #1
    nopunc = [char for char in text if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    
    #2
    clean_words = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
    
    #3 
    return clean_words


### Tokenization of data frames (list of tokens)
#
#msgs['message'].head().apply(process_text)
#
#
## Convert text collection to a matrix of tokens (vectorization) - 
#
#msgs.to_csv('spam_data.csv')
#
c_vectorizer = CountVectorizer(analyzer=process_text)
messages_bow = c_vectorizer.fit_transform(msgs['message'])

#print(c_vectorizer)
#print(messages_bow)
#
## Analyse shape of the data
#messages_bow.shape
#
##Create and train Naive Bayes Classifier
#from sklearn.model_selection import train_test_split
#
#X_train, X_test, y_train, y_test = train_test_split(messages_bow, msgs['label'], test_size=0.20,random_state=0)
#
#
##Create and train the Naive Bayes Classifier
#
#from sklearn.naive_bayes import MultinomialNB
#
#clf = MultinomialNB().fit(X_train, y_train)
#
## Print predictions
#print(clf.predict(X_train))
#
#print(X_train)
#print(X_test)
#print(y_test)
#
#
## Evaluate Model on training data set
#from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
#train_pred = clf.predict(X_train)
#print(classification_report(y_train, train_pred))
#print()
#print('Confusion Matrix: \n', confusion_matrix(y_train,train_pred))
#print()
#print('Accuraccy: ', accuracy_score(y_train, train_pred))
#
## Evaluate model on test data set
#
## Print predictions
#print(clf.predict(X_test))
#
## Print actual values
#print(y_test.values)
#
#
#test_pred = clf.predict(X_test)
#print(classification_report(y_test, test_pred))
#print()
#print('Confusion Matrix: \n', confusion_matrix(y_test, test_pred))
#print()
#print('Accuraccy: ', accuracy_score(y_test, test_pred))
#
# Save model 
#filename = 'bow_model.sav'
#pickle.dump(clf, open(filename, 'wb'))

#Save vectorizer


pickle.dump(c_vectorizer, open("test_vector.pickle", "wb")) 
#
#
#
#
#
#
#
#
#
#
#
