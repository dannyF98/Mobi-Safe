# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 17:53:41 2020

@author: Fitz
"""

import spam_model_training
import pickle
import numpy,sklearn,pandas

## Predictions ## 

def predictor(processed_data):
    
    # Load the stored model from disk 
    filename = '15_feature_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    print("model loaded")

    
    # set feature columns of the prediction to x
    x = processed_data.columns[2:17]
    
    #Perform prediction on x with loaded model
    preds = loaded_model.predict(processed_data[x])
    print("\nprediction complete")
    print(preds)
    
    # If the prediction returns 0 then it has predicted YES to phishing
    # If the prediction returns 1 then it has predicted NO to phishing 
    
    if preds == 0:
        str1 = "Phihsed webpage: Yes"
    else: str1 = "Phished webpage: NO"
    
    # Calculate the accuraccy score of the prediction to be returned
    
    score = loaded_model.predict_proba(processed_data[x])
    str2 = "Confidence score: "+ str(score[0][1])
    
    # Return result to the user
    return str1,str2