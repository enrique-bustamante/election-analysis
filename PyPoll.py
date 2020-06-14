# the data we need to retrieve
import os
import csv
# assign variables for the file to load and the path as well as to save
file_to_load = os.path.join('Resources','election_results.csv')
file_to_save = os.path.join('Analysis', 'election_results.txt')
# open the election results and read the file
with open(file_to_load) as election_data:
  #To-do: read and analyze data here
  file_reader = csv.reader(election_data)
  headers = next(file_reader)
  print(headers)

 

# 1. the total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
