#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A python script integrated in command-line program to test the sequences from
a fasta file.
"""
from __future__ import absolute_import
import argparse
import sys
from adn import is_valid, accept_n


def create_parser():
    """ Declares new parser and adds parser arguments
    Two group of parsers: Optional and required"""
    program_description = ''' reading fasta file and checking sequence
    format '''
    parser = argparse.ArgumentParser(
        add_help=True, description=program_description)
    requiredarg = parser.add_argument_group('required named arguments')
    requiredarg.add_argument('-i', '--inputfile', default=sys.stdin,
                             help="required input file in fasta format",
                             type=argparse.FileType("r"), required=True)
    parser.add_argument('-o', '--outputfile', default=sys.stdout,
                        help="optional output file containing the results",
                        type=argparse.FileType("w"), required=False)
    parser.add_argument('-l', '--length', help="""optional argument to be
                        added if you want the program to give you the length
                        of the sequence""",
                        action='store_true')
    parser.add_argument('-n', '--accept_n', help="""optional argument to be
                        added if you expect to have 'N' inside
                        your sequences""",
                        action='store_true')
    return parser


def run(args):
    """ Takes args from main and behaves accordingly
    Fetching the file from top to bottom while testing the validity of the
    sequences in between. Also makes up the choices for the function used for
    analyzing the sequences and displaying the results"""
    fasta = args.inputfile.read()
    output = args.outputfile  # Specifiying the output in case of user entry
    fasta_list = fasta.split()  # fasta sequence will be stored in a list
    if args.accept_n:  # Analyzing functions based on accept_n arg
        analyze_function = accept_n
    else:
        analyze_function = is_valid
    if args.outputfile is None:  # Results display based on output arg
        display = print
    else:
        display = output.write
    for index, line in enumerate(fasta_list):
        if line.startswith('>'):
            display('Reading sequence in line: '+str(index+1) +
                    '\t'+'sequence id: '+line+'\n'*2)
            seq = ''  # Initializing an empty string that stores the sequences
            for i in range(index+1, len(fasta_list)):
                if not fasta_list[i].startswith('>'):
                    seq += fasta_list[i].strip()  # Concatenates two sequences

                if fasta_list[i].startswith('>') or i == len(fasta_list)-1:
                    # Retrive values from functions of adn.py file
                    verdict, result, *error = analyze_function(seq)
                    if verdict:
                        display('This sequence is verified!' +
                                '\n')
                    elif len(seq) == 0:
                        display('Empty sequence.'+'\n')
                    else:
                        display('This sequence is not verified.' +
                                '\n' +
                                'Problem of annotation found at position: ' +
                                str(result+1) + '\n' + 'The script found a ' +
                                str(error) + '\n')
                    if args.length:  # If the user specified the -l parameter
                        display('The length of the sequence is: ' +
                                str(len(seq))+'\n')
                    display('\n---------------------------------------\n')
                    break


def main():
    """ Main function to run through the arguments and sending them into
    the run function above"""
    parser = create_parser()
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
