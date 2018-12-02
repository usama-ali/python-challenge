import os
import csv
import numpy as np

# input and ourput files
data = os.path.join(".", "budget_data.csv")
output = os.path.join(".", "budget_output.txt")

# initial values and defining variables as lists
total_months = 0
month_of_change_ls = []
change_ls = []
max_increase_ls = ["", 0]
max_decrease_ls = ["", 99999999999999]
total = 0

with open(data) as csvdata:
    csvreader = csv.reader(csvdata)
    # reading the first row (header)
    header = next(csvreader)
    # reading the second row (1st row data)
    first_row = next(csvreader)
    # update the number of total months read and current & total profit/loss net
    total_months = total_months + 1
    prev_tot = int(first_row[1])
    total = total + prev_tot

    # for loop for 2nd row of the data
    for row in csvreader:
        total_months = total_months + 1
        total = total + int(row[1])

        change = int(row[1]) - prev_tot
        prev_tot = int(row[1])

        change_ls = change_ls + [change]
        month_of_change_ls = month_of_change_ls + [row[0]]

        # get the greatest increase
        if change > max_increase_ls[1]:
            max_increase_ls[0] = row[0]
            max_increase_ls[1] = change

        # get the greatest decrease
        if change < max_decrease_ls[1]:
            max_decrease_ls[0] = row[0]
            max_decrease_ls[1] = change

# return arithmatic average of change over the whole period
mean_change = sum(change_ls)/len(change_ls)


print(f"Financial Analysis")
print(f"----------------------")
print(f"Total Months: {total_months}")
print(f"Total: {total}")
print(f"Average  Change: ${mean_change:.2f}")
print(f"Greatest Increase in Profits: {max_increase_ls[0]} ($ {max_increase_ls[1]})")
print(f"Greatest Decrease in Profits: {max_decrease_ls[0]} ($ {max_decrease_ls[1]})")


