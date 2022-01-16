#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    adn.py is a library that contains 2 functions to prompt the user for a 
    chain of nucleotids and verify it. If verified, it will print it. If not,
    it will keep prompting.
"""

__author__ = 'George Alehandro Saad'

nucleotides = ['a', 't', 'c', 'g']


def purify(adn):
    adn = adn.lower().replace(' ', '')  # Unify format of letters, ignore spaces
    for nuc in adn:
        if nuc not in nucleotides:
            adn = adn.replace(nuc, '')
    return adn


def accept_N(adn):
    bases_inclu_n = nucleotides.append('n')
    return(is_valid(adn, bases_inclu_n))


def is_valid(adn, bases=nucleotides):
    adn = adn.lower()  # Unify format of letters, ignore spaces
    for i in range(0, len(adn)):  # Iteration over all the letters of the chain
        if adn[i] not in nucleotides or len(adn) == 0:
            return False, i, adn[i]
        else:
            continue
    # print("Longueur de la sequence est: ", len(adn))
    return True, len(adn)


def get_valid_adn(prompt='chaine : '):
    chaine = input(prompt)
    while not is_valid(chaine):
        print('Try again!')
        return(get_valid_adn(prompt='chaine : '))
    else:
        print('La chaine ADN que vous avez inserez est: ', chaine)
        return chaine
