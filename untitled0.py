# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UJs1KVLhWEUZfvuIMqz8BS4U_xIt6Ftb
"""

#Description: Tracking the cost of material

#Import the libraries 
import numpy as np 
import pandas as pd
from datetime import date

def prepend_file(sum):
  filename = 'expenses.csv'
  with open(filename, 'r') as original: data = original.read()
  with open(filename, 'w') as modified: modified.write("Total Sum,"+str(sum)+"\n" + data)


#Create Empty Lists
GOODS_OR_SERVICES = []
PRICES = []
DATES = []
EXPENSE_TYPES = []

#Create a function to add the expenses to the lists and organize the data
def add_expense(good_or_service, price, date, expense_type):
  
  GOODS_OR_SERVICES.append(good_or_service)
  PRICES.append(price)
  DATES.append(date)
  EXPENSE_TYPES.append(expense_type)

from sys import breakpointhook
#Main program 
option = -1 #The users option for choice or input
while(option != 0):
  #Creating the option menu

  print('The best tracker:')
  print('1. Add expense.')
  print('2. Production hours?')
  print('3. Show and save the Expense report.')
  print('0.  Exit')
  option = int(input('Choose an option:\n'))

#Print a new line
  print()
#Check for the users choice or option of input
  if option == 0:
    print('Exiting the program')
    break
  elif option == 1: 
    print('Adding Material')
    expense_type = 'Material'
  elif option == 2:
    print('Production hours')
    expense_type = 'Production time'
  elif option == 3:
    #Create a data frame and add the expenses
    expense_report = pd.DataFrame()
    expense_report['GOODS_OR_SERVICES'] = GOODS_OR_SERVICES
    expense_report['PRICES'] = PRICES
    expense_report['DATES'] = DATES
    expense_report['EXPENSE_TYPES'] = EXPENSE_TYPES
    expense_report['sum(PRICES)'] = sum(PRICES)
    print("Sum of elements in given list is :", sum(PRICES))
    #Save the expense report
    expense_report.to_csv('expenses.csv')
    prepend_file(sum(PRICES))
    #Show the expense report
    print(expense_report)
  else:
    print('You chose an incorrect option. Please choose 0, 1, 2, or 3.')

  #Allows the user to enter the good or service and the price.
  if option == 1 or option == 2:
    good_or_service = input('Enter the good or service for the expense type '+expense_type+':\n')
    price = float(input('Enter the price of the good or service:\n'))
    today = date.today()
    add_expense(good_or_service, price, today, expense_type)
  #Print a new line
  print()