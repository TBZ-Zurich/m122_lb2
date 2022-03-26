from git import Repo
import csv
from datetime import date
import os

fields = ["Zielverzeichnis", "Datum", "Commit-Hash", "Author"]

filename = "university_records.csv"
baseDir = '/Users/lorispolenz/Documents/GitHub/tbz/m122/'
rows = []


my_list = os.listdir(baseDir)

for dire in my_list:
    directory = baseDir + dire
    if os.path.isdir(directory):

        try:
            repo = Repo(directory)
        except:
            print(dire, "is not a valid git repo")
            continue

        repo = Repo(directory)
        commits = list(repo.iter_commits())

        print(commits)

        for commit in commits:
            row = []

            row.append(dire)
            row.append(str(date.today()).replace("-", ""))
            row.append(commit.hexsha)
            row.append(commit.author)

            rows.append(row)


# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(rows)
