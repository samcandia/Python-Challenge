import csv
import os

#creating empty lists
totalmonths = 0
netprofit = 0
netchanges = [] #will be the list of changes that we take average of 
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999]


path = os.path.join("Resources", "budget_data.csv")
with open(path) as file:
    csvreader = csv.reader(file, delimiter=",")
    skipheader = next(csvreader)
    firstrow = next(csvreader) 
    totalmonths = totalmonths + 1
    netprofit = netprofit + int(firstrow[1])

#calculate total months and total profits   
    month1 = int(firstrow[1])
    for row in csvreader:
        totalmonths = totalmonths + 1
        netprofit = netprofit + int(row[1])

#calculate the profit changes then store them in 'netchanges'
        profitchanges =  int(row[1]) - month1
        netchanges += [profitchanges]
        month1 = int(row[1])

#calculate greatest increase and decrease in profits with the date
        if profitchanges > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = profitchanges
        if profitchanges < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = profitchanges





    financial_summary = (f"Financial Analysis\n" f"----------------\n" f"Total Months:{totalmonths}\n" f"Total: ${netprofit}\n"f"Average Change: ${round(sum(netchanges)/(len(netchanges)),2)}\n" f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n" f"Greatest Decrease in Profits {greatest_decrease[0]} (${greatest_decrease[1]})")
    
    print(financial_summary)

with open("analysis.txt", 'w') as analysis:
    analysis.write(financial_summary)





