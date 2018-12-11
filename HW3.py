import csv
file_name = "03-Python_Homework_PyBank_Resources_budget_data.csv"
with open(file_name) as myfile:
    csvreader = csv.reader(myfile)

    for row in csvreader: 
        print(row)

