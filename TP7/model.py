#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The model file for the MVC structure of the phonebook program.
"""
from __future__ import absolute_import
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
        if address is not None:
            self.address = address.title().lstrip().rstrip()
        if city is not None:
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
        self.connection = mysql.connector.connect(
            host=monServeur, user=monLogin, password=password, database="TP7")
        self.cursor = self.connection.cursor()
        # Creating the table if doesnt exist.
        query = ('''
              CREATE TABLE IF NOT EXISTS `person`  (
             `id` int NOT NULL AUTO_INCREMENT,
             `surname` varchar(100) NOT NULL,
             `name` varchar(100) NOT NULL,
             `telephone` varchar(100) NOT NULL,
             `address` varchar(100) NOT NULL,
             `city` varchar(100) NOT NULL,
             PRIMARY KEY (`id`)
            ) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT
            CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
              ''')
        self.cursor.execute(query)

    def insert_person(self, person):
        '''
        Person insertion inside Ensemble behavior and verification.
        '''
        # UPDATE `person` SET `name` = 'New' WHERE `person`.`ID` = 1;

        if isinstance(person, Person):
            if not hasattr(person, 'surname') or not hasattr(person, 'name'):
                return None
            person_info = person.get_surname().title(), person.get_prenom(
            ).title(), person.telephone, person.address, person.city, person.idi
            if person.idi is not None:
                query = ("Select `ID` from `person`;")
                self.cursor.execute(query)
                for idi in self.cursor.fetchall():
                    if int(person.idi) == idi[0]:  # Match on id:
                        query_2 = (
                            '''UPDATE `person` SET `surname` = %s, `name` = %s,
                            `telephone` = %s, `address` = %s, `city` = %s
                            WHERE `person`.`ID` = %s;''')
                        update = person_info
                        self.cursor.execute(query_2, update)
                        self.connection.commit()
                        return "Modified"
                else:
                    query = (
                        '''INSERT INTO `person` (`ID`, `surname`, `name`,
                        `telephone`, `address`, `city`) VALUES
                    (%s, %s, %s, %s, %s, %s);''')
                    insertion = person.idi, person.get_surname().title(), person.get_prenom(
                    ).title(), person.telephone, person.address, person.city
                    self.cursor.execute(query, insertion)
                    self.connection.commit()
                    return "Inserted"
            else:
                query = (
                    "INSERT INTO `person` (`ID`, `surname`, `name`, `telephone`, `address`, `city`) VALUES (NULL, %s, %s, %s, %s, %s);")
                insertion = person_info[:-1]
                self.cursor.execute(query, insertion)
                self.connection.commit()
               # self.cursor.close()
                return "Inserted"
        return None

    def delete_person(self, person):
        '''
        Person removal from an Ensemble.
        '''
        if isinstance(person, Person):
            print(person.idi)
            if person.idi is None:
                return False
            query = ("DELETE FROM `person` WHERE `person`.`ID` = %s")
            number = [str(person.idi)]
            print(number)
            query_2 = ("Select `ID` from `person`;")
            self.cursor.execute(query_2)
            for idi in self.cursor.fetchall():
                if int(''.join(number)) == idi[0]:
                    self.cursor.execute(query, number)
                    self.connection.commit()
                    return number
            else:
                return None

    def display_all(self):
        '''
        Shows the content of the ensemble.
        '''
        query = ("select * from person")
        self.cursor.execute(query)
        all_names = self.cursor.fetchall()
        return(all_names)

    def reset_id(self):

        query = (
            'ALTER TABLE `person` DROP id;ALTER TABLE  `person` ADD `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST')
        self.cursor.execute(query)
        self.connection = mysql.connector.connect(
            host=monServeur, user=monLogin, password=password, database="TP7")
        self.cursor = self.connection.cursor()
        return 'Reset done, connection restablished.'

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
                    fetch[number] = fetch[number] + '%'
                    construction.append(fetch[number])
                    ask += "`"+column_names[number]+"`" + ' LIKE' + ' %s'
            query = ("SELECT * FROM `person`"+ask)
            print(query)
            insertion = person
            self.cursor.execute(query, construction)
            row = self.cursor.fetchall()
            print(row)
            names_fetched = row
            if len(names_fetched) > 0:
                return names_fetched
            else:
                return None
