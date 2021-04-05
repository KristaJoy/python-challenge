import os
import csv

#import
# import csv data from this path
csvpath = os.path.join("Resources", "election_data.csv")

#open csv
with open(csvpath, 'r') as csvfile:
   #read csv
    csvreader = csv.reader(csvfile, delimiter=',')
    #skip header
    next(csvreader, None)










print("Election Results")
print("-------------------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------------------")
print(f"Khan: {khan_perc} ({khan_total})")
print(f"Correy: {corr_perc} ({corr_total})")
print(f"Li: {li_perc} ({li_total})")
print(f"O'Tooley: {otoo_perc} ({otoo_total})")
print("-------------------------------------")
print("Winner: {mostvotes}")
print("-------------------------------------")

