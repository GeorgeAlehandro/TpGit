#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_chained_list.py is used to test some functionalities of linked lists and
raise errors in case of error
"""
from __future__ import absolute_import
import unittest
from linked_list import LinkedList


class TestChainedList((unittest.TestCase)):
    '''
    Class that uses unittest to launch many tests around linked lists
    '''

    def setUp(self):
        """Initializing tests on a linked list of 3 elements."""
        self.liste = LinkedList()
        self.liste.add_node(1)
        self.liste.add_node(2)
        self.liste.add_node(3)  # A linked list made of 3 elements
        self.empty = LinkedList()  # An empty linked list to use in test_empty

    def test_empty(self):
        """Testing the emptiness of a newly created linked list."""
        self.assertIsNone(self.empty.first_node)

    def test_not_empty(self):
        '''Confirms that the linked list created in the beginning is not
        empty'''
        self.assertIsNotNone(self.liste.first_node)

    def test_add_first(self):
        '''Adding an element in the beginning of a linked list, will be indeed
        added in the beginning'''
        self.liste.add_first_node(10)
        self.assertIs(self.liste.get_first_node(), 10)

    def test_add_last(self):
        '''Adding an element in the end of a linked list, will be indeed
        added in the end'''
        self.liste.add_first_node(10)
        self.liste.add_last_node(20)
        self.assertIs(self.liste.get_last_node(), 20)

    def test_empi_depi_first_element(self):
        '''Push and Pop on first element will return the same original linked
        list'''
        # Creating a copy linked list called test, add then delete an element
        test = LinkedList(self.liste)
        test.add_first_node(100)
        test.delete(0)  # Something like push - pop but for a linked list
        # Check if it's still the same as original
        self.assertTrue(self.liste.comparison(test))

    def test_empi_depi_last_element(self):
        '''Push and Pop but on last element'''
        test = LinkedList(self.liste)  # I create a copy linked list
        test.add_last_node(100)
        test.delete_node(test.get_last_node())
        self.assertTrue(self.liste.comparison(test))


if __name__ == '__main__':
    unittest.main()
