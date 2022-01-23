#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import random
import time
import bisect


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None  # Pointer to the next node

    def __str__(self):
        # return str(self.value)
        string = str(self.value)
        if self.next != None:
            string += ", " + str(self.next)
        return string


class LinkedListIterator:

    def __init__(self, begin):
        self.first_node = begin

    def __next__(self):
        if self.first_node == None:
            raise StopIteration
        else:
            item = self.first_node.value
            self.first_node = self.first_node.next
        return item


class ChainedList:
    def __init__(self):
        self.first_node = None  # first_node = head

    def add_first_node(self, value):
        if self.first_node == None:
            self.first_node = Node(value)
        else:
            node = Node(value)
            node.next = self.first_node
            self.first_node = node

    def add_last_node(self, value):
        if self.first_node == None:
            self.first_node = Node(value)
        else:
            node = Node(value)
            added_node = self.first_node
            while added_node.next != None:
                added_node = added_node.next
            added_node.next = node

    def add_node(self, value):
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
                print('ERROR: '+str(value)+' already added in the chained list.')
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
        return LinkedListIterator(self.first_node)

    def length(self):
        # print(self.first_node)
        counted_node = self.first_node
        total = 0
        while counted_node != None:
            # print(counted_node)
            total += 1
            #print('total is' + str(total))
            counted_node = counted_node.next
            #print('coming up next'+str(counted_node))
        return total

    def get(self, index):
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
        if index >= self.length():
            print('ERROR: Out of range')
            return
        begin_index = 0
        node = self.first_node
        while True:
            if index == 0:
                temp = self.first_node
                self.first_node = self.first_node.next
                temp = None
                return self
            begin_index += 1
            last_node = node
            node = node.next
            if begin_index == index:
                last_node.next = node.next
                return self

    def deleteNode(self, key):

        # Store head node
        temp = self.first_node

        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.value == key):
                self.first_node = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while(temp is not None):
            if temp.value == key:
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if(temp == None):
            return

        # Unlink the node from linked list
        prev.next = temp.next

        temp = None
    # def remove_node(self, target_node_data):
    #     if self.first_node is None:
    #         raise Exception("List is empty")
    #     if self.first_node.value == target_node_data:
    #         self.first_node = self.first_node.next
    #         return
    #     previous_node = self.first_node
    #     for node in self:
    #         if node == target_node_data:
    #             previous_node.next = node.next
    #             return
    #         previous_node = node
    #     raise Exception("Node with data '%s' not found" % target_node_data)

    def __str__(self):
        if self.first_node is None:
            return "liste vide"
        return str(self.first_node)

    def __getitem__(self, index):
        return self.get(index)


def random_gen(number):
    chainedlist_gen(number)
    list_gen(number)


def chainedlist_gen(number):
    cl = ChainedList()
    for _ in range(number):
        cl.add_node(random())
    start = time.time()
    cl.add_last_node(random())
    end = time.time()
    print(f"Runtime of the program is {end - start}")
    return cl


def list_gen(number):
    l = []
    for _ in range(number):
        l.append(random())
    l.sort()
    start = time.time()
    bisect.insort(l, random())
    l.append(random())
    end = time.time()
    print(f"Runtime of the program is {end - start}")
    return l


cl = ChainedList()
cl.add_node(1)
cl.add_node(2)
cl.add_node(3)
cl.add_node(6)
cl.add_node(6)
# cl.add_first_node(9)
# cl.deleteNode(2)
# cl.add_last_node(7)
print(cl)
print(cl[2])
cl[2]
# print(cl.length())
# print(cl)
# print(cl.extract(0))
# print(cl.delete(0))
# print(cl.delete(0))


# print(cl.delete(2))
# print(cl.delete(4))
# random_gen(900)

# print(cl.delete(2))
# print(cl.delete(4))
random_gen(9000)
