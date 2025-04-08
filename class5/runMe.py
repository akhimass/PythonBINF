#!/usr/bin/env python

from countAA import aaCount

#reads amino acid sequence from file and prints application of countAA
def main():
    input_file = "aaInput.faa"

    with open(input_file) as file:
        sequence = "".join([line.rstrip() for line in file][1:])

        modified_sequence, count_m, count_r, count_y, count_l, percentage = aaCount(sequence)

        print("Modified sequence:", modified_sequence)
        print(f"Count of M: {count_m}")
        print(f"Count of R: {count_r}")
        print(f"Count of Y: {count_y}")
        print(f"Count of l: {count_l}")
        print(f"Percentage: {percentage}")

main()