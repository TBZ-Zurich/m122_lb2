import argparse, os, git, logger, shutil, glob
from git import Repo


# Parser for argument

parser = argparse.ArgumentParser(description="This clones all your git repos to your doirectory",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-d", "--dir",
                    help="You can enter your base directory here", required=True)
args = parser.parse_args()
BASE_DIR = args.dir

# Checks if the config file exists

if os.path.exists("gitclone.config"):
    logger.logInformation("The configfile does exists")
else:
    logger.logError("The config file does not exists, please read the readme.md file")
    quit()

# Reads the config file

with open("gitclone.config") as config_file:
    while (line := config_file.readline().rstrip()):
        config_line = line.split()
        logger.logInformation(config_line[0] + ' ' + config_line[1])
        if os.path.isdir(BASE_DIR + '/' + config_line[1]): # Checks if repo is already cloned
            g = git.cmd.Git(BASE_DIR + '/' + config_line[1])
            g.fetch()
            g.pull()
        elif not os.path.isdir(BASE_DIR + '/' + config_line[1]): 
            Repo.clone_from(config_line[0], BASE_DIR + '/' + config_line[1])

    # If the folder is not in config file, it deletes the folder ion the BASE_DIR

    dir_list = os.listdir(BASE_DIR + '/') 
    for count in dir_list:
        logger.logInformation('Checking if dir ' + count + ' exists')
        with open('gitclone.config') as config_file:
            if not(count in config_file.read()):
                shutil.rmtree(BASE_DIR + '/' + count)
                logger.logInformation("Removed " + count)