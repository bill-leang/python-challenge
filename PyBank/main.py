'''Your task is to create a Python script that analyses the records to calculate each of the following values:
The total number of months included in the dataset
The net total amount of "Profit/Losses" over the entire period
The changes in "Profit/Losses" over the entire period, and then the average of those changes
The greatest increase in profits (date and amount) over the entire period
The greatest decrease in profits (date and amount) over the entire period
print result to screen and export to textfile'''
# open the file
import os
import csv

tmonth= 0
# for tracking total profit
total = 0
# for tracking total change in profit
totalChg = 0
avgChg = 0
# record biggest increase in profit and its month
incrMonth = 0
incrProfit = 0
# records biggest decrease in profit and its month
decrMonth = 0
decrProfit = 0
# change in profit
chgProfit =0
prevProfit = 0
firstRow = True
csvpath = os.path.join("Resources", "budget_data.csv")
# read the file
with open(csvpath, 'r') as file:
  csvreader = csv.reader(file)
  # store the header
  header = next(csvreader)
  # read and tally the data line by line
  for row in csvreader:
    # current month and profit
    currMonth = row[0]
    currProfit = int(row[1])
    tmonth +=1
    total += currProfit
    # for first row, no change is recorded, not count the month
    if firstRow:
      prevProfit = currProfit
      firstRow = False
      
      # skip to next row
      continue
    # for 2nd row on, calc change, record number of month
    else: 
    # calc the change in profit
      chgProfit = currProfit - prevProfit
      prevProfit = currProfit
      totalChg += chgProfit
      
    # check if the current month profit is more than greatest incr Profit so far
    if chgProfit > incrProfit:
      incrProfit = chgProfit
      incrMonth = currMonth
    # check if the current month profit is less than greatest decr Profit so far
    elif chgProfit < decrProfit:
      decrProfit = chgProfit
      decrMonth = currMonth

# note the average change is divided by 85 months as the first month is not considered
avgChg = totalChg /(tmonth -1)

# create the result, format as currency
output = 'Financial Analysis\n\n'
output += '-'*30 + '\n\n'
output += f"Total Months: {tmonth}\n\n"
output += f"Total: ${total:,}\n\n"
# format as currency to 2 decimal places
output += f"Average Change: ${avgChg:,.2f}\n\n"
output += f"Greatest Increase in Profits: {incrMonth} (${incrProfit:,})\n\n"
output += f"Greatest Dncrease in Profits: {decrMonth} (${decrProfit:,})\n"
print(output)

# write result to file
resultfile = os.path.join("analysis", "result.txt")
with open(resultfile, 'w') as outfile:
  outfile.write(output)