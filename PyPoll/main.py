'''Your task is to create a Python script that analyzes the votes and calculates each of the following values:
The total number of votes cast
A complete list of candidates who received votes
The percentage of votes each candidate won
The total number of votes each candidate won
The winner of the election based on popular vote'''

# read the file
import os
import csv
csvpath = os.path.join("Resources", "election_data.csv")
# keep count of candidate votes
countdict = {}
total = 0
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    # store the header
    header = next(csvreader)
    # count all the votes, 
    #   keep count for each candidate, total count
    for row in csvreader:
        total += 1
        candidate = row[2]
        # new candidate found
        if countdict.get(candidate, 0) == 0:
           countdict[candidate] = 1
        else:
           countdict[candidate] = countdict[candidate] + 1
print(countdict)

# create result printout
output = 'Election Results\n\n'
output += '-'*30 + '\n\n'
output += f'Total Votes: {total}\n\n'
output += '-'*30 + '\n\n'
winvote = 0
winner = ''
# print out the results and find the winner
# get the winner from the dictionary
for k, v in countdict.items():
    output += f"{k}: {v/total*100:.3f}% ({v})\n\n"
    if v > winvote:
        winvote =v
        winner = k
output += '-'*30 + '\n\n'
output += 'Winner: ' + winner + '\n\n'
output += '-'*30 

# print result to screen and file
print(output)
outfile = os.path.join("analysis", "result.txt")
with open(outfile, 'w') as outfile:
    outfile.write(output)