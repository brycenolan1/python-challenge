#import csv
import os
import csv

#path to collect data from the given folder/file
budget_csv = os.path.join("budget_data.csv")

#storing date and revenue in a list
date = []
revenue = []

#open csv file
with open(budget_csv,encoding="utf8") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")

#append csvreader to date and revenue lists while skipping header
    header = next(csvreader) 
    for row in csvreader:
        date.append(row[0])
        revenue.append(row[1])

    #length of date list to get total number of months
    nummonths = len(date)

    #sum revenue
    revsum = int()

    #iterate to turn revenue into integer and add to sum
    for i in range(0,len(revenue)):
        revenue[i] = int(revenue[i])
        revsum += revenue[i]
    
    
    #average change in "Profit/Losses" between months over the entire period
    #create new integer to store total monthly changes,  divide by nummonths - 1
    #create new list to store monthly changes

    totalchange = int()
    monthchange = []
    for i in range(len(revenue)-1):
        totalchange += (revenue[i+1] - revenue[i])
        monthchange.append((revenue[i+1] - revenue[i]))

    avgchange = totalchange / (nummonths - 1)

    #print analysis
    print("Financial Analysis")
    print("-----------------------------")
    print(f"Total Months: {nummonths}")
    print(f"Total: ${revsum}")
    print(f"Average Change: ${avgchange}")
    print(f"Greatest Increase in Profits: {date[monthchange.index(max(monthchange))]} (${max(monthchange)})")
    print(f"Greatest Decrease in Profits: {date[monthchange.index(min(monthchange))]} (${min(monthchange)})")


#write analysis to csv
with open("pybankmain_solved.csv", "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Financial Analysis"])
    writer.writerow(["-----------------------------"])
    writer.writerow([f"Total Months: {nummonths}"])
    writer.writerow([f"Total: ${revsum}"])
    writer.writerow([f"Average Change: ${avgchange}"])
    writer.writerow([f"Greatest Increase in Profits: {date[monthchange.index(max(monthchange))]} (${max(monthchange)})"])
    writer.writerow([f"Greatest Decrease in Profits: {date[monthchange.index(min(monthchange))]} (${min(monthchange)})"])