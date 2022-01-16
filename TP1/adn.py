#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    adn.py is a library that contains 2 functions to prompt the user for a 
    chain of nucleotids and verify it. If verified, it will print it. If not,
    it will keep prompting.
"""

__author__ = 'George Alehandro Saad'


def is_valid(adn):
    nucleotides = ['a','t','c','g']
    adn = adn.lower().replace(' ','') #Unify format of letters, ignore spaces
    for i in range(0,len(adn)): #Iteration over all the letters of the chain
        if adn[i] not in nucleotides :
            return False
        else:
            continue
    if len(adn) > 0: #To refuse blank answers
        return True


def get_valid_adn(prompt='chaine : '):
    chaine = input(prompt)
    if is_valid(chaine) is True:
        print('La chaine ADN que vous avez inserez est: ',chaine)
        return chaine
    print('Try again!')
    return get_valid_adn(prompt='chaine : ')

