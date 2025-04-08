#!/usr/bin/env python

#read pU19c sequence
with open("sequence.fasta", "r") as f:
    lines = f.readlines()
    puc19c_seq = "".join(line.strip() for line in lines[1:])

#apply SmaI restriction enzyme cut site: CCCGGG
cut_sites = puc19c_seq.split("CCCGGG")

#read insert sequence
with open("insert.fasta", "r") as file:
    insert_seq = "".join(line.rstrip() for line in file.readlines()[1:]).lower()

#insert new sequence at restriction site
modified_sequence = cut_sites[0] + "CCCGGG" + insert_seq + "CCCGGG" + cut_sites[1]

#write output to output2.txt
with open("output2.txt", "w") as file:
    file.write(">pUC19c SmaI insert.fasta\n")
    file.write(modified_sequence + "\n")