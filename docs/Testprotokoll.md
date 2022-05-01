Skript 1

| test number | testcase | test description | test preset | test data | expected test result | received test result | tester | testdate and test status |
| - | - | - | - | - | - | - | - | - |
| 1. | Wrong `-d` parameter | The script should be called with the parameter -d, but a wrong directory is given, one that does not exist. The program should detect the wrong directory and display an error message and also log the error to the log file. | The script should be installed correctly according to the documetation and the configuration file should be configured correctly. |  `git_clone_update_repos.sh -d /docs/myspace/gitrepository` In case this directory exists `/docs/myspace/gitrepository` you can replace it with another directory. | This should be the output: `Error path: don't exists, please create or enter the right path` | RECEIVED TESTRESULT | TESTER |
| 2. | Right configuration file | The configuration file is filled with correct data. | The script should be installed correctly according to the documetation. | Hte config file should have following data for test porposes: ``` ``` |

Cloning creating new repository


Skript 2

| Testfall | Testbeschreibung | Testdaten | erwartetes Testresultat | erhaltenes Testresultat | Tester | Testdatum und Teststatus |
|  - | - | - | - | - | - | - |
| Erstmaliger Aufruf | Das Skript soll mit einem Verzeichnis als parameter augerufen werden in welchem 2 Repos sind:<pre> skript2.bash /tmp/myrepos /tmp/commits.csv</pre> | Verzeichnis mit den GIT-Repos die mit dem Skript 1 geklont wurden:<pre>/tmp/myrepos</pre> | Alle Repos aus /tmp/myrepos werden gelesen und ein File /tmp/commits.csv erstellt mit allen Commits beider Repos | | | |
