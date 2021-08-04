# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 20:33:46 2021

@author: Daniel Challenger
"""

# import pandas as pd
import numpy as np

def intrinsic_value(df0, StockPrice, StrikePrice, OptionType):
    
    row_labels = np.array(df0.index) # index values for Pandas dataframe
    
    ## Calculating instrinsic value for call options
    if OptionType=='call' or OptionType=='Call':
        # print('This is a call option') # Used for testing and debugging
    
        for i in range(0, len(row_labels)): # Loops == number of rows
            for j in range(0, len(df0.columns)): # Loops == number of columns
             
                # Applying formula "Strike Price - Future Stock Price"
                df0.iloc[i][j] = max(0, StrikePrice - row_labels[i])
    
    ## Calculating instrinsic value for put options
    elif OptionType=='put' or OptionType=='Put':
        # print('This is a put option') # Used for testing and debugging
        
        for i in range(0, len(row_labels)): # Loops == number of rows
            for j in range(0, len(df0.columns)): # Loops == number of columns
             
                # Applying formula "Future Stock Price - StrikePrice"
                df0.iloc[i][j] = max(0, row_labels[i] - StrikePrice)
                
    else:
        print('Enter "call" or "put" for OptionType')
    # print('It is working') # Used for tesing
    
    
    #--------------------TESTING AND DEBUGGING CODE--------------------------#
    
    # print("row_labels =", row_labels)
    # print(df0)
    
    #----------------END OF TESTING AND DEBUGGING CODE-----------------------#
    
    return(df0)