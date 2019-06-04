import os
import csv

# Path to collect data from the given folder/file
bd_csv = os.path.join("budget_data.csv")

# Define the function and have it accept 'budgetData' as its sole parameter
# def financial_analysis(budget_data):

# open csv file:
with open(bd_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)
    total_revenue = 0
    for row in csvreader:

        total_months = csvreader.line_num-1
        total_revenue += int(row[1])
        # average_change = mean(int(row[1]))
        max_profit = max(row[1])
        max_loss = min(row[1])
        date = row[0]

print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_revenue}")
# print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profits: {date} (${max_profit})")
print(f"Greatest Decrease in Profits: {date} (${max_loss})")


# #Lists to store data
# total_months = 0
# total = []
# average_change = []
# greatest_profit_increase = []
# greatest_profit_decrease = []

# # open csv file:
# with open(bd_csv, newline="") as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=",")
    
#     csv_header = next(csvreader)
#     for row in csvreader:
#         # count total months
#        total_months += 1
#     print(total_months)

#         # Add price
#         price.append(row[4])

#         # Add number of subscribers
#         subscribers.append(row[5])

#         # Add amount of reviews
#         reviews.append(row[6])

#         # Determine percent of review left to 2 decimal places
#         percent = round(int(row[6]) / int(row[5]), 2)
#         review_percent.append(percent)

#         # Get length of the course to just a number
#         new_length = row[9].split(" ")
#         length.append(float(new_length[0]))

# # Zip lists together
# cleaned_csv = zip(title, price, subscribers, reviews, review_percent, length)

# # Set variable for output file
# output_file = os.path.join("web_final.csv")

# #  Open the output file
# with open(output_file, "w", newline="") as datafile:
#     writer = csv.writer(datafile)

#     # Write the header row
#     writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
#                      "Percent of Reviews", "Length of Course"])

#     # Write in zipped rows
#     writer.writerows(cleaned_csv)