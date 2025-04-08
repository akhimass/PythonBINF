#!/usr/bin/env python

#function to import
def aaCount(sequence):
    #replace Ls with l lowercase
    sequence = sequence.replace("L", "l")
    #counts of each letter
    count_m = sequence.count("M")
    count_r = sequence.count("R")
    count_y = sequence.count("Y")
    count_l = sequence.count("l")
    #total length and calculating percentage of sequence that consists of 4 aa
    total_length = len(sequence)
    aa_percentage = (count_m + count_r + count_y + count_l) / float(total_length)
    return sequence, count_m, count_r, count_y, count_l, aa_percentage

