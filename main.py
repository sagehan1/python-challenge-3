# -*- coding: UTF-8 -*-
# Dependencies
import csv
import os


# Files to load and output (update with correct file paths)
INPUT_PATH = os.path.join("Resources", "budget_data.csv")  # Input file path
OUTPUT_PATH = os.path.join("analysis", "budget_analysis.txt")  # Output file path


print(os.getcwd())
os.chdir(os.path.dirname(os.path.realpath(__file__)))
print(os.getcwd())

# Define variables to track the financial data
# month_of_change = []  # Store months where changes occurred
# net_change_list = []  # Store profit/loss changes between months
total_change = 0
greatest_increase = {'value': -9999999999999999999}
greatest_decrease = {'value': 9999999999999999999}

# Add more variables to track other necessary financial data

# Open and read the csv
with open(INPUT_PATH) as input_file:
    reader = csv.reader(input_file)
    header = next(reader)     # Skip the header row
    # process first row
    first_row = next(reader) 
    month_count = 1 
    total_profit = int(first_row[1])
    prev_profit = int(first_row[1])
 
    # Process each remaining row of data
    for row in reader:
        current_month = row[0]
        current_profit = int(row[1])
        #print(type(current_profit), current_profit)
        month_count += 1
        total_profit += current_profit

        # Track the net change

        current_change = current_profit - prev_profit
        total_change += current_change
        # Calculate the greatest increase in profits (month and amount)
        # if greatest_increase_value < current_change:
        if current_change > greatest_increase['value']:
            greatest_increase['value'] = current_change
            greatest_increase['month'] = current_month
        # Calculate the greatest decrease in losses (month and amount)
        if current_change < greatest_decrease['value']:
            greatest_decrease['value'] = current_change
            greatest_decrease['month'] = current_month
        # Prepare for next row
        prev_profit = current_profit

# Calculate the average net change across the months
average_change = total_change / (month_count - 1)
print(month_count, total_profit, average_change, greatest_increase)
# Generate the output summary
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)

output_text = (
    "Financial Analysis\n"
    "----------------------------\n" 
    f"Total Months: {month_count}\n"
    f"Total: ${total_change}\n"
    f"Average Change: {total_change}\n"
    f"Greatest Increase in Profits: {greatest_increase['month']} (${greatest_increase['value']}) \n"
    f"Greatest Decrease in Profits: {greatest_decrease['month']} (${greatest_decrease['value']})"
    )
# Write the results to a text file
with open(OUTPUT_PATH, "w") as output_file:
    output_file.write(output_text)
print(output_text)