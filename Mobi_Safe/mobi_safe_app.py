# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 17:13:44 2020

@author: Fitz
"""

## MOBI-SAFE Homepage ##

# Access URL and SMS classifiers


import process_message
import sms_controller
import feature_extraction
import pandas as pd

class MobiSafe:
    
    '''Outer Class'''
    
    def __init__(self):
        self.phishing = self.Phishing_Detector()
        self.spam = self.Spam_Detector()
        
    def sms(self):
        ## Calling inner classes
        self.spam.submit_message()
       
    def url(self):
        self.phishing.submit_url()

    def text_file(self):
        self.phishing.submit_text_file()
        
        
    class Phishing_Detector:
        
        def submit_url(self):
        
           self.user_input = input("Please Type URL in standard format: ")
           text = self.user_input
           print("Input recieved.\t", text)
           obj = feature_extraction.Feature_Extraction(text)
           str1,str2 = obj.extract()
           
           result = []
           result.append("{} \n{}\n\n".format(str1,str2))
           print("Prediction Result: \n",result)

        
        def submit_text_file(self):
            self._results = []

            file_name = input("Please type your filename here with extension, please ensure file is in the same path as the program\n\n")
            try: 
                with open(file_name, "r") as file:

                    for line in file:
                        text = str(line.split())
                        print("Reading from text file.\t", text)
                        obj = feature_extraction.Feature_Extraction(text)
                        str1,str2 = obj.extract()

                        result = []
                        result.append("{} \n{}\n\n".format(str1,str2))
                        print("Prediction Result: \n",result)
                        self._results.append(text)
                        self._results.append(result)
                print("Predictions Complete")
                print(self._results)
                
            except FileNotFoundError:
                print("File not found, please try again")
                self.submit_text_file()


       
       
        
        
    class Spam_Detector:
        
  
        def submit_message(self):
        
            self.user_input = input("Please Type message in standard format: ")
            text = self.user_input
           
            # Check if there exits url within the message
            print("Input recieved.\t", text)
             
            if "https://" in self.user_input:
               
                print("\n\t Url Detection")
               
                obj2 = sms_controller.locate_url(text)
                str3= obj2.split_url()
                print(str3)
                
                ###     URL Classification      ###
               
                classify_url = feature_extraction.Feature_Extraction(str3)
                str4,str5 = classify_url.extract()
               
                result = []
                result.append("{} \n{}\n\n".format(str4,str5))
                print("\nThe system has processed the url within the message\n")
                print("Prediction Result: \n",result)
              
            
            print("Begin analysis of sms")
            ###     SMS Classification      ###
       
           
           
            obj = process_message.Classify_Message(text)
            str1,str2 = obj.process()
           
            result = []
            result.append("{} \n{}\n\n".format(str1,str2))
            print("Prediction Result: \n",result)
            


## Create instance of Mobi-Safe
            
            
mobi_safe = MobiSafe()

mobi_safe.sms()












   
        
        




            
       