# import modules that we'll utilize
import os
import csv
# assign variables for the file to load and the path as well as to save
file_to_load = os.path.join('Resources','election_results.csv')
file_to_save = os.path.join('Analysis', 'election_results.txt')

# initialize vote counter
total_votes = 0
# initialize list of counties
county_names = []
# initialize dictionary to store county vote counts
county_votes = {}
# initialize list of candidate names
candidate_options = []
#initialize dictionary to store candidate votes
candidate_votes = {}

# initialize array for county with highest turnout
county_highest_vote = ""
high_county_vote = 0

# initialize arrays for winning candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# open the election results and read the file
with open(file_to_load) as election_data:
  #To-do: read and analyze data here
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    # iterate though data to find values
    for row in file_reader:
      # this adds up the total vote count
      total_votes += 1

      # this aggregates the data for the counties
      county_name = row[1]
      if county_name not in county_names:
        # this adds county name to list if not on there already
        county_names.append(county_name)

        # this sets up array for county and sets value to zero
        county_votes[county_name] = 0

      # this keeps running tally of count of votes per county
      county_votes[county_name] += 1

      # this aggregates the data for the candidates
      candidate_name = row[2]
      if candidate_name not in candidate_options:

        #this adds a candidate's name to the list if not already on there
        candidate_options.append(candidate_name)

        #this sets up arrays for each candidate and sets value to zero
        candidate_votes[candidate_name] = 0

      # this tallies votes for each candidate
      candidate_votes[candidate_name] += 1

  # send information over to final destination file
with open(file_to_save, "w") as txt_file:

      # Print the final vote count to the terminal.
      election_results = (
          f"\nElection Results\n"
          f"-------------------------\n"
          f"Total Votes: {total_votes:,}\n"
          f"-------------------------\n"
          f"\nCounty Votes:\n")
      print(election_results, end="")

      # Save the final vote count to the text file.
      txt_file.write(election_results)

      # iterate through county data
      for county in county_votes:

        # tallies the vote count for each county in a local value
        c_votes = county_votes[county]

        # calculates the vote percentage by county in a local value
        c_vote_percentage = int(c_votes)/int(total_votes) * 100

        # sets local variable to disply the county name, vote count, and vote percentage
        county_results = (
          f"{county}: {c_vote_percentage:.1f}% ({c_votes})\n"
        )

        # print the county results
        print(county_results)

        # write county results onto txt_file
        txt_file.write(county_results)

        # find out the county with the highest participation
        if c_votes > high_county_vote:
          high_county_vote = c_votes
          county_highest_vote = county

      # set variable for info to print
      highest_county = (
        f"\n-------------------------\n"
        f"Largest county turnout: {county_highest_vote}\n"
        f"-------------------------\n"
      )

      # print county values
      print(highest_county)

      # write county highest value to txt_file
      txt_file.write(highest_county)

      # iterate through candidate data
      for candidate in candidate_votes:

        # retrieve number of votes for each candidate
        votes = candidate_votes[candidate]

        # calculate the percentage of vote
        vote_percentage = int(votes)/int(total_votes) * 100

        # print the candidate name and vote count
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # print the candidate results
        print(candidate_results)

        # write results onto txt_file
        txt_file.write(candidate_results)

      # Finds the winner of the election based on popular vote
          # sets condition to find the candidate with most vote count and percentage
        if votes > winning_count and vote_percentage > winning_percentage:
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate

      #print(winning_candidate_summary)
      winning_candidate_summary = (
          f"----------------------------\n"
          f"Winner: {winning_candidate}\n"
          f"Winning Vote: {winning_count:,}\n"
          f"Winning Percentage: {winning_percentage:.1f}\n"
      )
      print(winning_candidate_summary)
      txt_file.write(winning_candidate_summary)