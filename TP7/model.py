#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The model file for the MVC structure of the phonebook program.
"""
from __future__ import absolute_import
import os.path
import pickle
import mysql.connector

monServeur = "localhost"
monLogin = "root"
password = "root"


class Person:
    '''
    Defines Person objects to be inserted
    '''

    def __init__(self, idi, surname, name, telephone=None, address=None, city=None):
        '''
        Constructor for person
        '''
        if idi == '':
            self.idi = None
        else:
            self.idi = idi
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
        # if os.path.isfile('output_new.pickle'):
        #     infile = open('output_new.pickle', 'rb')
        #     self.list_person = pickle.load(infile)
        #     infile.close()
        #     #print('Save file found.')
        # else:
        #     self.list_person = {}
        self.connection = mysql.connector.connect(
            host=monServeur, user=monLogin, password=password, database="TP7")
        self.cursor = self.connection.cursor()

    def insert_person(self, person):
        '''
        Person insertion inside Ensemble behavior and verification.
        '''
        # UPDATE `person` SET `name` = 'New' WHERE `person`.`ID` = 1;

        if isinstance(person, Person):
            person_info = person.get_surname().title(), person.get_prenom(
            ).title(), person.telephone, person.address, person.city, person.idi
            print(person_info)
            if person.idi is not None:
                query = ("Select `ID` from `person`;")
                self.cursor.execute(query)
                for idi in self.cursor.fetchall():
                    if int(person.idi) == idi[0]:  # Match on id:
                        # UPDATE `person` SET `surname` = %s, `name` = %s, `telephone` = %s, `address` = %s, `city` = %s WHERE `person`.`ID` = 1;
                        query_2 = (
                            "UPDATE `person` SET `surname` = %s, `name` = %s, `telephone` = %s, `address` = %s, `city` = %s WHERE `person`.`ID` = %s;")
                        update = person_info
                        self.cursor.execute(query_2, update)
                        self.connection.commit()
            else:
                query = (
                    "INSERT INTO `person` (`ID`, `surname`, `name`, `telephone`, `address`, `city`) VALUES (NULL, %s, %s, %s, %s, %s);")
                insertion = person_info[:-1]
                self.cursor.execute(query, insertion)
                self.connection.commit()
                self.cursor.close()
                return "Inserted"
        return None

    def delete_person(self, person):
        '''
        Person removal from an Ensemble.
        '''
        if isinstance(person, (tuple, list)):
            query = ("DELETE FROM `person` WHERE `person`.`ID` = %s")
            number = tuple(person[0])
            print(type(number))
            self.cursor.execute(query, number)
            self.connection.commit()
            self.cursor.close()
            return number
        else:
            return None

    def display_all(self):
        '''
        Shows the content of the ensemble.
        '''
        query = ("select * from person")
        self.cursor.execute(query)
       # self.connection.commit()
        all_names = self.cursor.fetchall()
        return(all_names)

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
            id_searched = person[0]
            name_searched = person[1].title()
            prenom_searched = person[2].title()
            tel_searched = person[3]
            adresse_searched = person[4].title()
            ville_searched = person[5].title()
            fetch = [id_searched, name_searched, prenom_searched,
                     tel_searched, adresse_searched, ville_searched]
            construction = []
            ask = " WHERE "

            column_names = ['ID', 'surname', 'name',
                            'telephone', 'address', 'city']
            for number in range(len(column_names)):
                if fetch[number] != '':
                    if ask != " WHERE ":
                        ask += " AND "
                   # construction += "'"+str(fetch[number])+"',"
                    fetch[number] = fetch[number] + '%'
                    construction.append(fetch[number])
                    ask += "`"+column_names[number]+"`" + ' LIKE' + ' %s'
            # SELECT * FROM `person` WHERE `surname` LIKE 'saad' AND `address` LIKE 'luminy'
            query = ("SELECT * FROM `person`"+ask)
           # query = ("SELECT * FROM `person` WHERE `surname` LIKE %s")
            print(query)
            insertion = person
            #test = ['saad']
            # print(type(test))
            self.cursor.execute(query, construction)
            row = self.cursor.fetchall()
            print(row)
            names_fetched = row
            # self.connection.commit()
            self.cursor.close()
            if len(names_fetched) > 0:
                return names_fetched
            else:
                return None
