#PyPoll

import os
import csv

total_votes = 0
c_votes = 0
d_votes = 0
r_votes = 0


# Path
csvpath = os.path.join('.', 'Resources', 'election_data.csv')

# Open and Read Path
with open(csvpath) as csvfile:

    
    reader = csv.reader(csvfile)
    
    # Read the header
    header = next(csvfile)

    # Read rows
    for row in reader:
        
        # Calculate total votes
        total_votes += 1
        
        # calculate votes for each candidate
        if (row[2] == "Charles Casper Stockham"):
            c_votes += 1
        elif (row[2] == "Diana DeGette"):
            d_votes += 1
        else: 
            r_votes += 1
        
            
    # calculate percentages
    c_percent = c_votes / total_votes
    d_percent = d_votes / total_votes
    r_percent = r_votes / total_votes
    
    # winner of election
    winner = max(c_votes, d_votes, r_votes)

    if winner == c_votes:
        winner_name = "Charles Casper Stockham"
    elif winner == d_votes:
        winner_name = "Diana DeGette"
    else:
        winner_name = "Raymon Anthony Doanne"
   

# print results
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------------")
print(f"Charles Casper Stockham: {c_percent:.3%}({c_votes})")
print(f"Correy: {d_percent:.3%}({d_votes})")
print(f"Raymon Anthony Doanne: {r_percent:.3%}({r_votes})")
print(f"---------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------")

# write file to
output_file = os.path.join('.', 'analysis', 'election_results.txt')


with open(output_file, 'w',) as txtfile:

# write data in analysis file
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Charles Casper Stockham: {c_percent:.3%}({c_votes})\n")
    txtfile.write(f"Diana DeGette {d_percent:.3%}({d_votes})\n")
    txtfile.write(f"Raymon Anthony Doanne: {r_percent:.3%}({r_votes})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {winner_name}\n")
    txtfile.write(f"---------------------------\n")

