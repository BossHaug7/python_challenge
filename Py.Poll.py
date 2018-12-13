import os
import csv

# Variables 1 
candidates = []
number_votes = 0
vote_counts = []

election_data = ['1', '2']

for files in election_data:
    election_data = csvpath = os.path.join("election_data.csv")
       
    with open(election_data) as csvfile:
        
        csvreader = csv.reader(csvfile, delimiter=',')
        
        line = next(csvreader,None)
        
        for line in csvreader:
            
            number_votes = number_votes + 1
            candidate = line[2]
            
            
            if candidate in candidates:
                candidate_index = candidates.index(candidate)
                vote_counts[candidate_index] = vote_counts[candidate_index] + 1
                
            else:
                candidates.append(candidate)
                vote_counts.append(1)
                
    percentages = []
    max_votes = vote_counts[0]
    max_index = 0
    
    for count in range(len(candidates)):
        vote_percentage = vote_counts[count]/number_votes*100
        percentages.append(vote_percentage)
        if vote_counts[count] > max_votes:
            max_votes = vote_counts[count]
            print(max_votes)
            max_index = count
    winner = candidates[max_index]
    
    percentages = [round(i,2) for i in percentages]
    
 #Print 
    print(f"Total Votes: {number_votes}")
    for count in range(len(candidates)):
        print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
    print(f"Winner:  {winner}")
    
    