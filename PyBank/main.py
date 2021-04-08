import os
import csv

#import
# import csv data from this path
csvpath = os.path.join("Resources", "budget_data.csv")

#open csv
with open(csvpath, 'r') as csvfile:
#read csv
    csvreader = csv.reader(csvfile, delimiter=',')
#skip header
    next(csvreader, None)
    
#define variables
    total_months = 0
    net_total = 0
    profitlosses = []
    months = []
#read through the rows
    for row in csvreader:
#Count the total number of months
        total_months += 1
        
#add up all the values in the rows
        numlist = int(row[1])
        net_total += numlist
        profitlosses.append(int(row[1]))
        months.append(str(row[0]))
        
#calculate average change
month_changes = []
for i in range(0,(len(profitlosses)-1)):
    month_changes.append(profitlosses[i+1] - profitlosses[i])

#calculate average changes
averagechange = sum(month_changes)/(total_months-1)

#calculate the highest and lowest
greatinc = max(month_changes)
monthinc = months[month_changes.index(greatinc)+1]
greatdec = min(month_changes)
monthdec = months[month_changes.index(greatdec)+1]

#print the results
print("Financial Analysis")
print("-------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${averagechange:.2f}")
print(f"Greatest Increase in Profits: {monthinc} (${greatinc})")
print(f"Greatest Decrease in Profits: {monthdec} (${greatdec})")

output_path = os.path.join("Analysis", "Analysis.txt")
   # with open(output_path, 'w', newline='') as txtfile:
        
