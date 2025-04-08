#!/usr/bin/env python
import re

#read pU19c sequence
with open("sequence.fasta", "r") as f:
    lines = f.readlines()
    puc19c_seq = "".join(line.strip() for line in lines[1:])

#apply SmaI restriction enzyme cut site: CCCGGG
cut_sites = list(re.finditer("CCCGGG", puc19c_seq))
start_index = cut_sites[0].start()
end_index = cut_sites[0].end()
#read insert sequence
with open("insert.fasta", "r") as file:
    insert_seq = "".join(line.rstrip() for line in file.readlines()[1:]).lower()

#insert new sequence at restriction site
modified_sequence =  puc19c_seq[:start_index] + insert_seq + puc19c_seq[end_index:]

#write output to output2.txt
with open("output2.txt", "w") as file:
    file.write(">pUC19c SmaI insert.fasta\n")
    file.write(modified_sequence + "\n")