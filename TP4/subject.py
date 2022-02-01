#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Module that cotains the class Subject out of the UML diagram, necessary for the
functions
'''
from classroom import Classroom


class Subject:
    '''
    Class that defines all the characteristics of the subjects
    (See after: teacher, student)
    '''

    def __init__(self, name_of_subject):
        self.name_of_subject = name_of_subject
        self.classroom = None
        self.notes = []

    def set_classroom(self, class_to_set):
        '''
        A method that indicates the classroom of a subject
        '''
        if not isinstance(class_to_set, Classroom):
            return('Classroom non existent')
        else:
            if self.classroom is None:
                self.classroom = class_to_set
                print('Succesfully set to: '+class_to_set.class_id)
            elif self.classroom != class_to_set:
                confirmation = input(
                    "Please confirm your choice by typing Y/N" + '\n')
                if confirmation.upper() == 'Y':
                    self.classroom = class_to_set
                    print('The classroom for this subject ' +
                          'has been changed to: ' + str(class_to_set.class_id))
                elif confirmation.upper() == 'N':
                    print('Confirmation failed.')
                else:
                    self.setclassroom(class_to_set)
            else:
                print('Classroom number inserted is the same as before.')

    def avg_subj_grade(self):
        '''
        A method that calculates the mean of the grades for the subject object
        '''
        if not self.notes:
            return 'Grades are not available for this subject.'
        total = 0
        count = 0
        for note in self.notes:
            if note is not None:
                total += note
                count += 1
        avg_grade = total/count
        sentence = 'The average grade for ' + \
            self.name_of_subject+' is: ' + str(avg_grade)
        return sentence

    def all_subj_grades(self):
        '''
        Extract all the subjects grades
        '''
        sentence = ('All the grades in subject ' + self.name_of_subject +
                    ' are ' + (', '.join(str(grade) for grade in self.notes)))
        return sentence

    def modify_classroom(self, new_classroom):
        '''
        Sets the classroom of a subject, in case of change, prompts.
        '''
        if not isinstance(new_classroom, Classroom):
            return('Classroom non existent')
        if self.classroom != new_classroom:
            confirmation = input(
                "Please confirm your choice by typing Y/N" + '\n')
            if confirmation.upper() == 'Y':
                self.classroom = new_classroom
                print('The classroom for this subject' +
                      ' has been changed to: ' + str(new_classroom))
            elif confirmation.upper() == 'N':
                print('Confirmation failed.')
            else:
                self.setclassroom(new_classroom)
        else:
            print('Classroom number inserted is the same as before.')
