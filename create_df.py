# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 11:21:30 2021

@author: Daniel Challenger

This function creates and empty dataframe for a stock options calculator. 
"CurrentDate" being sent from the main function gets converted to StartDate. 
StartDate is the first date to be used as a column header.

"""

import pandas as pd
import datetime as dt
import numpy as np

## VARIABLES BEING USED IN THIS FUNCTION

def blankdf(StartDate, ExpirationDate, MaxStockPrice, MinStockPrice, \
            PriceIncrement):
    
    ## Initialize additional variables
    OneDay = dt.timedelta(days = 1) # Defining day increment for columns
    columns = 0 # Column labels for dataframe    
    rows = 0 # Index labels for dataframe
    df0 = 0 # Final dataframe to be exported to main script                            
    
    ##########################################################################
    
    ## Setting the beginning date which is represented as "StartDate".
    ## The beginning date will not be current day or a weekend.
    ## If current day is Friday or a weekend, then the start day will be
    ## the following Monday. If current day falls from Monday through
    ## Thursday, then the start day will be the next day.
    if StartDate.isoweekday() >= 5: # If current day of Friday, SAturdy,
                                    # or Sunday.
        # Use function "y = -x + 8" to adjust StartDate 
            # x = current date
            # y = adjusted start date
        StartDate = StartDate + (-StartDate.isoweekday() + 8) * OneDay
            # Start date will be following Monday
    else: # If current day is Monday, Tuesday, Wednesday, or Thursday
        StartDate = StartDate + OneDay # Start date will be tomorrow
        
    
    ## Creating labels for columns
    
    columns = pd.bdate_range(start=StartDate, end=ExpirationDate)
    
    ##########################################################################
    
    ## Creating labels for rows
    
    rows = np.arange(MaxStockPrice, MinStockPrice, -PriceIncrement)
    
    ##########################################################################
    
    ## Creating empty dataframe
    
    df0 = pd.DataFrame(index=rows, columns=columns)
    
    #----------------------DEBUGGING AND TESTING CODE------------------------#

    # df = 'testing this out again'
    # print(OneDay)
    # print(OneDay + StartDate)
    # print('Column Headers =', ColHeaders)
    # print('StartDate =', StartDate.isoweekday())
    # StartDate = StartDate - OneDay
    # print(StartDate - OneDay)
    # print(StartDate)
    # print(MaxStockPrice, MinStockPrice, PriceIncrement)
    # print(rows)
    
    #------------------END OF DEBUGGING AND TESTING CODE---------------------#
    
    return(df0)