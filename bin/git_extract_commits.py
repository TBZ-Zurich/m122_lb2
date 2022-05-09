#! /bin/python3

from git import Repo
import csv
import os
import argparse
from logger import logInformation, logWarning


FIELDS = ["Zielverzeichnis", "Datum", "Commit-Hash", "Author"]

TARGET_DIRECTORY = ''
CWD = os.getcwd()
rows = []

# Handle arguments
parser = argparse.ArgumentParser()

parser.add_argument(
    "-o", "--Output", help="Ouput location and filename", default="./gitlogs.csv")
parser.add_argument("-d", "--Directory",
                    help="Target directory with the git repos", required=True)

args = parser.parse_args()

OUTPUT_LOCATION = args.Output
TARGET_DIRECTORY = args.Directory


def dtToDateString(datetime):
    dateStr = ["%s" % datetime.year,
               ("0%s" % datetime.month)[-2:], ("0%s" % datetime.day)[-2:]]
    return "".join(dateStr)


def validate_target_dir(target_dir):
    if os.path.isdir(target_dir) == False:
        print(target_dir + 'is an invalid directory, exit')
        exit()


validate_target_dir(TARGET_DIRECTORY)
sub_target_dirs = os.listdir(TARGET_DIRECTORY)

for subdir in sub_target_dirs:
    directory = TARGET_DIRECTORY + subdir
    if os.path.isdir(directory):

        try:
            Repo(directory)
        except:
            logWarning(subdir + "is not a valid git repo, skipping")
            continue

        repo = Repo(directory)

        # check if repo has any commits
        try:
            repo.iter_commits()
        except:
            logWarning(subdir + "has no commits yet, skipping")
            continue

        commits = list(repo.iter_commits())

        for commit in commits:
            rows.append([subdir, dtToDateString(
                commit.authored_datetime), commit.hexsha, commit.author])


with open(str(OUTPUT_LOCATION), 'w') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(FIELDS)

    csvwriter.writerows(rows)

logInformation("successfully saved the logs to csv")
