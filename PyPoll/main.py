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

# voter id 0, county 1, candidate 2

#define variables
    total_votes = 0
    khan_total = 0
    corr_total = 0
    li_total = 0
    otoo_total = 0
    
#read through the rows
    for row in csvreader:
        total_votes += 1
   
#count votes for each candidate
        if str(row[2]) == "Khan":
            khan_total += 1
        if str(row[2]) == "Correy":
            corr_total += 1
        if str(row[2]) == "Li":
            li_total += 1
        if str(row[2]) == "O'Tooley":
            otoo_total += 1
        
#calculate percentage of votes
    khan_perc = khan_total/total_votes * 100
    correy_perc = corr_total/total_votes * 100
    li_perc = li_total/total_votes * 100
    otoo_perc = otoo_total/total_votes * 100

#calculate winner
winner = max(khan_total, corr_total, li_total, otoo_total)
if winner == khan_total:
    mostvotes = "Khan"
elif winner == corr_total:
    mostvotes = "Correy"
elif winner == li_total:
    mostvotes = "Li"
else:
    mostvotes = "O'Tooley"

#print results
print("Election Results")
print("-------------------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------------------")
print(f"Khan: {khan_perc:.3f}% ({khan_total})")
print(f"Correy: {correy_perc:.3f}% ({corr_total})")
print(f"Li: {li_perc:.3f}% ({li_total})")
print(f"O'Tooley: {otoo_perc:.3f}% ({otoo_total})")
print("-------------------------------------")
print(f"Winner: {mostvotes}")
print("-------------------------------------")

#output results to text file
output_path = os.path.join('Analysis', 'Analysis.txt')
with open(output_path, 'w') as output:
    
    csvwriter = csv.writer(output, delimiter=',')

    # Write the Analysis
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-------------------------------------"])
    csvwriter.writerow(["Total Votes: " + str(total_votes)])
    csvwriter.writerow(["-------------------------------------"])
    csvwriter.writerow(["Khan: " + str(round(khan_perc, 3)) + "% (" + str(khan_total) + ")"])
    csvwriter.writerow(["Correy: " + str(round(correy_perc, 3)) + "% (" + str(corr_total) + ")"])
    csvwriter.writerow(["Li: " + str(round(li_perc, 3)) + "% (" + str(li_total) + ")"])
    csvwriter.writerow(["O'Tooley: " + str(round(otoo_perc, 3)) + "% (" + str(otoo_total) + ")"])
    csvwriter.writerow(["-------------------------------------"])
    csvwriter.writerow(["Winner: " + str(mostvotes)])
    csvwriter.writerow(["-------------------------------------"])
