
#Add our dependencies
import os
import csv 
# Assign a variable for the file to load and the path.
file_to_load = os.path.join('foo',"election_results.csv")
#Assign a variable to save the file to a path 
file_to_save = os.path.join("analysis", "election_results.txt")

#  Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_names = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
largest_county = ""
largest_county_count = 0
winning_county_percentage = 0



# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data: 
    reader = csv.reader(election_data)
     
    # Read the header row.
    header = next(reader)

     # For each row in the CSV file.
    for row in reader:
          # Add to the total vote count.
        total_votes += 1
        
         # Get the candidate name from each row.
        candidate_name = row[2]
         # 3: Extract the county name from each row.
        county_name = row[1]
          # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
             # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

    
# 4a: Write a decision statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_names:

            # 4b: Add the existing county to the list of counties.
            county_names.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] +=1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

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
    for county_name in county_votes:

        # 6b: Retrieve the county vote count.
        votes_1 = county_votes.get(county_name)
        # 6c: Calculate the percent of total votes for the county.
        county_percentage = float(votes_1) / float(total_votes) * 100
        county_results = (f"{county_name}: {county_percentage:.1f}%({votes_1:,})\n")
         # 6d: Print the county results to the terminal.
        print(county_results)
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
         # 6f: Write a decision statement to determine the winning county and get its vote count.
        if (votes_1 > largest_county_count) and (county_percentage > winning_county_percentage):
            largest_county_count = votes_1
            largest_county = county_name

       

   #7: Print the county with the largest turnout to the terminal.
    winning_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"-------------------------\n")
    print(winning_county_summary)

   # 8: Save the county with the largest turnout to a text file.

    txt_file.write(winning_county_summary)


    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:
            # Retrieve vote count of a candidate.
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
                f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate's voter count and percentage to the
        #terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

    # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    # Print the winning candidate (to terminal)
    print(winning_candidate_summary)

    #  Save the candidate results to our text file.
    txt_file.write(winning_candidate_summary)


    # Close the file.
    txt_file.close()



