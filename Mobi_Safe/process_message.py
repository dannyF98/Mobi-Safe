# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 03:31:49 2020

@author: Fitz
"""

from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import pandas as pd
import numpy as np
import string
import re

import sms_predictions
## Process submitted message 

class Classify_Message:
    
    def __init__(self, msg:str):
        self.input_msg = msg
        
    def process_text(self, text):

        #1 Remove punctuaation
        #2 Remove stopwords
        #3 return a list of clean text words
        
        #1
        nopunc = [char for char in text if char not in string.punctuation]
        nopunc = ''.join(nopunc)
        print("punctuation removed")
        
        #2
        clean_words = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
        print("stop_words removed")
        #3 
        return clean_words
    
    def process(self):
        
        # Load submitted data and process for classification
        
        input_data = [{"message":self.input_msg}]
        temp_df = pd.DataFrame(input_data)
        print(temp_df)
      
       
        temp_df['message'].apply(self.process_text)
        
        print("Input vectorized\n Submitting to prediction model")
     
        return sms_predictions.prediction(temp_df)
    
    
    


        
        