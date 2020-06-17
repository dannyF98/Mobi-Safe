# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 03:50:05 2020

@author: Fitz
"""


import spam_model_training
import pickle
import numpy,sklearn,pandas
from sklearn.feature_extraction.text import CountVectorizer

# SMS_Predictions

def prediction(processed_message):
    
    # Make prediction on processed data with saved model 
    
    #1. Load Naive Bayes Model and vectoriser
    #2. Perform prediction on input data
    #3. Return result and confidence score to the user
    
    #1 
    #Load vectoriser
    
    loaded_vectorizer = pickle.load(open('test_vector.pickle', 'rb'))

    
    x = processed_message['message']
    print(x)
    
    # Load the stored model from disk 
    filename = 'bow_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    print("model loaded")
    
    msg_bow = loaded_vectorizer.transform(x)
    preds = loaded_model.predict(msg_bow)
    print("prediction complete")
    print(preds)
    
    
    # If the prediction returns 0 then it has predicted YES to phishing
    # If the prediction returns 1 then it has predicted NO to phishing 
    
    if preds == 0:
        str1 = "Ham"
    else: str1 = "Spam"
    
    # Calculate the accuraccy score of the prediction to be returned
    
    score = loaded_model.predict_proba(msg_bow)
    str2 = "Confidence score: "+ str(score[0][1])
    
    # Return result to the user
    return str1,str2
    
    
    
    
    
    


    
    
    