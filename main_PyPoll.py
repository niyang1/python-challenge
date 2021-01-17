# Import Dependencies
import os, csv
import statistics

# create variable to store path location 
elections_d = os.path.join("PyPoll",'Resource', "election_data.csv")

# Declare Variables 
total_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Open csv 
with open(elections_d,newline="", encoding="utf-8") as elections:

    # create variable csvreader to store budget.csv info
    csvreader = csv.reader(elections) 

    # Skip the header 
    header = next(csvreader)     

    # loop through cvs
    for row in csvreader: 

        # Count the votes
        total_votes +=1

        # Use if statements to loop through names and assign to list 
        if row[2] == "Khan": 
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

 # Create list of Candidates
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes,li_votes,otooley_votes]

candidates_votes = dict(zip(candidates,votes))
Winner = max(candidates_votes, key=candidates_votes.get)

# Get Vote %
khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes)* 100
otooley_percent = (otooley_votes/total_votes) * 100

# Print the summary table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {Winner}")
print(f"----------------------------")

# Output files
# Assign output file location and with the pathlib library
elections_d = os.path.join("PyPoll",'Resource', "Election_analysis.txt")

with open(elections_d,"w") as file:

# Write methods to print to Elections_Results_Summary 
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Khan: {khan_percent:.3f}% ({khan_votes})")
    file.write("\n")
    file.write(f"Correy: {correy_percent:.3f}% ({correy_votes})")
    file.write("\n")
    file.write(f"Li: {li_percent:.3f}% ({li_votes})")
    file.write("\n")
    file.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {Winner}")
    file.write("\n")
    file.write(f"----------------------------")
