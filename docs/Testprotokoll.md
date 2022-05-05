Skript 1

| test number | testcase | test description | test preset | test data | expected test result | received test result | tester | testdate and test status |
| - | - | - | - | - | - | - | - | - |
| 1. | Wrong `-d` parameter | The script should be called with the parameter -d, but a wrong directory is given, one that does not exist. The program should detect the wrong directory and display an error message and also log the error to the log file. | The script should be installed correctly according to the documetation and the configuration file should be configured correctly. |  `git_clone_update_repos.sh -d /docs/myspace/gitrepository` In case this directory exists `/docs/myspace/gitrepository` you can replace it with another directory. | This should be the output: `Error path: don't exists, please create or enter the right path` | RECEIVED RESULT | TESTER | TESTDATE AND TEST STATUS |
| 2. | Right configuration file | The configuration file is filled with correct data. | The script should be installed correctly according to the documentation. | The config file should have following data for test porposes: ``` ``` To do this, a new empty folder must be created.| `All repositories cloned/updated successfull`  | RECEIVED RESULT | TESTER | TEST DATA AND TEST STATUS |
| 3. | Missing path in configuration File | If there is no targetfolder defined it should be cloned in the default aka installation path. | The script should be installed correctly according to the documentation. |  The config file should contain only this data for testing porposes: ```fff``` Please enter the keyword 'go' within 60 seconds after you staretd the clone proccess.| This message will appear: `Files will be cloned in the default repository please write "go"` There is a counter of 60 seconds. If the user don't enter the input 'go' into the console, the process will abord. | RECEIVED RESULT | TESTER | TEST DATE AND TEST STATUS |
| 4. | Wrong URL | If a wrong URL entered (alsow if it is not a git URL) the clone is skipped. | The script should be installed correctly according to the documentation. | Please configure the following config file: ```fff```| `The following URL isn't a git URL, please check and run the script again.` | RECEIVED RESULT | TESTER | TEST DATE AND TEST STATUS |
| 5. | Updating a repository works | If a repository has already been cloned it will be updated | Testcase 2.  successful | The config file should have following data for test porposes: To do this, a new empty folder must be created. | `All repositories cloned/updated successfull`| RECEIVED RESULT | TESTER | TEST DATE AND TEST STATUS | 

Cloning creating new repository


Skript 2

| Testfall | Testbeschreibung | Testdaten | erwartetes Testresultat | erhaltenes Testresultat | Tester | Testdatum und Teststatus |
|  - | - | - | - | - | - | - |
| Erstmaliger Aufruf | Das Skript soll mit einem Verzeichnis als parameter augerufen werden in welchem 2 Repos sind:<pre> skript2.bash /tmp/myrepos /tmp/commits.csv</pre> | Verzeichnis mit den GIT-Repos die mit dem Skript 1 geklont wurden:<pre>/tmp/myrepos</pre> | Alle Repos aus /tmp/myrepos werden gelesen und ein File /tmp/commits.csv erstellt mit allen Commits beider Repos | | | |
