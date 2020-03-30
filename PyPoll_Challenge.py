import csv
import os
# loads election results file, opens it for reading
file_to_load = os.path.join("Resources", "election_results.csv")
# creates a file to write to
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initializes variable for total votes
total_votes = 0
#initializes the candidate and county options
candidate_options = []
county_options = []
# initializes candidate and county vote dictionaries
candidate_votes= {}
county_votes = {}
# initializes winning county info
winning_county = ""
winning_county_count = 0
winning_county_percentage = 0
# initializes winning candidate info
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
		
		# gets list of canditates and counties that recieved votes
		county = row[1]
		candidate = row[2]

		# adds county name to county list
		if county not in county_options:
			county_options.append(county)
            # begins tracking county vote count
			county_votes[county] = 0

        # adds vote to county for every new instance of the county name
		county_votes[county] += 1

        #adds candidate names to candidate list
		if candidate not in candidate_options:
			candidate_options.append(candidate)
			# begins tracking candidates vote count
			candidate_votes[candidate] = 0

		# adds vote to the value of the key which is candidates name
		candidate_votes[candidate] += 1

	# writes and prints winning county & candidate to text file & terminal
	with open(file_to_save, "w") as txt_file:
		# creates header and prints the total votes for the election
		election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
		print(election_results, end="")
    	# Save the final vote count to the text file.
		txt_file.write(election_results)
		
		# creates header for county votes
		print("County Votes:")
		txt_file.write("\nCounty Votes:\n")

        # gets/ prints/ writes count and % for county; gets winning info 
		for county in county_options:
			# gets county name, vote count, and percentage
			county_tally = county_votes[county]
			county_percentage = county_tally/ total_votes * 100
            
			# gets and prints county name, vote count, and percentage
			county_results = (f"{county}: {county_percentage:.1f}% ({county_tally:,})\n")
			print(county_results)

			#writes county results to election_analysis.txt
			txt_file.write(county_results)
			
			# gets county with the largest voter turnout
			if ((county_tally > winning_county_count) and (county_percentage > winning_county_percentage)):
				# if this above statement is true, then this county WINS
				winning_county_count = county_tally
				winning_county_percentage = county_percentage
				winning_county = county

		# this formats and prints the winning county's information
		winning_county_summary = (
			f"\n-------------------------\n"
			f"Largest County Turnout: {winning_county}\n"
			f"-------------------------\n\n")
		print(winning_county_summary)
		# writes winning county information to txt file
		txt_file.write(winning_county_summary)

		# count and percentage of votes won for each candidate 
		for candidate in candidate_options: 
            # gets candidate name, vote count, and percentage
			votes = candidate_votes[candidate]
			vote_percentage = votes/ total_votes * 100

			# gets and prints candidate name, vote count and percentage
			candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
			print(candidate_results)

			# saves candidate results to txt file
			txt_file.write(candidate_results)

			# checks if votes and % is higher than previous candidate
			if ((votes > winning_count) and (vote_percentage > winning_percentage)):

				# if above is true, then this candidate WINS and had this count, %
				winning_count = votes
				winning_percentage = vote_percentage
				winning_candidate = candidate
		
		# this formats and then prints the winning candidate's information
		winning_candidate_summary = (
			f"\n-------------------------\n"
			f"Winner: {winning_candidate}\n"
			f"Winning Vote Count: {winning_count:,}\n"
			f"Winning Percentage: {winning_percentage:.1f}%\n"
			f"-------------------------\n")
		print(winning_candidate_summary)
		# writes winning candidate's summary to txt file
		txt_file.write(winning_candidate_summary)