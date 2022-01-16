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
    parser.add_argument('-o', '--outputfile',
                        help="optional output file containing the results",
                        type=argparse.FileType("w"), required=False)
    parser.add_argument('-n', '--accept_N', help="""optional argument to be
                        added if you expect to have 'N' inside
                        your sequences""",
                        action='store_true')
    return parser


def run(args):
    """ Takes args from main and behaves accordingly"""
    fasta = args.inputfile.read()
    output = args.outputfile
    fasta_list = fasta.split()
    if args.accept_N:  # Analyzing functions based on accept_N arg
        analyze_function = accept_N
    else:
        analyze_function = is_valid
    if args.outputfile is None:  # Results display based on output arg
        display = print
    else:
        display = output.write
    for index, line in enumerate(fasta_list):
        if line.startswith('>'):
            display('Reading sequence in line: '+str(index+1) +
                    '\t'+'sequence id: '+line)
            seq = ''
            for i in range(index+1, len(fasta_list)):
                if fasta_list[i].startswith('>') or i == len(fasta_list)-1:
                    # Retrive values from functions of adn.py file
                    verdict, result, *error = analyze_function(seq)
                    if verdict:
                        display('The length of the sequence is: ' +
                                str(result)+'\n'+'This sequence is verified!' +
                                '\n')
                    else:
                        display('Problem of annotation found at position: ' +
                                str(result) + '\n' + 'The script found a ' +
                                str(error) + '\n' +
                                'However, the length of the sequence is: '
                                + str(len(seq)) + '\n')
                    break
                else:
                    # Concatenates two sequences
                    seq += fasta_list[i].strip()


def main():
    """ Main function for reading fasta file and checking sequence format """
    parser = create_parser()
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
