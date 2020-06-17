# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 14:08:15 2020

@author: Fitz
"""


import pandas as pd
import numpy as np
import pickle
import string
import re

### SMS Input Controller ## 

class locate_url():
    
     def __init__(self, message:str):
        self.input_msg = message
     ## Check msg for presence of URL
     
     def split_url(self): 

        ## Seperates the url from message into a new column

        input_data = [{"message":self.input_msg}]
        temp_df = pd.DataFrame(input_data)
        print(temp_df)
        seperate_url = temp_df['message'].str.split("://", expand = True) 
        
        # Rename data frame columns
        seperate_url.columns=["message", "URL"] 
        seperate_url = seperate_url.drop(["message"], axis = 1)
        print("\n URL detected: ", seperate_url)
        print("\n Passing URL to prediction model\n")
        
        text = str(seperate_url['URL'])
  
        
        return(text)
                
    
    