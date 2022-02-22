#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The model file for the MVC structure of the phonebook program.
"""
from __future__ import absolute_import
import os.path
import pickle


class Person:
    '''
    Defines Person objects to be inserted
    '''

    def __init__(self, surname, name, telephone=None, address=None, city=None):
        '''
        Constructor for person
        '''
        self.set_surname(surname)
        self.set_name(name)
        self.telephone = telephone
        self.address = address.title().lstrip().rstrip()
        self.city = city.title().lstrip().rstrip()

    def set_surname(self, surname):
        '''
        Surname setter.
        '''
        if (isinstance(surname, str)
            and all(x.isalpha() or x.isspace() for x in surname)
                and len(surname) > 0):
            self.surname = surname.lstrip().rstrip()

    def get_surname(self):
        '''
        Surname getter.
        '''
        return self.surname

    def set_name(self, name):
        '''
        Name setter.
        '''
        if (isinstance(name, str)
            and all(x.isalpha() or x.isspace() for x in name)
                and len(name) > 0):
            self.name = name.lstrip().rstrip()

    def get_prenom(self):
        '''
        Surname getter.
        '''
        return self.name

    def get_telephone(self):
        '''
        Telephone getter.
        '''
        if self.telephone is not None:
            if str(self.telephone).isdigit():
                return self.telephone
            else:
                return ''

    def get_address(self):
        '''
        Address getter.
        '''
        # if self.address is not None:
        return self.address

    def get_city(self):
        '''
        City getter.
        '''
        # if self.city is not None:
        return self.city


class Ensemble:
    '''
    Defines Ensemble object, which will be the content of the notebook.
    '''

    def __init__(self):
        '''
        Ensemble class constructor.
        '''
        if os.path.isfile('output_new.pickle'):
            infile = open('output_new.pickle', 'rb')
            self.list_person = pickle.load(infile)
            infile.close()
            #print('Save file found.')
        else:
            self.list_person = {}

    def insert_person(self, person):
        '''
        Person insertion inside Ensemble behavior and verification.
        '''
        if isinstance(person, Person):
            if not hasattr(person, 'surname') or not hasattr(person, 'name'):
                print('For inserting, name and surname should be defined.')
                return None
            person.set_surname(person.get_surname().title())
            person.set_name(person.get_prenom().title())
            list_attributs = {}
            name = person.name
            surname = person.surname
            list_attributs['surname'] = surname
            list_attributs['name'] = name
            if person.telephone is not None:
                list_attributs['telephone'] = person.get_telephone()
            if person.address is not None:
                list_attributs['address'] = person.get_address()
            if person.city is not None:
                list_attributs['city'] = person.get_city()
            for information in self.list_person.values():
                if (surname == information['surname']
                        and name == information['name']):
                    self.list_person[f"{name} {surname}"] = list_attributs
                    return 'Person already exists. Data overwritten'
            self.list_person[f"{name} {surname}"] = list_attributs
            return "Inserted"
        return None

    def delete_person(self, person):
        '''
        Person removal from an Ensemble.
        '''
        if isinstance(person, (tuple, list)):
            names_fetched = []
            name_searched = person[0].title()
            prenom_searched = person[1].title()
           # if tel_searched
            for identification, information in self.list_person.items():
                try:
                    if (name_searched == information['surname']
                            and prenom_searched == information['name']):
                        names_fetched.append(identification)
                except KeyError:
                    next
            if len(names_fetched) > 0:
                for name in names_fetched:
                    del self.list_person[name]
                return names_fetched
            else:
                return None

    def display_all(self):
        '''
        Shows the content of the ensemble.
        '''
        content_display = []
        for value in self.list_person.values():
            content_display.append(value)
        return content_display

    # def search_person(self, category, name):
    #     names_fetched = []
    #     for identification, information in self.list_person.items():
    #         try:
    #             if surname in information[category]:
    #                 names_fetched.append(information)
    #         except KeyError:
    #             next
    #     if len(names_fetched) > 0:
    #         return names_fetched
    #     else:
    #         return None

    def search_person(self, person):
        '''
        Function to look up persons inside the Ensemble.
        '''
        if isinstance(person, (tuple, list)):
            names_fetched = []
            name_searched = person[0].title()
            prenom_searched = person[1].title()
            tel_searched = person[2]
            adresse_searched = person[3].title()
            ville_searched = person[4].title()
            # if tel_searched
            for information in self.list_person.values():
                try:
                    if (name_searched in information['surname']
                            and prenom_searched in information['name']):
                        names_fetched.append(information)
                        if tel_searched != '':
                            for fetched in names_fetched:
                                if tel_searched not in fetched['telephone']:
                                    names_fetched.remove(fetched)
                        if adresse_searched != '':
                            for fetched in names_fetched:
                                if adresse_searched not in fetched['address']:
                                    names_fetched.remove(fetched)
                        if ville_searched != '':
                            for fetched in names_fetched:
                                if ville_searched not in fetched['city']:
                                    names_fetched.remove(fetched)

                except KeyError:
                    next
            if len(names_fetched) > 0:
                return names_fetched
            else:
                return None

    def save(self):
        '''
        Function to save the model.
        '''
        file_to_write = open("output_new.pickle", "wb")
        pickle.dump(self.list_person, file_to_write)
        file_to_write.close()

    def __str__(self):
        '''
        To represent the print when needed.
        '''
        return str(self.list_person)
