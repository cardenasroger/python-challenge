# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import os
import pandas as pd

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("C:\\Users\\carde\\Documents\\School\\Starter_Code\\PyPoll", "Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("C:\\Users\\carde\\Documents\\School\\Starter_Code\\PyPoll", "analysis", "election_analysis.txt")  # Output file path

# Load the data
try:
    data = pd.read_csv(file_to_load)
except FileNotFoundError:
    print(f"Error: The file at {file_to_load} was not found.")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

# Calculate total votes
total_votes = len(data)

# List of candidates
candidates = data['Candidate'].unique()

# Count votes for each candidate
vote_counts = data['Candidate'].value_counts()

# Calculate percentages and prepare results
results = {}
for candidate, votes in vote_counts.items():
    percentage = (votes / total_votes) * 100
    results[candidate] = {'votes': votes, 'percentage': percentage}

# Determine the winner
winner = vote_counts.idxmax()

# Print results
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