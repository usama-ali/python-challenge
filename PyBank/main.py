import os
import csv
import numpy as np

file = open("budget_data.csv", "r")
data = {}
sum = 0
for line in file:
    x = line.split(",")
    a = x[0]
    b = x[1]
    data[a]= b
    sum += data[a]

#print(f' {data[1]}')


def average(numbers):
    length= len(numbers)
    total = 0.0

    for number in numbers:
        total = total + number # total += number
        arithmatic_average = total/length
    return arithmatic_average


print(f"Financial Analysis")
print(f"----------------------")
print(f"Total Months: len(data)-1")
print(f"Total: sum")
print(f"Average  Change: sum(data[1])/len(data[1])")
#print(f"Greatest Increase in Profits: {max_increase_date} ($ {max_increase_value})")
#print(f"Greatest Increase in Profits: {max_decrease_date} ($ {max_decrease_value})")
