import os
import csv 

csvpath = os.path.join("budget_data.csv")

total_months = 0
total = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 1000000000000]

month_of_change = []
net_change_list = []


with open(csvpath) as rawdata:
    reader = csv.reader(rawdata)
    header = next(reader)

    first_row = next(reader)
    total_months = total_months + 1
    total = total + int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:
        total_months = total_months + 1
        total = total + int(row[1])

        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]

        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

net_monthly_avg = sum(net_change_list) / len(net_change_list)

report = (
    f"Total Months: {total_months}\n"
    f"Total: ${total}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(report)