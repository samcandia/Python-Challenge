import csv
import os

#creating empty lists and defining variables
totalvotes = 0
candidates = []
votes = {}
winner = 0 

path = os.path.join("Resources", "election_data.csv")
with open(path, 'r') as file:
    csvreader = csv.reader(file, delimiter=",")
    skipheader = next(csvreader)
    
#find total votes and candidate names    
    for row in csvreader:
        candidatename = row[2]
        totalvotes = totalvotes + 1

        if candidatename not in candidates: 
            candidates.append(candidatename)
            votes[candidatename] = 0
        votes[candidatename] = votes[candidatename] + 1

#begin exporting results 
with open("analysis.txt", 'w') as analysis:
     
    print1 = (f"Election Results\n" f"----------------\n" f"Total Votes:{totalvotes}\n" f"----------------\n")
    print(print1)
    analysis.write(print1)

calculate percent of votes and total votes for EACH candidate
    for candidates in votes: 
        percentage = (round(votes[candidates]/totalvotes * 100, 3))
        candidatetotal = votes.get(candidates)
        print2 = (f"{candidates} {percentage}% ({candidatetotal})\n")
        print(print2)
        analysis.write(print2)
        

        if candidatetotal > winner:
            winner = candidatetotal
            winningcandidate = candidates
      
    print3 = (f"----------------\n" f"Winner: {winningcandidate}")
    print(print3)
    analysis.write(print3)


    
