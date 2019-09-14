import os 
import csv

csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath, newline = "") as csvfile:


        csvreader = csv.reader(csvfile)
        csv_header = next(csvfile)

        Candidates = {}
        Count = 0
        Votes_casted = 0
        Percentage_of_votes = 0
        Most_votes = 0
        Most_voted = ""

        for row in csvreader:

            candidate = row[2]
            Count += 1

            if candidate in Candidates.keys():
               Candidates[candidate] += 1
            
            else:
                Candidates[candidate] = 1

print("Election Results")
print("-------------------")
print(f"Total Votes:{Count}")
print("-------------------")

for candidate in Candidates:
    Votes_casted += Candidates[candidate]
    Percentage_of_votes = (Candidates[candidate])/(Count) * 100
    print(f"{candidate}: {int(Percentage_of_votes)}% {Votes_casted}")
   
    if Candidates[candidate] > Most_votes:
        Most_voted = candidate
        Most_votes = Candidates[candidate]

print("-------------------")
print(f"Winner, {Most_voted}")
print("-------------------")