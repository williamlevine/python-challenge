# Import modules
import os
import csv

# Set up the csv path to find the election_data.csv file in the Resources folder
csvpath = os.path.join("Resources", "election_data.csv")

# Set up empty lists
totalVotes = []
candidates = []

# Set up dictionary to hold candidate and their respective amount of votes
candidateVotes = {}

# Open the csv file and set up the csv reader
# Use UTF-8 encoding in case there are any ususual characters in the names of a candidate or elsewhere
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

# For each row in the csv file, add each Ballot ID to the totalVotes list
# Set a variable to hold the name of the candidate 
    for row in csvreader:
        totalVotes.append(row[0])
        candidate = row[2]

# See if the current candidate name is already in the candidateVotes dictionary
# If they are, add one vote to their vote count
# If the candidate is not already in the dictionary, add them to it, and count this row as their first vote         
        if candidate in candidateVotes:
            candidateVotes[candidate] += 1
        else:
            candidateVotes[candidate] = 1

# Determine the winner based on who has the highest value in the dictionary
winner = max(candidateVotes, key=candidateVotes.get)

# Print the results, including total vote count, which is determined by the length of the totalVotes list
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(len(totalVotes)))
print("-------------------------")

# Loop through the dictionary, calculating the percentage of votes for each candidate
# Print the name of the candidate, their percent of the votes, and the vote count
# Print the winner
for candidate, votes in candidateVotes.items():
    votePercent = (votes / int(len(totalVotes))) * 100
    print(f"{candidate}: {round(votePercent, 3)}% ({votes})")
print("-------------------------")
print("Winner: " + winner)

# Set up the output file as a .txt in the Analysis folder called Election_Results.txt
output_file = os.path.join("Analysis", "Election_Results.txt")

# Open the output file in write mode
# Print each line as above but with the \n command at the end of each line to ensure proper new line creation
with open(output_file, "w") as textfile:
    textfile.write("Election Results\n")
    textfile.write("-------------------------\n")
    textfile.write("Total Votes: " + str(len(totalVotes)) + "\n")
    textfile.write("-------------------------\n")
    for candidate, votes in candidateVotes.items():
        votePercent = (votes / int(len(totalVotes))) * 100
        textfile.write(f"{candidate}: {round(votePercent, 3)}% ({votes})\n")
    textfile.write("-------------------------\n")
    textfile.write("Winner: " + winner + "\n")

