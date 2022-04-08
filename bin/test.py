#! /bin/python3
from git import Repo
import csv
import os
import argparse


FIELDS = ["Zielverzeichnis", "Datum", "Commit-Hash", "Author"]

FILENAME = "gitlogs.csv"
TARGET_DIRECTORY = ''
CWD = os.getcwd()
rows = []

# Handle arguments
parser = argparse.ArgumentParser()

parser.add_argument(
    "-o", "--Output", help="Ouput location and filename", default="gitlogs.csv")
parser.add_argument("-d", "--Directory",
                    help="Target directory with the git repos", required=True)

args = parser.parse_args()

OUTPUT_LOCATION = args.Output
TARGET_DIRECTORY = args.Directory


def dtToDateString(datetime):
    dateStr = ["%s" % datetime.year,
               ("0%s" % datetime.month)[-2:], ("0%s" % datetime.day)[-2:]]
    return "".join(dateStr)


my_list = os.listdir(TARGET_DIRECTORY)

for dire in my_list:
    directory = TARGET_DIRECTORY + dire
    if os.path.isdir(directory):

        try:
            repo = Repo(directory)
        except:
            print(dire, "is not a valid git repo")
            continue

        repo = Repo(directory)
        commits = list(repo.iter_commits())

        for commit in commits:
            row = []

            row.append(dire)
            row.append(dtToDateString(commit.authored_datetime))
            row.append(commit.hexsha)
            row.append(commit.author)

            rows.append(row)


with open(str(OUTPUT_LOCATION), 'w') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(FIELDS)

    csvwriter.writerows(rows)
