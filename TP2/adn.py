#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    adn.py is a library that contains functions to prompt the user for a
    chain of nucleotids and verify it. If verified, it will print it. If not,
    it will keep prompting.
"""

__author__ = 'George Alehandro Saad'

nucleotides = ['a', 't', 'c', 'g']


def purify(adn):
    """
        Used to clear all the anomalies in annotation
    """
    adn = adn.lower().replace(' ', '')  # Unify format of letters, ignore space
    for nuc in adn:
        if nuc not in nucleotides:
            adn = adn.replace(nuc, '')
    return adn


def accept_n(adn):
    """
        Function indicating that the user will accept having 'N' inside his
        ADN sequences
    """
    bases_inclu_n = nucleotides.append('n')
    return is_valid(adn, bases_inclu_n)


def is_valid(adn, bases=nucleotides):
    """
    Main function used to validate or not a given DNA sequence.
    The parameter bases is optional allowing a user-entry identification
    depending on the nature of the analysis

    """
    adn = adn.lower()  # Unify format of letters, ignore spaces
    if len(adn) == 0:
        return False, 0
    for i, nuc in enumerate(adn):  # Iteration over all letters of the chain
        if nuc not in nucleotides or len(adn) == 0:
            return False, i, nuc
    return True, len(adn)


def get_valid_adn(prompt='chaine : '):
    """
    User prompt for a DNA sequence, until validated. Will return the validated
    sequence

    """
    chaine = input(prompt)
    while not is_valid(chaine):
        print('Try again!')
        return get_valid_adn(prompt='chaine : ')
    print('The inserted chain is: ', chaine)
    return chaine
