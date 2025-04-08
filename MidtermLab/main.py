#!/usr/bin/env python
import re
from gc_content import gcContent
from dnatorna import dna_to_rna
from dna_aa import translate_dna
from dna_aa import translate_dna

with open('dnaseqs.txt') as f:
    seq = []
    header = []
    lines = f.readlines()  # lines into list
    x = 0  # counter for the line #
    tempSeq = ""  # empty seq
    while x < len(lines):  # going to line before last
        line = lines[x].rstrip()
        if (line[0] == ">"):
            if tempSeq:
                seq.append(tempSeq)
            header.append(line)
            tempSeq = ""
        else:
            tempSeq += line

        x += 1
    if tempSeq:
        seq.append(tempSeq)

combined = ""
with open('midtermoutput.txt', 'w') as f:
    for i in range(len(header)):
        current_sequence = seq[i]
        f.write(header[i] + "\n")

        f.write(str(gcContent(current_sequence)) + "\n")
        rna_sequence = dna_to_rna(current_sequence)
        f.write(rna_sequence + "\n")

        a4find = re.findall(r"A{4,}", current_sequence)
        tfind = re.findall(r"TTT.", current_sequence)
        f.write(str(a4find) +"\n")
        f.write(str(tfind) + "\n")


        combined += ''.join(a4find) + ''.join(tfind)


print(combined)
translated_protein = translate_dna(combined)
print(translated_protein)















