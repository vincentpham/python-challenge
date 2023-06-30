import csv

election_data = '../Resources/election_data.csv'
results_file = 'election_results.txt'

with open(election_data, 'r') as csv_file:
    csvreader = csv.reader(csv_file)
    header = next(csvreader)  # Can't forget to skip the header row

    # Initialize variables
    total_votes = 0
    candidates = []
    candidate_votes = {}

    # Iterate through each row of the CSV file
    for row in csvreader:
        # Total number of votes cast
        total_votes += 1

        # Getting complete list of candidates who received votes
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates.append(candidate_name)

        # Adding up the vote count for each candidate
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

    # Calculating percentage of votes
    vote_percentage = {}
    for candidate in candidate_votes:
        vote_percentage[candidate] = (candidate_votes[candidate] / total_votes) * 100

    # Calculating winner
    candidate_winner = max(candidate_votes, key=candidate_votes.get)

    # Printing the analysis
    election_results =  f"Election Results\n" \
                        f"-------------------------------------\n"   \
                        f"Total Votes: {total_votes}\n"   \
                        f"-------------------------------------\n"   \

    print(election_results)

    # Continuation of results but have to loop trough
    # Don't forget to use .3f for 3 decimals instead of 2 like pybank

    for candidate in candidates:
        print(f"{candidate}: {vote_percentage[candidate]:.3f}% ({candidate_votes[candidate]})")
        
    print("-------------------------------------\n")
    print(f"Winner: {candidate_winner}\n")

    # I don't know how to add the for loop inside the election_results variable while still within
    # the with open function

    # Export the results to a text file
    # I will just keep it simple and have it print and write every line
    
    with open(results_file, 'w') as text_file:
        text_file.write("Election Results\n")
        text_file.write("----------------------------------------\n")
        text_file.write(f"Total Votes: {total_votes}\n")
        text_file.write("----------------------------------------\n")

        for candidate in candidates:
            text_file.write(f"{candidate}: {vote_percentage[candidate]:.3f}% ({candidate_votes[candidate]})\n")
            
        text_file.write("----------------------------------------\n")
        text_file.write(f"Winner: {candidate_winner}")

print("Results exported to", results_file)