import os 
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, newline="") as csvfile:


        csvreader = csv.reader(csvfile, delimiter =",")
        csv_header = next(csvfile)

        Months = []
        Profit_Loss = []
        Differences = []
        Increase = ""
        Decrease = ""

        for row in csvreader: 
                Months.append(row[0])
                Profit_Loss.append(int(row[1]))

print("Financial Analysis")
print("-------------------------------")
print("Total Months", len(Months))
print("Net Total: $", sum(Profit_Loss))

for i in range(1, len(Profit_Loss)):
        Differences.append(Profit_Loss[i] - Profit_Loss[i-1])
        Average_Change = sum(Differences) / len(Differences)

        Increase = max(Differences)
        Increase_Date = str(Months[Differences.index(max(Differences))])

        Decrease = min(Differences)
        Decrease_Date = str(Months[Differences.index(min(Differences))])

print("Average Change: $", round(Average_Change))
print("Greatest Increase in Profits:",Increase_Date, "($", Increase,")") 
print("Greatest Decrease in Profits:",Decrease_Date, "($", Decrease,")")             