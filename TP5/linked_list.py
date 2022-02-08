#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    linked_list.py contains three different classes with many methods that in
    the end build and manipulate Listed Links
"""
from __future__ import absolute_import


__author__ = 'George Alehandro Saad'


class Node:
    """
        Defines Nodes for the Linked List
    """

    def __init__(self, value=None):
        """
            Constructor for the class Node, with parameter node
        """
        self.value = value
        self.next = None  # Pointer to the next node

    def __str__(self):
        """
            The manner nodes are printed inside the linked lists
        """
        string = str(self.value)
        if self.next is not None:
            string += ", " + str(self.next)
        return string


class LinkedListIterator:
    """
        Defines the iteration for the Linked LIst
    """

    def __init__(self, begin):
        """
            Constructor for the class LinkedListIterator
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


class LinkedList:
    """
        Defines the Linked List, accepts str, float, int as one by one element
        or directly as a list or LinkedList
    """

    def __init__(self, nodes=None):
        """
            Constructor for the class LinkedList
        """
        self.first_node = None  # first_node = head
        if nodes is None:
            return
        if isinstance(nodes, (list, LinkedList)):
            for _ in nodes:
                self.add_last_node(_)
            return
        if isinstance(nodes, (str, float, int)):
            self.first_node = Node(nodes)
            return
        print("Format not accepted")

    def add_first_node(self, value):
        """
            Adds a node in the beginning of the Linked List
        """
        if self.first_node is None:
            self.first_node = Node(value)
        else:
            node = Node(value)
            node.next = self.first_node
            self.first_node = node

    def add_last_node(self, value):
        """
            Adds a node at the end of the Linked List
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
            Adds a node in the Linked List. The added node will be directly
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
                print('ERROR: '+str(value)+' already in the linked list.')
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
            To iterate over the different elements of the Linked List.
        """
        return LinkedListIterator(self.first_node)

    def length(self):
        """
            Shows the length of the Linked List by counting each node.
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

    def get_first_node(self):
        '''
        Returns the value of the first node of the linked list
        '''
        return self.first_node.value

    def get_last_node(self):
        '''
        Returns the value of the last node of the linked list
        '''
        curr = self.first_node
        while curr.next is not None:
            curr = curr.next
        return curr.value

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
            print(str(key) + ' element not found')
            return
        prev.next = cur_node.next
        cur_node = None

    def comparison(self, second_list):
        '''
        To compare between two different linked lists
        '''
        a_curr = self.first_node
        b_curr = second_list.first_node
        if self.length() != second_list.length():
            return False
        while (a_curr is not None and b_curr is not None):
            if a_curr.value != b_curr.value:
                return False
            a_curr = a_curr.next
            b_curr = b_curr.next
        return True

    def __str__(self):
        """
            The manner the linked lists are printed.
        """
        if self.first_node is None:
            return "liste vide"
        return str(self.first_node)

    def __getitem__(self, index):
        """
            Permits to call elements by using brackets '[]'
        """
        return self.get(index)
