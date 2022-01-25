#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
To launch commands based on chained_list.py
"""
from __future__ import absolute_import
from chained_list import ChainedList, random_gen, list_to_chained_list

if __name__ == "__main__":
    cl = ChainedList([1, 0, 4, 5, 3, 2, 6])
    cl.add_node(1.2)
    cl.add_node(6)
    # cl.add_node(6)
    # cl.add_first_node(9)
    # cl.delete_node(2)
    # cl.add_last_node(7)
    print(cl)
    print('Incoming iteration: ')
    for item in cl:
        print(item)
    print('The third element being: ' + str(cl[2]))
    cl[2]
    print('And the first: ' + str(cl.get(0)))
    cl.add_first_node(9)
    cl.add_last_node(3)
    print('9 was added at the beginning and 3 at the end: ', cl)
    cl.delete(1)
    cl.delete_node(6)
    print('Deleted the second element. And also deleted the value 6:', cl)
    print('The length of the Chained List is: ' + str(cl.length()))
    print('Example done for benchmarking adding last element in two cases: ')
    random_gen(180)
