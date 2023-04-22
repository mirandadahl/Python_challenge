# start output at the beginging the end output to turn into a text file (look up)
import os

import csv

input_file = os.path.join("Resource", "election_data.csv")
output_file = os.path.join("analysis", "election_results.txt")

votes = 0
l_candidates = []
d_candidates = {}
winner = ""
winner_votes = 0

# The total number of votes cast

with open(input_file) as infile:

    csv_reader = csv.reader(infile)
    # votes = len(list(csv_reader)) -1
    next(csv_reader)

    for row in csv_reader:
        votes += 1     
        candidate_name = row[2]

        if candidate_name not in l_candidates:
            l_candidates.append(candidate_name)
            d_candidates[candidate_name] = 0
        d_candidates[candidate_name] += 1
    


output = (
    f"Election Analysis\n"
    f"-------------------\n"
    f"Total Votes: {votes}\n"
    f"-------------------\n"
)

print(output)
with open(output_file, "w") as outfile:
    outfile.write(output)
    for candidate in l_candidates:
        c_vote = d_candidates[candidate]
        percentage = float(c_vote) / float(votes) *100
        print(f"{candidate}: {percentage:.3f}% ({c_vote})")
        outfile.write(f"{candidate} {percentage:.3f}% {c_vote}\n")
        if c_vote > winner_votes:
            winner_votes = c_vote
            winner = candidate

    
    print(f"--------------------------\nWinner: {winner}\n--------------------------")
    outfile.write(f"--------------------------\nWinner: {winner}\n--------------------------")
