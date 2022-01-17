# TP2 - INLO

## Introduction

This exercice was done in the context of a practical exercice around argument parsers on python. 

## Main goal
- Check the validity of the FASTA sequences available inside a .fasta file. 

## Secondary goals
- Indicate the length of the FASTA sequences for each sequence.  

- Indicate the position where a letter of the sequence is not a known nucleotide.
## Requirements
To run this script, python3 is needed to be installed along with the packages mentioned inside.  
The file adn.py needs to be on the same directory as the select_fasta_parser.py.
## Biological explanation
A FASTA sequence should always begin with a '>' indicating the sequence identifier of the nucleotid chain under it.  
The validation of a FASTA sequence is verified when the nucleotides belong to the known bases (A,T,C,G) without any anomalies in the annotation.

## Input
While running the script, the inputfile (-i) should have a .fasta folder as an argument also .txt files are accepted.

## Reading the file
Since the file can contain more than one sequence, it's important to split the sequences and analyze each one on its own.  
For the moment the accepted separators between the sequences are:  
- Tabulation (\t)
- Newline (\n)
- Backspace (\b)
## Output
For each sequence the line of the user should be able to identify the line of the sequence analyzed, the ID. 
After that, the output depends on the result of the script.  
- If the sequence is validated the script will notify the user and will also give the length of the sequence.  
- If not validated, the script will return the position where it found a problem along with the letter that caused it. Also the overall full length of the sequence will be displayed.

## Optional arguments
- (-n): Adds 'N' to the accepted nucleotids for the sequence analysis. To use when the the .fasta files are known to have N inside their annotations.
- (-o): Saves the results of the analysis into a .txt file.  *Results will not be printed in the console, the user will find them inside the output file*

## Author
George Alehandro Saad
