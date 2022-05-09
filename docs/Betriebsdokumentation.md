# Betriebsdokumentation
[[_TOC_]]
## Einführungstext 

This script clones all repositories if they are not present. If they are present, the corresponding repository is fetched.

TODO: @Loris

## Installationsanleitung für Administratoren

### Installation

The following script will ONLY work on a Linux machine!!!

Please make sure that at least python 3.7 and pip is installed. You can find a installation guide for python under this link: https://www.python.org/downloads/

Please make sure that git is installed on your device! You can find a installation guide for git under this link: https://git-scm.com/downloads

After that you can install the scripts with this command: 
`git clone https://github.com/TBZ-Zurich/m122_lb2.git`

Now you can go inside the cloned folder. Go into the bin folder and install git and all the dependencies. 

`pip install GitPython`

### Konfiguration

There is a gitclone.config.sample config file inside. The config file must be at the same directory as the script (git_clone_update_repos.py).

You're config file should be named `gitclone.config` and should have the following pattern:

```
gitURL path
https://github.com/microsoft/Web-Dev-For-Beginners.git test/
```

If this is not the case an error will be throwed and logged into the console and the log file.

If you want to run the script regularly just follow the instructions here: https://towardsdatascience.com/how-to-schedule-python-scripts-with-cron-the-only-guide-youll-ever-need-deea2df63b4e

TODO: Wie sind User-Home-Templates einzurichten

## Bediensanleitung Benutzer

TODO: Erzeugen der Input-Files beschreiben, falls noetig

Go to the following directory, after you downloaded it with: `cd m122_lb2/bin`. After you have configured everything and you are in the `bin` directory of the project you can start the script with `python3 git_clone_update_repos.py -d test/`. The `-d` tag stands for the base directory and is mandatory. You can replace the `test/` path with your base directory. If you have configured everything according to the operating documentation, then a clone/pull will work.


TODO: beschreiben der erzeugt files (falls solche erzeugt werden)

TODO: Lokation von logfiles und bekannte Fehlermeldungen beschreiben.

