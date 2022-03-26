# Projekt Dokumentation

[[_TOC_]]

## Lösungsdesign
Anhand der Analyse wurde folgendes Lösungsdesign entworfen.

### Aufruf der Skripte

### Script 2
When calling the script only two params are needed. The location of the directory that contains the cloned repositories and name of the output file. 

To define the directory use the `-d` tag and with `-o` it is possible to define the location, name and file ending of the output file. By default the file gets put into the current working directory named `gitLog.csv`.

This script can be called using the following command `script.py -o /home/root/result.txt -d /home/root/Downloads`. 

TODO: schreiben sie wie die Skripte aufgerufen werden sollen (d.h. welche Parameter werden übergeben, gibt es Interaktionen mit dem Skript, läuft es automatisch täglich ab?)

### Ablauf der Automation
The following section shows the UML Activity Diagrams of our scripts.
### Script 1

### Script 2

### Konfigurationsdateien
The following section shows the configuration file that is used to run both of our scripts.

TODO: Definieren sie welche Parameter in welchen Konfigurationsdateien gespeichert werden.

## Abgrenzungen zum Lösungsdesign

TODO: Nachdem das Programm verwirklicht wurde hier die unterschiede von der Implemenatino zum Lösungsdesign beschreiben (was wurde anders gemacht, was wurde nicht gemacht, was wurde zusaetzlich gemacht)