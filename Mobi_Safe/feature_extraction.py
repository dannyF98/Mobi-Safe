# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 17:54:17 2020

@author: Fitz
"""

import numpy as np 
import pandas as pd 
import re
# Import prediction model
import predictions

## FEATURE EXTRACTION ## 



class Feature_Extraction:
    
    def __init__(self,url:str):
        self.input_url = url
    
    ## Class of all 15 feature extraction functions ## 
    
    
    #### FEATURE 1: Long URL ####
    
    def long_url(self, l):
        l= str(l)  
        
        'This function uses URL length to differentiate between webistes' 
        
        if len(l) < 54:
            return 0
        elif len(l) >=54 and len(l) <= 75:
            return 2
        return 1
    
    
    
    #### FEATURE 2: Tiny URL ####
    
    def tiny_url(self, l):
        l= str(l)
        
        ' This function uses the shortening of URLs to differentiate'
        
        match=re.search('bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'
                        'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'
                        'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'
                        'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|'
                        'db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|'
                        'q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|'
                        'x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|tr\.im|link\.zip\.net',l)
        
        if match:
            return 1 
        else:
            return 0
        
        
        
    #### FEATURE 3: Having @ Symbol ####
         
    def having_at_symbol(self, l):
        l=str(l)
        
        'This function differentiates urls with @ symbol'
        
        if "@" in str(l):
            return 1
        return 0
    
    
    
    #### FEATURE 4: Path Redirection "//" ####
    
    def path_redirection(self, l):
        
        'If ''//'' exits within the path of URL, then identify as phihsing'  
        
        if "//" in str(l):
            return 1
        return 0
    
    
    
    #### FEATURE 5: Pref/Suff Seperation ####
        
    def prefix_suffix_seperation(self, l):
        
        'If ''-'' exits within the path of URL, then identify as phihsing' 
        
        if '-' in str(l):
            return 1
        return 0
    
    
    
    #### FEATURE 6: Presence of Sub-Domain ####
        
    def sub_domains(self, l):
        l= str(l)

        'If more than 3 Sub-Domains, then identify as phihsing' 
        
        if l.count('.') <= 3:
            return 0
        elif l.count('.') > 3:
            return 1
    
       
        
    #### FEATURE 7: Presence of special chars ####
        
    def special_chars(self, l):
        l =str(l)
        
        ' If unexpected symbols exist in URL then identify as phihsing'
        
        symbols = ['"','#','%','&','\'',':',';','<','=','>','?','@','[',']','^','`','{','|','}','~']
        numSymbols = 0
        for item in symbols:
            if str(item) in str(l):
                numSymbols+=1
        
        if numSymbols < 1:
            return 0
        elif numSymbols == 1:
            return 2
        return 1
                   
                   
    
     #### FEATURE 8: Symbol to character ratio ####
        
    def symbol_character_ratio(self, l):
        l = str(l)
        
        'If the ratio of symbols to characters, or numbers to characters..'
        ' is greater than characters to them, then classify as phishing '
        
        symbols = ['!','"','#','$','%','&','\'','(',')','*','+',',','-','.',':',';','<','=','>','?','@','[',']','^','_','`','{','|','}','~']
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
                   'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        
        num_symbols = 0
        num_numbers = 0
        num_chars = 0
                   
                 
        for char in symbols:
            if str(char) in str(l):
                num_symbols+=1
                
        for char in numbers:
            if str(char) in str(l):
                num_numbers+=1
    
        for char in letters:
            if str(char) in str(l):
                num_chars+=1
                
                
       
        # If the number of symbols is greator than a 1/3 of the number of alphanumerics then phsihing       
        if num_symbols >= (num_numbers + num_chars) / 5 or num_numbers > num_chars:
            return 1
        return 0
    
    
    
    #### FEATURE 8: HTTPS in domain ####
        
    def https_in_domain(self, l):
        l = str(l)
        
        ' If https exists in the domain then class as phishing'
        
        if 'https' in str(l):
            return 1
        return 0
    
    
    
    #### FEATURE 10: Suspicious Words #### 
    
    def suspicious_words(self, l):
        l = str(l)
    
        ' If a word from the list exists within the URL, class as phishing '
        
        match = re.search('submit|secure|suspend|confirm|webscr|account|login|'
                          'sigin|logon|cmd|wp|ebayisapi|banking|payment|paypal|'
                          'webhostapp|dropbox',l)
        
        if match:
            return 1
        else:
            return 0
        
        
        
    #### FEATURE 11: Path Length ####
    
    def path_length(self, l):
        l = str(l)
        
        ' If the path length of the URL is of a greater proportion than 1/2 of the domain..'
        ' Then classify the URL as phishing '
        
        domain = []
        path = []
        domain_length = 0
        path_length = 0
        total_length = 0
    
        split = l.split("/",1)
    
        if len(split) == 1:
            domain.append(str(split))
            
        else:
            domain.append(split[0])
            path.append(split[1])
            
            
        for item in domain:
            for elem in item:
                total_length+=1
                domain_length+=1
        
        for item in path:
            for elem in item:
                total_length+=1
                path_length+=1
                
        if path_length == 0:
            return 0
      
        elif path_length >= total_length/2:
            return 1
        elif path_length >= total_length/4:
            return 2
        else:
            return 0
        
    
    ##### FEATURE 12: last char symbol ## 
        
    
    def last_char_symbol(self, l):
        l=str(l)
        
        symbols = ['!','"','#','$','%','&','\'','(',')','*','+',',','-','.',':',';','<','=','>','?','@','[',']','^','_','`','{','|','}','~']
                   
        if len(l) == 0:
            return 0
        
        for elem in symbols:
            if elem == str(l[-1]):
                return 1
        return 0
      
                
                
    ##### FEATURE 13: Question Mark ##### 
    
    def question_mark(self, l):
        l=str(l)
        
        if '?' in str(l):
            return 1
        return 0
    
    
    
    ##### FEATURE 14: www._domain #### 
    
    def www_start_domain(self, l):
        l=str(l)
        
        match = re.search('www.',l)
        
        if match:
            return 0
        return 1
    
    
    
    #### FEATURE 15: Top_level_domain #### 
        
    def top_level_domain(self, l):
        l = str(l)
        print(l)
        match = re.search('.country|.stream|.download|.xin|.gdn|.racing|.jetzt|.win|.bid|.vip|.ren|.kim|.loan|.mom|.party|.review|.trade|.date|.wang|'
                          '.accountants|.tk|.ml|.cf|.ga|.buzz|.ryuku|.top|.live',l)
        if match:
            return 1
        return 0
    
    
    
    #################  END OF FEATURE FUNCTIONS ##########################
            
    
    # Define function to extract features from submitted prediction, 
    # and return to prediction model
            
    def extract(self):
        
        # Check format of url to see if https:// is present
        # If present, remove before continuing
        
        if re.match(r"^https?",self.input_url):
            self.input_url = self.input_url.replace("https://", '',1)
            print("https:// tag removed")
            
        if '/' not in self.input_url:
            self.input_url = self.input_url + '/'
            print("slash added\t", self.input_url)
            
        print("Input received")
        
  
        # Extract input data from app and assign to array
        input_data = [{"URL":self.input_url}]
        

        # Create tempory data frame for handling prediction
        temp_df = pd.DataFrame(input_data)
        print("data frame created")
        
            
        # Split the url into its parts, 'domain' & 'address'
    
        temp_df['URL'].str.split("/",1,expand = True)
        processed_data = temp_df['URL'].str.split("/",1, expand = True)

        processed_data.columns=["domain_name","address"]
        print("step 3 done")
        print(processed_data.head())
   
    
            
        ### Begin feature extraction of submitted URL ###
        
        
        # Apply the abpve functions to split the url into its feature parts
        
        
        ## ft 1 ##    
        processed_data['long_url'] = temp_df['URL'].apply(self.long_url)
        print("FT: 1")

        ## ft 2 ## 
        processed_data['tiny_url'] = temp_df['URL'].apply(self.tiny_url)
        print("FT: 2")
        ## ft 3 ##
        processed_data['have_@_symbol'] = temp_df['URL'].apply(self.having_at_symbol)
        print("FT: 3")
        ## ft 4 ##
        processed_data['redirect'] = processed_data['address'].apply(self.path_redirection)
        print("FT:4 ")
        ## ft 5 ##
        processed_data['prefix_suffix_seperation'] = processed_data['domain_name'].apply(self.prefix_suffix_seperation)
        print("FT:5 ")
        ## ft 6 ## 
        processed_data['sub_domains'] = processed_data['domain_name'].apply(self.sub_domains)
        print("FT: 6")
        ## ft 7 ## 
        processed_data['symbol_character_ratio'] = temp_df['URL'].apply(self.symbol_character_ratio)
        print("FT:7 ")
        ### ft 8 ##
        processed_data['https_in_domain'] = temp_df['URL'].apply(self.https_in_domain)
        print("FT: 8")
        ### ft 9 ##
        processed_data['special_characters'] = temp_df['URL'].apply(self.special_chars)
        print("FT: 9")
        ### ft 10
        processed_data['suspicious_words'] = temp_df['URL'].apply(self.suspicious_words)
        print("FT: 10")
        ### ft 11 ## 
        processed_data['path_length'] =  processed_data['address'].apply(self.path_length)
        print("FT: 11")
        ### ft 12 ## 
        processed_data['last_char_symbol'] = processed_data['address'].apply(self.last_char_symbol)
        print("FT: 12")
        ### ft 13 ## 
        processed_data['question_mark'] =temp_df['URL'].apply(self.question_mark)
        print("FT: 13")
        ### ft 14 ## 
        processed_data['www._present'] = processed_data['domain_name'].apply(self.www_start_domain)
        print("FT: 14")
        ###ft 15 ## 
        processed_data['top_level_domain'] = processed_data['domain_name'].apply(self.top_level_domain)
        print("FT: 15")
        ## All functions now applied##

        print("Feature extraction Complete\n")
        
        ## return extracted features to prediction model ## 
        
        return predictions.predictor(processed_data)
