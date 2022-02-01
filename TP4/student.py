#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Module that cotains the class Student out of the UML diagram, necessary for the
functions
'''
from person import Person
from subject import Subject


class Student(Person):
    '''
    Class that unites all the basic of the Student objects
    Iherits from Person the basic information elements
    '''

    def __init__(self, lastname, firstname, phone_number, email, year_of_sub):
        super().__init__(lastname, firstname, phone_number, email)
        self.student_file = None
        if isinstance(year_of_sub, int):
            self.year_of_sub = year_of_sub
        else:
            print('Bad year of subscription format')

    def get_year_of_sub(self):
        '''
        To get the Student's year of sub
        '''
        return self.year_of_sub

    def set_year_of_sub(self, new_year):
        '''
        To change the Student's year of sub
        '''
        if isinstance(new_year, int):
            self.year_of_sub = new_year
        else:
            print('Bad year of subscription format')

    def add_course(self, subject, note=None):
        '''
        To add a course to the student's object
        It's a way to 'enroll' students in a course
        Not specifying a note will be considered as a non-graded subject.
        '''
        if isinstance(subject, Subject):
            if self.student_file is None:
                self.student_file = {}
            self.student_file[subject.name_of_subject] = note
            # Grade will be registered in the corresponding class
            subject.notes.append(note)
        else:
            print("Registered subject non existent.")

    def set_note(self, subject, note):
        '''
        Modifying a grade for a student already registered in that course.
        '''
        if subject.name_of_subject in self.student_file.keys():
            self.student_file[subject.name_of_subject] = note
        else:
            sentence = self.firstname + \
                ' not registered in ' + subject.name_of_subject
            print(sentence)

    def avg_grade_student(self):
        '''
        Calculates the general mean of the GRADED student courses.
        '''
        total = 0
        count = 0
        for val in self.student_file.values():
            if val is not None:
                # We dont count the subjects he hasnt been evaluated on yet
                total += val
                count += 1
        moyenne = total/count
        sentence = 'For student '+self.lastname+' '+self.firstname + \
            ' the average of the grades is: ' + str(moyenne) + '.'
        return sentence

    def not_graded(self):
        '''
        Searches for the not graded subjects of the student.
        '''
        count = 0
        not_graded = []
        for mat, val in self.student_file.items():
            if val is None:
                count += 1
                not_graded.append(mat)
        if len(not_graded) > 0:
            sentence = "The non-graded subjects are: " + \
                ''.join(not_graded) + ". Their total number is :" + str(count)
        else:
            sentence = 'All his/her subjects are graded.'
        return sentence

    def get_grades(self):
        '''
        Returns a dictionnary of all the subjects (and corresponding grades)
        that the student is enrolled at.
        '''
        sentence = 'His/her student file is as following ' + \
            str(self.student_file)
        return sentence
