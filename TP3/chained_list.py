#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    chained_list.py contains three different classes with many methods that in
    the end build and manipulate Listed Links
"""
from __future__ import absolute_import
from random import random
import time
import bisect

__author__ = 'George Alehandro Saad'


class Node:
    """
        Defines Nodes for the CHained List
    """

    def __init__(self, value=None):
        """
            Constructor for the class Node, with parameter node
        """
        self.value = value
        self.next = None  # Pointer to the next node

    def __str__(self):
        """
            The manner nodes are printed inside the chained lists
        """
        string = str(self.value)
        if self.next is not None:
            string += ", " + str(self.next)
        return string


class ChainedListIterator:
    """
        Defines the iteration for the Chained LIst
    """

    def __init__(self, begin):
        """
            Constructor for the class ChainedListIterator
        """
        self.first_node = begin

    def __next__(self):
        """
            Link between consecutive nodes to work as an itterator
        """
        if self.first_node is None:
            raise StopIteration
        item = self.first_node.value
        self.first_node = self.first_node.next
        return item


class ChainedList:
    """
        Defines the Chained List
    """

    def __init__(self):
        """
            Constructor for the class ChainedList
        """
        self.first_node = None  # first_node = head

    def add_first_node(self, value):
        """
            Adds a node in the beginning of the Chained List
        """
        if self.first_node is None:
            self.first_node = Node(value)
        else:
            node = Node(value)
            node.next = self.first_node
            self.first_node = node

    def add_last_node(self, value):
        """
            Adds a node at the end of the Chained List
        """
        if self.first_node is None:
            self.first_node = Node(value)
        else:
            node = Node(value)
            added_node = self.first_node
            while added_node.next is not None:
                added_node = added_node.next
            added_node.next = node

    def add_node(self, value):
        """
            Adds a node in the Chained List. The added node will be directly
            inserted in a sorted way.
        """
        curr = self.first_node
        if curr is None:
            node = Node(value)
            self.first_node = node
            return

        if curr.value > value:
            node = Node(value)
            node.value = value
            node.next = curr
            self.first_node = node
            return

        while curr.next is not None:
            if curr.next.value == value:
                print('ERROR: '+str(value)+' already in the chained list.')
                return
            if curr.next.value > value:
                break
            curr = curr.next
        node = Node(value)
        node.value = value
        node.next = curr.next
        curr.next = node
        return

    def __iter__(self):
        """
            To iterate over the different elements of the Chained List.
        """
        return ChainedListIterator(self.first_node)

    def length(self):
        """
            Shows the length of the Chained List by counting each node.
        """
        counted_node = self.first_node
        total = 0
        while counted_node is not None:
            # print(counted_node)
            total += 1
            counted_node = counted_node.next
        return total

    def get(self, index):
        """
            Extracts the value of a node in a specified index.
        """
        if index >= self.length() or index < 0:
            print('Index out of range')
            return None
        begin_index = 0
        node = self.first_node
        while True:
            if begin_index == index:
                return node.value
            node = node.next
            begin_index += 1

    def delete(self, index):
        """
            Deletes the node in a specified index.
        """
        if index >= self.length():
            print('ERROR: Out of range')
            return
        begin_index = 0
        node = self.first_node
        while True:
            if index == 0:
                self.first_node = self.first_node.next
                return self
            begin_index += 1
            last_node = node
            node = node.next
            if begin_index == index:
                last_node.next = node.next
                return self

    def delete_node(self, key):
        """
            Deletes the node based on a value.
        """
        cur_node = self.first_node
        if cur_node is not None:
            if cur_node.value == key:
                self.first_node = cur_node.next
                cur_node = None
                return
        while cur_node is not None:
            if cur_node.value == key:
                break
            prev = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None

    def __str__(self):
        """
            The manner the chained lists are printed.
        """
        if self.first_node is None:
            return "liste vide"
        return str(self.first_node)

    def __getitem__(self, index):
        """
            Permits to call elements by using brackets '[]'
        """
        return self.get(index)


def random_gen(number):
    """
        Calls the two functions to make a kind of time comparison between
        chained list and a list
    """
    chainedlist_gen(number)
    list_gen(number)


def chainedlist_gen(number):
    """
    Generates a Chained List and benchmarks the timing of a specified operation
    """
    clst = ChainedList()
    for _ in range(number):
        clst.add_node(random())
    start = time.time()
    clst.add_last_node(random())
    end = time.time()
    print(f"Runtime of the command on the Chained List is {end - start}")
    return clst


def list_gen(number):
    """
    Generates a list and benchmarks the timing of a specified operation
    """
    lst = []
    for _ in range(number):
        lst.append(random())
    lst.sort()
    start = time.time()
    bisect.insort(lst, random())
    lst.append(random())
    end = time.time()
    print(f"Runtime of the command on the list is {end - start}")
    return lst


def list_to_chained_list(input_list):
    """
    Generates a sorted chained list with unique values from an input list.
    """
    clst = ChainedList()
    for element in input_list:
        clst.add_node(element)
    return clst
