# don't forget to do the 'before you begin section' of the challenge

# import csv module

import csv

# read the csv file

budget_data = '../Resources/budget_data.csv'
with open(budget_data, 'r') as csv_file:
    csvreader = csv.reader(csv_file)
    header = next(csvreader) # Can't forget to skip header row

# Your task is to create a Python script that analyzes the records to calculate each of the following values:

    # The total number of months included in the dataset
        # total_months

    # The net total amount of "Profit/Losses" over the entire period
        # net_pnl

    # The changes in "Profit/Losses" over the entire period, and then the average of those changes
        # month_pnl
        # total_change
        # average_change

    # The greatest increase in profits (date and amount) over the entire period
        # greatest_increase
        # greatest_increase_date

    # The greatest decrease in profits (date and amount) over the entire period
        # greatest_decrease
        # greatest_decrease_date

# Be careful with proper indentation

# initialize variables

    total_months = 0
    net_pnl = 0

    month_pnl = 0
    total_change = 0
    average_change = 0

    greatest_increase = 0
    greatest_increase_date = "" # getting the date

    greatest_decrease = 0
    greatest_decrease_date = ""

# calculating monthly change
    # month_pnl


# loop through and iterate through csv data

    for row in csvreader:
        total_months += 1
        pnl = int(row[1])
        net_pnl += pnl
        if total_months > 1:
            change = pnl - month_pnl
            total_change += change
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = row[0]
            elif change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = row[0]
        month_pnl = pnl

average_change = total_change / (total_months - 1)

# don't forget this:
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Don't forget the \ at the end of each line of a long string

pnl_results =   f"Financial Analysis\n" \
                f"----------------------------\n" \
                f"Total Months: {total_months}\n" \
                f"Total: ${net_pnl}\n" \
                f"Average Change: ${average_change:.2f}\n" \
                f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n" \
                f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n"

print(pnl_results) # Getting the results on the terminal

# exporting text file

PyBank_results = 'PyBank_results.txt' # Making variable for text file 
with open(PyBank_results, 'w') as file:
    file.write(pnl_results)

print("Results exported to", PyBank_results)