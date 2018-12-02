import os
import csv

# input and output files
data = os.path.join(".", "election_data.csv")
output = os.path.join(".", "election_output.txt")

# initial values of votes
total_votes = 0

# Defining lists, dictionaries and initial values
candidate_options_ls = []
candidate_votes_dict = {}
winning_candidate_st = ""
winning_vote = 0

with open(data) as csvdata:
    csvreader = csv.reader(csvdata)

    # reading the first row (header)
    header = next(csvreader)

    # for loop for 1st row of the data
    for row in csvreader:
        total_votes = total_votes + 1
        candidate_name = row[2]
        if candidate_name not in candidate_options_ls:
            # update the candidate list and the votes
            candidate_options_ls.append(candidate_name)
            candidate_votes_dict[candidate_name] = 0

        candidate_votes_dict[candidate_name] = candidate_votes_dict[candidate_name] + 1

print(f"Election Results")
print(f"----------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------")

for candidate in candidate_votes_dict:
    votes = candidate_votes_dict.get(candidate)
    votes_percent = float(votes) / float(total_votes)*100

    if (votes > winning_vote):
        winning_vote = votes
        winning_candidate_st = candidate

    print(f"{candidate}: {votes_percent:.2f}% ({votes})")

print(f"----------------------")
print(f" Winner: {winning_candidate_st}")
print(f"----------------------")
