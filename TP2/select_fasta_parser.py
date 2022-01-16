#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A python script integrated in command-line program to test the sequences from
a fasta file.
"""

from __future__ import absolute_import
import argparse
import sys
from adn import is_valid, accept_N


def create_parser():
    """ Declares new parser and adds parser arguments """
    program_description = ''' reading fasta file and checking sequence
    format '''
    parser = argparse.ArgumentParser(
        add_help=True, description=program_description)
    parser.add_argument('-i', '--inputfile', default=sys.stdin,
                        help="required input file in fasta format",
                        type=argparse.FileType("r"), required=True)
    parser.add_argument('-n', '--accept_N',
                        action='store_true')
    return parser


def main():
    """ Main function for reading fasta file and checking sequence format """
    parser = create_parser()
    args = parser.parse_args()
    args = args.__dict__
    print(args)
    # print(args["inputfile"])
    fasta_sequence = args["inputfile"].read()
    print(type(fasta_sequence.split()))
    fasta_sequence_list = fasta_sequence.split()
    if args["accept_N"]:  # Choice of functions to use based on accept_N arg
        function_choice = accept_N
    else:
        function_choice = is_valid
    for index, line in enumerate(fasta_sequence_list):
        if line.startswith('>'):
            print(index, line)
            seq = ''
            for i in range(index+1, len(fasta_sequence_list)):
                if fasta_sequence_list[i].startswith('>'):
                    print(seq, function_choice(seq))  # Result the old sequence
                    seq = ''  # Reinitiates a new sequence
                    break
                # Concatenates two sequences
                seq += fasta_sequence_list[i].strip()
                if i == len(fasta_sequence_list)-1:  # End of text, last print
                    print(seq, function_choice(seq))


if __name__ == "__main__":
    main()
