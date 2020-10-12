#The data we need to retrieve 
#1. The total number of votes cast
#2. A complete list of candidates who received votes 
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote 

#Add our dependencies
import os
import csv 
# Assign a variable for the file to load and the path.
file_to_load = 'foo/election_results.csv'
#Assign a variable to save the file to a path 
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_names = []
county_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
largest_county = ""
largest_county_count = 0
winning_county_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data: 

#To do:read and analyze the data here 
    # Read the file object with the reader function.
    reader = csv.reader(election_data)
     
    # Read and print the header row.
    header = next(reader)


     # Print each row in the CSV file.
    for row in reader:
          # 2. Add to the total vote count.
        total_votes += 1
        
         # Print the candidate name from each row.
        candidate_name = row[2]
         # 3: Extract the county name from each row.
        county_name = row[1]
          # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
             # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

    
# 4a: Write a decision statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_names:

            # 4b: Add the existing county to the list of counties.
            county_names.append(county_names)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] +=1

# Save the results to our text file.
with open("file_to_save", "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n "
        f"-------------------------\n "
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

       # 6a: Write a repetition statement to get the county from the county dictionary.
    for county in county_votes:

        # 6b: Retrieve the county vote count.
        votes = county_votes.get(county)
        # 6c: Calculate the percent of total votes for the county.
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (f"{county}: {vote_percentage:.1f}%({votes:,})\n")
         # 6d: Print the county results to the terminal.
        print(county_results)
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
         # 6f: Write a decision statement to determine the winning county and get its vote count.
    if (votes > largest_county_count) and (vote_percentage > winning_county_percentage):
        largest_county_count = voteslargest_county = county
        winning_county_percentage = vote_percentage

    # 7: Print the county with the largest turnout to the terminal.
#winning_county_summary = (
        #f"-------------------------\n"
        #f"Winner: {largest_county}\n"
        #f"Winning Vote Count: {largest_county_count:,}\n"
        #f"Winning Percentage: {winning_county_percentage:.1f}%\n"
        #f"-------------------------\n")
#print(format(winning_county_summary)

   # 8: Save the county with the largest turnout to a text file.

#txt_file.write(winning_county_summary)


    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
    votes = candidate_votes.get(candidate_name)
        # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    print(candidate_results)
     #  Save the candidate results to our text file.
    txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
    if votes > winning_count and vote_percentage > winning_percentage:
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    #  Save the candidate results to our text file.
    txt_file.write(winning_candidate_summary)


    # Close the file.
    txt_file.close()



