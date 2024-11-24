# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("analysis", "election_analysis.txt")

# Ensure the output directory exists
if not os.path.exists('analysis'):
    os.makedirs('analysis')

# Initialize variables
total_votes = 0
vote_counts = {}

# Load the data
try:
    with open(file_to_load) as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)  # Skip the header row
        
        # Read each row in the CSV
        for row in csvreader:
            total_votes += 1  # Count total votes
            candidate = row[2]  # Assuming the candidate's name is in the third column
            
            # Count votes for each candidate
            if candidate in vote_counts:
                vote_counts[candidate] += 1
            else:
                vote_counts[candidate] = 1

except FileNotFoundError:
    print(f"Error: The file at {file_to_load} was not found.")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

# Calculate percentages and prepare results
results = {}
for candidate, votes in vote_counts.items():
    percentage = (votes / total_votes) * 100
    results[candidate] = {'votes': votes, 'percentage': percentage}

# Determine the winner
winner = max(vote_counts, key=vote_counts.get)

# Print results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, result in results.items():
    print(f"{candidate}: {result['percentage']:.3f}% ({result['votes']})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export results to a text file
with open(file_to_output, 'w') as f:
    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write("-------------------------\n")
    for candidate, result in results.items():
        f.write(f"{candidate}: {result['percentage']:.3f}% ({result['votes']})\n")
    f.write("-------------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write("-------------------------\n")