# Add our dependencies

import csv
import os

# Assign a variable to load a file from a path 
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")
# Initialize a total vote counter
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}
# Track the winning Candidate , vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row
    headers = next(file_reader)
    # Print each Row in the CSV file
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        #store the Candidate name for each row  
        candidate_name = row[2]
        #If the candidate does not match any existinfg candidate add it to the candidate list
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            #and begin tracking that cadidate's vote count
            candidate_votes[candidate_name]=0
        #Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save resukts to our text file
with open(file_to_save, "w") as txt_file:

    #Print the final vote cout to Terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n" 
        f"-------------------------\n"
    )
    print (election_results, end="")

    #Save the final vote count to the text file
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100

        # Store each candidate's name, vote count, and percentage of votes to a variable
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print out each candidate's name, vote count, and percentage of votes to terminal
        print(candidate_results)
        #Save the candidate_results to a txt file
        txt_file.write(candidate_results)
        #Determine winning vote count and candidate
        if(votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        

        # Print out the winning candidadt, vote count and percentage to terminal
    winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n"
        )
    print(winning_candidate_summary)

    #Save the winning candidate's name to the txt file
    txt_file.write(winning_candidate_summary)
    
