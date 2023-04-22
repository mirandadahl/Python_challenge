import os

import csv 

input_file = os.path.join("Resource", "budget_data.csv")
output_file = os.path.join("analysis", "budget_results.txt")


print('Financial Analysis')
print('--------------------------')
# The total number of months included in the dataset

with open(input_file) as infile:

    csv_reader = csv.reader(infile)
    months = len(list(csv_reader)) -1

print(f"Total Months: {months}")

# The net total amouth of "Profit/Losses" over the entire period


file = open("/Users/mirandadahl/Desktop/Python_challenge/Resource/budget_data.csv", "r")
lines = file.readlines()
budget_col = [line.split(',')[1] for line in lines]
','.join(budget_col)
budget_col.pop(0)

budget = []

for value in budget_col:
    budget.append(value.replace("\n", ""))

budget_list = [int(num) for num in budget]

total = sum(budget_list)

print(f"Total: ${total}")

# The average changes in "Profit/Losses"

change = [budget_list[i+1] - budget_list[i] for i in range(len(budget_list)-1)]

budget_average = sum(change) / len(change)

print(f"Average Change: ${budget_average}")

# The greatest increase in profits (date and amount) over the entire period

Greatest = max(change)

print(f"Greatest Increase in Profits: (${Greatest})")

# The greatest decrease in profits (date and amoutn) over the entire period

lowest = min(change)

print(f"Greatest Decrease in Profits: (${lowest})")
# Result:
# Financial Analysis
# --------------------------
# Total months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)


#how to insert the date associated
