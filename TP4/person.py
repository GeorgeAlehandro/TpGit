#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Module that cotains the class Person out of the UML diagram, necessary for the
functions
'''


class Person:
    '''
    Class that unites all the basic characteristics of the persons objects
    (See after: teacher, student)
    '''

    def __init__(self, lastname, firstname, phone_number, email):
        if lastname.isalpha():
            self.lastname = lastname
        else:
            print('Bad last name input')
        if firstname.isalpha():
            self.firstname = firstname
        else:
            print('Bad first name input')
        if len(phone_number) == 10 and phone_number.isdigit():
            # Supposedly  we are in France (10 digits number)
            self.phone_number = phone_number
        else:
            print('Bad phone number input')
        if '@' in email:
            self.email = email
        else:
            print('Bad email input')

    def set_lastname(self, new_lastname):
        '''
        To set the Person's last name
        '''
        if new_lastname.isalpha():
            self.lastname = new_lastname
        else:
            print('Bad last name input')

    def set_firstname(self, new_firstname):
        '''
        To set the Person's first name
        '''
        if new_firstname.isalpha():
            self.firstname = new_firstname
        else:
            print('Bad first name input')

    def set_phonenumber(self, new_phone_number):
        '''
        To set the Person's phone number
        '''
        if len(new_phone_number) == 8 and new_phone_number.isdigit():
            self.phone_number = new_phone_number
        else:
            print('Bad phone number input')

    def set_email(self, new_email):
        '''
        To set the Person's email
        '''
        if '@' in new_email:
            self.email = new_email
        else:
            print('Bad email input')

    def get_information(self):
        '''
        To obtain the Person's basic information
        '''
        return self.firstname, self.phone_number, self.email
