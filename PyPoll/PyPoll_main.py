#Dependencies
import os
import csv

#variables / initial conditions
candidate = []
vote_count = {}
percentage = {}


total_votes = 0

#open csv
with open('PyPoll/Resources/election_data.csv', newline = '') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    next(csvreader, None)
    #cycle through data and append candidate list with candidate
    #increases vote counter by 1
    for row in csvreader:
        total_votes += 1
        if row[2] in candidate and row[2] not in "Candidate":
            vote_count[row[2]] = vote_count[row[2]] + 1
        #else create new spot in list for candidate
        else:
            candidate.append(row[2])
            vote_count[row[2]] = 1

#Percentage calculation
for key,value in vote_count.items():
    percentage[key] = str(round((value/total_votes)*100,3)) + "% ("+str(value)+ ")"

#winner
winner = max(vote_count.keys(), key=(lambda k: vote_count[k]))

#output to textfile
with open('output_election.txt','w',newline='') as textfile:
    print('Election Results', file = textfile)
    print('----------------------------------',file = textfile)
    print(f'Total Votes: {total_votes}', file = textfile)
    print('----------------------------------',file = textfile)
    print(f'Percentage: {percentage}', file = textfile)
    print('----------------------------------',file = textfile)
    print(f'Winner: {winner}', file = textfile)
    print('----------------------------------', file = textfile)

with open('output_election.txt',newline='')as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    for row in csvreader:
        print(row)