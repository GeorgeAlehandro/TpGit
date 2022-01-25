# TP3 - INLO

## Introduction

This exercice was done in the context of a practical exercice around object oriented programming by creating a Chained List in python.  
_To know more about Chained Lists:_  
https://en.wikipedia.org/wiki/Linked_list

## Main goal
- Create a chained list based on the consecutive insertion of nodes in a sorted way.  
- Manipulate the chained list by deleting elements.
- Make the chained list itterable.

## Secondary goals
- Added other functions to get used to creating methods for a class.  
- Comparisons between randomly generated list and chained_list and observe the time each operation takes.
## Requirements
To run this test, python3 is needed to be installed along with the packages mentioned inside.  
The file chained_list.py needs to be on the same directory as the main.py.


## Input
Floats and integers are accepted by using the add_node() method.  
_Alternatively, a list can be given._

## Output
A chained list will be obtained.
## Optional methods:
### - add_first_node(value)
### - add_last_node(value)
### - length()
### - get(index)
### - delete(index)
### - delete_node(value)
## Optional functions:
### - random_gen(number):  
which calls chainedlist_gen(number), list_gen(number).  
Out of curiosity to find the difference in time between an operation on lists VS chained lists.  
Customized based on the aspect we would like to compare, for example:  
- Adding an element in the beginning of the list.
- Adding an element in the end of the list.
- Inserting elements in the middle.
- Sorting.
- ...
### - list_to_chained_list(input_list):  
Transforms an object of instance list into a Chained List.

## Author
George Alehandro Saad
