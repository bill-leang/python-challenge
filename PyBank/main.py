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
total = 0
avgChg = 0
incrMonth = 0
incrProfit = 0
decrMonth = 0
decrProfit = 0

csvpath = os.path.join("Resources", "budget_data.csv")
# read the file
with open(csvpath, 'r') as file:
  csvreader = csv.reader(file)
  # discard the header
  next(csvreader)
  # read and tally the data line by line
  for row in csvreader:
    currMonth = row[0]
    currProfit = int(row[1])
    total += currProfit
    tmonth += 1
    # check if this is the first row
    if incrProfit == 0:
      incrProfit = currProfit
      decrProfit = currProfit
      incrMonth = currMonth
      decrMonth = currMonth
    # check if the current month profit is more than greatest incr Profit so far
    elif currProfit > incrProfit:
      incrProfit = currProfit
      incrMonth = currMonth
    # check if the current month profit is less than greatest decr Profit so far
    elif currProfit < decrProfit:
      decrProfit = currProfit
      decrMonth = currMonth

avgChg = round(total /tmonth,2)


output = 'Financial Analysis\n\n'
output += '-'*30 + '\n\n'
output += f"Total Months: {tmonth}\n\n"
output += f"Total: ${total}\n\n"
output += f"Average Change: ${avgChg:.2f}\n\n"
output += f"Greatest Increase in Profits: {incrMonth} (${incrProfit})\n\n"
output += f"Greatest Dncrease in Profits: {decrMonth} (${decrProfit})\n\n"
print(output)

# write result to file
resultfile = os.path.join("analysis", "result.txt")
with open(resultfile, 'w') as outfile:
  outfile.write(output)