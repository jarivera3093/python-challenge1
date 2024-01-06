import csv
import  os


csvpath = 'C:/Users/jariv/python-challenge/pyPoll/election_data.csv'

election_data_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'election_data.csv')
#print ('File:', election_data_csv)
print ('File:', csvpath)
with open (csvpath, encoding='UTF-8') as csvfile:  
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)  #  discard headers
    #Read the header row first
    row = next(csvreader)
    #print(f"CSV Header: {csv_header})

    #assign variables total rows 9not including the header is the total votes
    #votesCandidate
    totalVotes = 0
    votescandidates = {}
    #Read each row of data after the header
    for row in csvreader:
        totalVotes += 1
        candidate = row[2].strip()
        if candidate not in votescandidates:
            votescandidates[candidate] = 1
        else: 
            votescandidates[candidate] += 1

with open ('Election_Data_Results.txt', 'w') as file:

    #write to an output file
    
    print("Election Results")
    file.write("Election Results\n")
    print("---------------------------")
    print("Total Votes: " + str(totalVotes))
    print("---------------------------")

    file.write("---------------------------\n")
    file.write("Total Votes: " + str(totalVotes) + '\n')
    file.write("---------------------------\n")




    for candidate, votes in votescandidates.items():
        print(candidate + ": " + "{:.3%}".format(votes/totalVotes) + " (" + str(votes) + ")")
        file.write(candidate + ": " + "{:.3%}".format(votes/totalVotes) + " (" + str(votes) + ")\n")

    print("---------------------------")

    file.write("---------------------------\n")
    winner = max(votescandidates, key=votescandidates.get)

    print(f"Winner: {winner}")
    file.write(f"Winner: {winner}\n")

