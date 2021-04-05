import os
import csv

# import csv data from this path
csvpath = os.path.join("Resources", "budget_data.csv")

#open csv
with open(csvpath) as csvfile:
   #read csv
    csvreader = csv.reader(csvfile, delimiter=',')
    #skip header
    next(csvreader, None)
    
    total_months = 0
 #read through the rows
    for row in csvreader:
    #The total number of months included in the dataset
    #count the rows
        total_months += 1

#for rows in csvreader:
   # r = len(rows)
   # total = 0
   # for row in rows:
       # total += row # this euqals total = total + row

#The net total amount of "Profit/Losses" over the entire period
#add up the column

#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# VVV the easiest way to solve average is this:

#import statistics
#def mean(numlist):
    #print(statistics.mean(numlist))

#The greatest increase in profits (date and amount) over the entire period
# x = max(rows?)

#The greatest decrease in losses (date and amount) over the entire period
# y = min(rows?)

