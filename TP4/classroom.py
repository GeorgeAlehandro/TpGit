#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Module that cotains the class Classroom out of the UML diagram,
not really necessary for the functions (optional for subjects)
'''


class Classroom:
    '''
    Class that defines all the characteristics of the subjects
    (See after: teacher, student)
    '''

    def __init__(self, class_id, capacity):
        self.class_id = class_id
        self.capacity = capacity

    def get_id(self):
        '''
        A method that calculates the mean of the grades for the subject object
        '''
        return self.class_id

    def get_cap(self):
        '''
        A method that calculates the mean of the grades for the subject object
        '''
        return self.capacity
