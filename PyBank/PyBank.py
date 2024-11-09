"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join('Starter_Code', 'PyBank', 'Resources', 'budget_data.csv')
file_to_output = os.path.join('Starter_Code', 'PyBank', 'Resources', 'analysis', 'budget_analysis.txt')  # Output file

# Define variables to track the financial data
total_months = 0
net_total = 0
changes = []
previous_profit = None
greatest_increase = ("", float('-inf'))
greatest_decrease = ("", float('inf'))

# Open and read the csv
with open(file_to_load) as csvfile:
    csvreader = csv.reader(csvfile)
    # Skip the header row
    next(csvreader)

    # Process each row of data
    for row in csvreader:
        date = row[0]
        profit = int(row[1])

        # Track the total
        total_months += 1 
        
        # Track the net total
        net_total += profit

        # Track the net change
        if previous_profit is not None:
            change = profit - previous_profit
            changes.append(change)

            # Calculate the greatest increase in profits (month and amount)
            if change > greatest_increase[1]:
                greatest_increase = (date, change)

            # Calculate the greatest decrease in losses (month and amount)
            if change < greatest_decrease[1]:
                greatest_decrease = (date, change)

        previous_profit = profit  # Update previous profit for the next iteration

# Calculate the average net change across the months
average_change = sum(changes) / len(changes) if changes else 0    

# Generate the output summary
output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
    