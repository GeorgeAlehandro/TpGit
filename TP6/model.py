#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os.path
import pickle
import inspect


class Person:
    def __init__(self, nom, prenom, telephone=None, adresse=None, ville=None):
        self.set_nom(nom)
        self.set_prenom(prenom)
        self.telephone = telephone
        self.adresse = adresse
        self.ville = ville
       # self.id =

    def set_nom(self, nom):
        if isinstance(nom, str) and all(x.isalpha() or x.isspace() for x in nom) and len(nom) > 0:
            self.nom = nom

    def get_nom(self):
        return self.nom

    def set_prenom(self, prenom):
        if isinstance(prenom, str) and all(x.isalpha() or x.isspace() for x in prenom) and len(prenom) > 0:
            self.prenom = prenom

    def get_prenom(self):
        return self.prenom

    def get_telephone(self):
        if self.telephone is not None:
            return self.telephone

    def get_adresse(self):
        if self.adresse is not None:
            return self.adresse

    def get_ville(self):
        if self.ville is not None:
            return self.ville


class Ensemble:
    def __init__(self):
        if os.path.isfile('output_new.pickle'):
            infile = open('output_new.pickle', 'rb')
            self.list_person = pickle.load(infile)
            infile.close()
            print('Save file found.')
        else:
            self.list_person = {}

    def insert_person(self, person):
        if isinstance(person, Person):
            person.set_nom(person.get_nom().capitalize())
            person.set_prenom(person.get_prenom().capitalize())
            list_attributs = {}
            prenom = person.prenom
            nom = person.nom
            list_attributs['name'] = nom
            list_attributs['prenom'] = prenom
            if person.telephone is not None:
                list_attributs['telephone'] = person.get_telephone()
            if person.adresse is not None:
                list_attributs['adresse'] = person.get_adresse()
            if person.ville is not None:
                list_attributs['ville'] = person.get_ville()
            self.list_person[f"{prenom} {nom}"] = list_attributs
            return "Inserted"
        return None

    def deleteperson(self, category, name):
        if isinstance(category, str):
            values_to_del = []
            for identification, information in self.list_person.items():
                try:
                    if name in information[category]:
                        values_to_del.append(identification)
                except KeyError:
                    next
            for to_del in values_to_del:
                del self.list_person[to_del]
            return('Deleted: '+''.join(values_to_del))

    def delete_person(self, person):
        if isinstance(person, tuple):
            names_fetched = []
            name_searched = person[0].capitalize()
            prenom_searched = person[1].capitalize()
           # if tel_searched
            for identification, information in self.list_person.items():
                try:
                    if name_searched in information['name'] and prenom_searched in information['prenom']:
                        names_fetched.append(identification)
                except KeyError:
                    next
            if len(names_fetched) > 0:
                for name in names_fetched:
                    del self.list_person[name]
                    return 'Deleted'
            else:
                return None

    def display_all(self):
        content_display = []
        for key, value in self.list_person.items():
            content_display.append(value)
        return content_display

    # def search_person(self, category, name):
    #     names_fetched = []
    #     for identification, information in self.list_person.items():
    #         try:
    #             if name in information[category]:
    #                 names_fetched.append(information)
    #         except KeyError:
    #             next
    #     if len(names_fetched) > 0:
    #         return names_fetched
    #     else:
    #         return None

    def search_person(self, person):
        if isinstance(person, tuple):
            names_fetched = []
            name_searched = person[0].capitalize()
            prenom_searched = person[1].capitalize()
            tel_searched = person[2]
            adresse_searched = person[3]
            ville_searched = person[4]
           # if tel_searched
            for identification, information in self.list_person.items():
                try:
                    if name_searched in information['name'] and prenom_searched in information['prenom']:
                        names_fetched.append(information)
                        if tel_searched != '':
                            for fetched in names_fetched:
                                if tel_searched not in fetched['telephone']:
                                    names_fetched.remove(fetched)
                        if adresse_searched != '':
                            for fetched in names_fetched:
                                if adresse_searched not in fetched['adresse']:
                                    names_fetched.remove(fetched)
                        if ville_searched != '':
                            for fetched in names_fetched:
                                if tel_searched not in fetched['ville']:
                                    names_fetched.remove(fetched)

                except KeyError:
                    next
            if len(names_fetched) > 0:
                return names_fetched
            else:
                return None

    def intersection(self, list1, list2):
        list3 = [value for value in list1 if value in list2]
        return list3

    def save(self):
        file_to_write = open("output_new.pickle", "wb")
        pickle.dump(self.list_person, file_to_write)
        file_to_write.close()

    def __str__(self):
        return str(self.list_person)
