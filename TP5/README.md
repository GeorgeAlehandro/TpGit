# TP5 - INLO

## Introduction

This exercise was done in the context of a practical exercise around unittest for testing some functions around Linked Lists in python.  
_To know more about unittest:_  
https://docs.python.org/3/library/unittest.html

## Main goals
- Confirm that an empty Linked List is empty and that it's not empty if it isn't.  
- Adding an element in the beginning and the end of a Linked List are done in the right way.
- Adding then deleting an element will return the original list.

## Requirements
To run this test, python3 is needed to be installed along with the packages mentioned inside.  
The file linked_list.py needs to be on the same directory as the test_linked_list.py.


## About linked_list.py
It's the same script that was used in TP3 (https://github.com/GeorgeAlehandro/TpGit/blob/master/TP3/chained_list.py)
except that some unnecessary functions of the old script were removed. Also modified the constructor of the linked list
to accept LinkedList inputs (as a way to construct a linked list from an already available linked list).
Also new input verifications were added, specifically strings, floats, integers are now accepted directly inside the constructor.

## To run the script

```bash
git clone https://github.com/GeorgeAlehandro/TpGit/
python3 TpGit/TP5/test_linked_list.py
```

## Author
George Alehandro Saad
