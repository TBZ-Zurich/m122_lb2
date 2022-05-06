Skript 1

| Testfall | Testbeschreibung | Testdaten | erwartetes Testresultat | erhaltenes Testresultat | Tester | Testdatum und Teststatus |
|  - | - | - | - | - | - | - |
| Erstmaliger Aufruf | Das Skript soll mit einem input file aufgerufen werden, in welchem nur verfügbare Git-URLs sind. Diese sollen in ein noch nicht existierendes Verzeichnis geklont werden:<pre>skript1.bash repolist.txt /tmp/myrepos</pre> | repolist.txt mit folgendem Inhalt:<pre>https://gitlab.com/armindoerzbachtbz/m122_praxisarbeit<br>https://gitlab.com/wapdc/InfoSearch/Project-2017</pre> | Verzeichnis wird erstellt und alle Repos werden darin geklont | | | |


Skript 2

| Testfall | Testbeschreibung | Testdaten | erwartetes Testresultat | erhaltenes Testresultat | Tester | Testdatum und Teststatus |
|  - | - | - | - | - | - | - |
| Initial install | The tester follows all the steps described in the installation part of the [Documentation](./Betriebsdokumentation.md#Installation). The test will take place either on the tester's machine or in a provided Linux environment. The test will done by copying commands from the said documentation.| 1. The first command does clone the repository and enters the `bin` directory with the script. 2. The second command will exectue the script in the same directory as the clone was conducted. This will result in an output with the file gitlog.csv in the `bin` directory, since the default location will be taken. |  If the test is sucessfull, the script is installed and can be used in to comming test cases without any work needed to make an installation. || |
| Invalid target directory | The tester will enter a directory that does not exists `/User/danglang/thisdoesnotexis`.| - |The script will inform the user about the directory that was entered and that the directory does not exist.||
| Missing target directory | The tester will execute the script without defining any target directory.| - | The script will exit and inform the user that a target directory needs to be present at every given time. | |
| Custom output location + name | The tester will execute the script with a custom file location and name e.g. `~/Desktop/gitout.csv` Both relative and absolute path's are possible || The script will execute normally and palce the output file to the given path.||
| Non git directory | The user will create a directory in the same directory as the script was cloned. This directory however will not be a git repository. |-|  The script will inform the user about the name of the directory and that it is not a directory. The script will run, but exclude the said directory. |||
| CSV generation | The tester will execute the command defined in Test Case #1 and inspect the generated CSV file. The CSV File will have a correct header and every commit will be shown. To check for the ammount of the commits, the tester enters the following command within the `bin` directory and get a number. `git rev-list --count HEAD` The said number needs to be lower by 2 than the lines in the CSV (Header row and last empty row) | - | The two numbers generated in the test case will match. ||