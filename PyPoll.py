import csv
import os
# loads election results file, opens it for reading
file_to_load = os.path.join("Resources", "election_results.csv")
# creates a file to write to
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initializes variable(s) for total votes
total_votes = 0
candidate_options = []
candidate_votes= {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# opens the election results file and reads it
with open(file_to_load) as election_data:
	file_reader = csv.reader(election_data)

	# reads header row
	headers = next(file_reader)
	 
	#print row in csv file
	for row in file_reader:
		# gets a total number of votes cast by row count
		total_votes += 1
		
		# gets a complete list of canditates that recieved votes
		candidate = row [2]
		
		if candidate not in candidate_options:
			candidate_options.append(candidate)
			# begins tracking candidates vote count
			candidate_votes[candidate] = 0

		# adds vote to the value of the key which is candidates name
		candidate_votes[candidate] += 1

	 # count and percentage of votes won for each candidate 
	for candidate in candidate_options: 
		votes = candidate_votes[candidate]
		vote_percentage = votes/ total_votes * 100
		
		#prints candidate name, vote count and percentage
		print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

		# this checks if the votecount, % is higher than previous candidate
		if ((votes > winning_count) and (vote_percentage > winning_percentage)):

			# if above is true, then this candidate WINS and had this count, %
			winning_count = votes
			winning_percentage = vote_percentage
			winning_candidate = candidate
		
	winning_candidate_summary = (
		f"-------------------------\n"
    		f"Winner: {winning_candidate}\n"
    		f"Winning Vote Count: {winning_count:,}\n"
    		f"Winning Percentage: {winning_percentage:.1f}%\n"
    		f"-------------------------\n")
	print(winning_candidate_summary)

	


