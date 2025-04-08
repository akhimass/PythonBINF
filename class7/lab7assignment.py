#!/usr/bin/env python

import re

import re


codon_table = {
    "ATA": "I", "ATC": "I", "ATT": "I", "ATG": "M",
    "ACA": "T", "ACC": "T", "ACG": "T", "ACT": "T",
    "AAC": "N", "AAT": "N", "AAA": "K", "AAG": "K",
    "AGC": "S", "AGT": "S", "AGA": "R", "AGG": "R",
    "CTA": "L", "CTC": "L", "CTG": "L", "CTT": "L",
    "CCA": "P", "CCC": "P", "CCG": "P", "CCT": "P",
    "CAC": "H", "CAT": "H", "CAA": "Q", "CAG": "Q",
    "CGA": "R", "CGC": "R", "CGG": "R", "CGT": "R",
    "GTA": "V", "GTC": "V", "GTG": "V", "GTT": "V",
    "GCA": "A", "GCC": "A", "GCG": "A", "GCT": "A",
    "GAC": "D", "GAT": "D", "GAA": "E", "GAG": "E",
    "GGA": "G", "GGC": "G", "GGG": "G", "GGT": "G",
    "TCA": "S", "TCC": "S", "TCG": "S", "TCT": "S",
    "TTC": "F", "TTT": "F", "TTA": "L", "TTG": "L",
    "TAC": "Y", "TAT": "Y", "TAA": "*", "TAG": "*",
    "TGC": "C", "TGT": "C", "TGA": "*", "TGG": "W"
}


def reverse_complement(dna):
    complement_dict = {"A": "T", "T": "A", "C": "G", "G": "C"}
    reverse_comp = ""
    for nucleotide in dna:
        reverse_comp = complement_dict[nucleotide] + reverse_comp
    return reverse_comp

def translate_dna(dna):
    protein = ""
    for pos in range(0, len(dna) - 2, 3):
        codon = dna[pos:pos + 3]
        protein += codon_table.get(codon)
    return protein


def find_genes(dna, protein):
    genes = []
    pattern = re.finditer(r"M[^*]*\*", protein)

    for match in pattern:
        start = match.start()
        end = match.end()
        if (end - start) % 3 == 0:
            genes.append((dna[start * 3:end * 3], protein[start:end]))

    return genes


def read_fasta(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    dna_seq = ""
    for line in lines:
        if not line.startswith(">"):
            dna_seq += line.strip()
    return dna_seq


def main():
    dna_seq = read_fasta("lab7.fa")

    all_genes = []
    frames = []
    for shift in range(3):
        frame = ""
        for i in range(shift, len(dna_seq)):
            frame += dna_seq[i]
        frames.append(frame)
    reverse_dna = reverse_complement(dna_seq)

    for shift in range(3):
        frame = ""
        for i in range(shift, len(reverse_dna)):
            frame += reverse_dna[i]
        frames.append(frame)

    for frame in frames:
        protein_seq = translate_dna(frame)
        genes = find_genes(frame, protein_seq)
        all_genes.extend(genes)

    with open("seq.fa", "w") as output_file:
        index = 1
        for gene_dna, gene_protein in all_genes:
            output_file.write(">Gene" + str(index) + "\n" + gene_dna + "\n")
            output_file.write(">Protein" + str(index) + "\n" + gene_protein + "\n")
            index += 1

main()