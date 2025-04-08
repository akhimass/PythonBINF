#!/usr/bin/env python

#calculate AT content of given DNA sequence
def atContent(sequence, sig_figs = 2):
    length = len(sequence)
    a_count = sequence.count('A')
    t_count = sequence.count('T')
    at_content = (a_count + t_count) / length
    return round(at_content, sig_figs)

#read fasta file
def readfastafile():
    with open("dna.fasta", "r") as file:
        lines = file.readlines()

        sequences = {}
        header = None

        for line in lines:
            line = line.rstrip()
            if line.startswith(">"):
                header = line[1:] #removing carrot
                sequences[header] = ""
            else:
                sequences[header] = line

        #loop coded with chatgpt to print correct output as specified in assignment
        for idx, (header, sequence) in enumerate(sequences.items(), start = 1):
            print(f"{idx} - {atContent(sequence)}")

