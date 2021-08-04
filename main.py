# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 01:38:11 2021

@author: Daniel Challenger
"""

# Importing modules

import datetime as dt
import numpy as np
import pandas as pd

# The following fuctions are custom created for this script

from create_df import blankdf # Creates blank data frame
from intrinsic import intrinsic_value # Calculates intrinsic value
from implied import implied_volatility # Calculated implied volatility

# What information do I need?
#
# Stock Price
# Strike Price
# Implied Volatility
# Intrinsic Value
# Time Value 
# Option Premium


##############################################################################

# This section only focuses on declaring variables used in script.

#----------------------------------------------------------------------------#

# All of the variables being declared in this area are values which need to
# inputted with data that is not initially calculated.

StockPrice = 440.0
StrikePrice = 435.0
OptionPremium = 2.31
OptionType = 'put' # Enter 'call' or 'put
ExpirationDate = dt.date(2021, 8, 13) # Date in format (yyyy, mm, dd)

# The following will help label the rows inthe final output

MaxStockPrice = 450.0 # Maximum stock price for range os prices
MinStockPrice = 430.0 # Minumum stock prices for range of prices
PriceIncrement = 0.05 # Increment of all prices being displayed

#----------------------------------------------------------------------------#

# All of these varibles do not require initial input before running script. 
# All values entered are default values.

df0 = 0 # Blank dataframe with columns and rows labeled
df_IntrinsicValue = 0.0 # Dataframe containing intrinsic values
df_ImpliedVolatility = 0.0 # Dataframe containing implied volatility
TimeDecay = 0.0
CurrentDate = dt.date.today()

#----------------------DEBUGGING AND TESTING CODE----------------------------#

# print(StockPrice)
# print(dt.date.today())
# print(CurrentDate)
# print(dt.date(2021, 8, 25))
# print(ExpirationDate)
# print(ExpirationDate - CurrentDate)
# print(blankdf(2,3))
# print(ExpirationDate.weekday())

#------------------END OF DEBUGGING AND TESTING CODE-------------------------#
##############################################################################

###########################################################################3##

# Main components of code

#----------------------------------------------------------------------------#

# Create blank dataframe which will be filled with calculated values 
df0 = blankdf(CurrentDate, ExpirationDate, MaxStockPrice, MinStockPrice, \
              PriceIncrement)
    
# Calculate the intrinsic value
df_IntrinsicValue = intrinsic_value(df0, StockPrice, StrikePrice, OptionType)

# Calculate implied volatility
df_ImpliedVolatility = implied_volatility(StockPrice, StrikePrice, \
                                          OptionPremium, OptionType, \
                                          ExpirationDate)

# print(df0.index)
# strikes =  np.array(df0.index)
# print(strikes)
# rows = df0.head()
# for row in rows.index:
#     print(row, ' ')

# numnum=123.456789
# print("Two numnum decibals = %.2f" % numnum)
# decitest=("%.2f"%numnum)
