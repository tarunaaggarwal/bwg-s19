#!/usr/bin/python3
# A program for removing end line characters from sequences so that the DNA strings shows up as a single line
# USAGE: python removing_endline_character_in_seqs_TAS.py input_file output_file
# Author: Taruna Schuelke
# Affiliation: University of California, Santa Barbara, USA
# Date: 01May2019

import argparse

# set up your command line arguments
parser = argparse.ArgumentParser(description="This script calculates the GC content in a fasta file.")
parser.add_argument('--input', help="PATH to the directory with input files.", required=True)
parser.add_argument('--output', help="PATH to the directory with output files.", required=True)
args = parser.parse_args()

# set up our files
inFile = open(args.input, "r") # r is for read file
outFile = open(args.output, "w") # w is for write file

flag = False
for currentLine in inFile:
    currentLine = currentLine.rstrip()
    if currentLine.startswith(">"):
        flag = False
        outFile.write("{0}{1}".format(currentLine, "\n"))
        flag = True
    else:
        if flag:
            currentLine = currentLine.replace("\n", "")
            outFile.write("{0}".format(currentLine))

inFile.close()
outFile.close()
