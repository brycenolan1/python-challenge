#import csv
import os
import csv

#path to collect data from the given folder/file
poll_csv = os.path.join("election_data.csv")

#storing voter_id and candidate in a list
voter_id = []
candidate = []

#open csv file
with open(poll_csv,encoding="utf8") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

#append csvreader to voter_id and candidate lists while skipping header
    header = next(csvreader)
    for row in csvreader:
        voter_id.append(row[0])
        candidate.append(row[2])

#print results
print("Election Results")
print("---------------------------")
print(f"Total Votes: {len(voter_id)}")
print("---------------------------")

#get list of candidates values of specific candidates
cands = list(set(candidate))
cands.sort()

#get a vote count of candidates
vote_candidates = []
for cand in cands:
    vote_candidates.append(candidate.count(cand))

#list out pertectange and totals of votes with the winner of candidates
for i in range(len(cands)):
    print(f"{cands[i]}: {'{:.2%}'.format(vote_candidates[i]/len(candidate))} ({vote_candidates[i]})")
print("--------------------")
print(f"Winner: {cands[vote_candidates.index(max(vote_candidates))]}")
print("-------------------")


#write results to csv
with open("pypollmain_solved.csv", "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Election Results"])
    writer.writerow(["---------------------------"])
    writer.writerow([f"Total Votes: {len(voter_id)}"])
    writer.writerow(["---------------------------"])
    writer.writerow([f"{cands[i]}: {'{:.2%}'.format(vote_candidates[i]/len(candidate))} ({vote_candidates[i]})"])
    writer.writerow(["---------------------------"])
    writer.writerow([f"Winner: {cands[vote_candidates.index(max(vote_candidates))]}"])
    writer.writerow(["---------------------------"])