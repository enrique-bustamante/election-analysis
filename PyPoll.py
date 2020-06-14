# the data we need to retrieve
import os
import csv
# assign variables for the file to load and the path as well as to save
file_to_load = os.path.join('Resources','election_results.csv')
file_to_save = os.path.join('Analysis', 'election_results.txt')

# initialize vote counter
total_votes = 0
# initialize list of candidate names
candidate_options = []
#initialize dictionary to store candidate votes
candidate_votes = {}

#initialize arrays for winning candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# open the election results and read the file
with open(file_to_load) as election_data:
  #To-do: read and analyze data here
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
  
    for row in file_reader:

      #t his adds up all of the votes
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:

          #this adds a candidate's name to the list
          candidate_options.append(candidate_name)

          #this sets up arrays for each candidate and sets them to zero
          candidate_votes[candidate_name] = 0

          # this tallies votes for each candidate
        candidate_votes[candidate_name] += 1

# the total number of votes cast
print(total_votes)

# A complete list of candidates who received votes
print(candidate_options)
print(candidate_votes)

# The percentage of votes each candidate won
# iterate through candidate list
for candidate in candidate_votes:
    # retrieve number of votes for each candidate
    votes = candidate_votes[candidate]

    # calculate the percentage of vote
    vote_percentage = int(votes)/int(total_votes) * 100

    # print the candidate name and vote count
    print(f"{candidate} received {vote_percentage:.1f}% of the vote.")
    print(f"{candidate}: {vote_percentage:.1f}% {votes:,}\n")

# 5. The winner of the election based on popular vote

    if votes > winning_count and vote_percentage > winning_percentage:
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate

winning_candidate_summary = (
    f"-------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------------\n"
)
print(winning_candidate_summary)

    