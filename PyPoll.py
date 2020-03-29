import csv
import os
# loads election results file, opens it for reading
file_to_load = os.path.join("Resources", "election_results.csv")
# creates a file to write to
file_to_save = os.path.join("analysis", "election_analysis.txt")

# opens the election results file and reads it
with open(file_to_load) as election_data:
     file_reader = csv.reader(election_data)

     # reads and prints header row
     headers = next(file_reader)
     print(headers)
   


#total number of votes cast


# complete list of canditates that recieved votes


# percentage of votes won for each candidate


# total number of votes each candidate won


# winner of election based on pop vote

