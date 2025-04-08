#!/usr/bin/env python

import re

def process_fasta (input, output):
    with open ("input.fasta", "r") as inputfile, open ("output.fasta", "w") as outputfile:
        header, sequence = None, ""

        for line in inputfile:
            line = line.strip()
            if re.match(r">", line):
                if header and sequence:
                    check_conditions (header, sequence, outputfile)
                    header, sequence = line, ""
            else:
                sequence += line
        if header and sequence:
            check_conditions (header, sequence, outputfile)

def check_conditions (header, sequence, outputfile):
    if re.match(r"^ACAA", sequence):
        if len(sequence) > 20:
            outputfile.write(f"{header}\n{sequence}\n")
        elif re.search(r"TTTT$", sequence):
            print(f"{header}\n{sequence}\n")


process_fasta()
