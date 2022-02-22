# TP6 - MVC

## Introduction

This exercise was done in the context of a practical exercise around MVC programming architecture. We are building a phone book.
_To know more about MVC:_
https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller

## Main goals
- Implement all the needed files, classes, methods to create a Phone Book.
- Each person should be indexed by his name.

## Secondary goals
- The files can be saved by using the pickle package.
- Integrate a cli view beside the tkinter one.
## Requirements
To run this test, python3 is needed to be installed along with the packages mentioned inside including _ttkwidgets_.
```bash
pip install ttkwidgets
```
All the files should be in the directory.


## About main.py
To run the program, we should call
```bash
python3 main.py -h
```
With -h all the possible arguments will be shown, including:
```bash
python3 main.py -g
```
which directly runs the GUI mode on tkinter.
Alternatively the user might directly run:
```bash
python3 tkinter_run.py
```
## About the data storage
Each entry is stored inside a nested dictionnary, whose key will be the name and surname of the person (so each name and surname combo is unique). The value of this dictionnary is a dictionnary of the different elements of informations of each person with its value.
## About Pickle
A package used to save the progress of writing the contacts and load the Phone Book on launch.
The file will check for the presence of a pickle save file on launch, if not found will create a new one.
## Data representation
When showing the content of the book or while searching, the data will be presented in a Treeview.
## Two ways to delete an entry
Either by entering the exact surname and name then deleting.  
Or by using the Tkinter interface and then Display or Search and click the entries that you are willing to delete.
## Things I could improve
Create a random ID for each person inserted that replaces the key value of the dictionnary, this way people with the same name and surname can co-exist inside the Phone Book. Then I could modify the delete function to prompt the user for his choice of which contact should be deleted.
## To run the script

```bash
git clone https://github.com/GeorgeAlehandro/TpGit/
python3 TpGit/TP6/main.py -h
```

## Author
George Alehandro Saad
