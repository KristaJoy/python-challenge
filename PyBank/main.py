import os
import csv

#import
# import csv data from this path
csvpath = os.path.join("python-challenge", "PyBank", "Resources", "budget_data.csv")

#open csv
with open(csvpath, 'r') as csvfile:
   #read csv
    csvreader = csv.reader(csvfile, delimiter=',')
    #skip header
    next(csvreader, None)
    
    #define variables
    total_months = 0
    net_total = 0
    
 #read through the rows
    for row in csvreader:
        #Count the total number of months
        total_months += 1
        
        #add up all the values in the rows
        numlist = int(row[1])
        net_total += numlist
       
        #calculate average change
        line = float(row[1])
        change = line - (line+1)
  
    averagechange = change/line * 100
        #medianlow = statistics.median_high(
        #medianhigh = statistics.median_low(
        
print("Financial Analysis")
print("-------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${averagechange}")
#print(f"Greatest Increase in Profits: max{list name}")
#print(f"Greatest Decrease in Profits: min{list name}")


# old number - new number / old number x 100 is the percentage change formula
