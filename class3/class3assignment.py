#!/usr/bin/env python

#assigning sequence to variable
DNASeq = "TACGACACAAAAGTAACCTAGATAACGATA"

#printing the DNA sequence and its length
print(DNASeq)
print(len(DNASeq))

#assigning first 10 letters to variable
UTR = DNASeq[0:10]
print(UTR)

#assigning last 20 letters to variable
GENE = DNASeq[10:30]
print(GENE)

#counting and printing C characters
c_count = UTR.count("C")
print (c_count)

#counting and printing T characters
t_count = GENE.count("T")
print (t_count)

#replacing T with U to create trGene sequence
trGene = DNASeq.replace("T","U")
print (UTR, trGene)

#finding position of AUA codon and printing position
AUApos = trGene.find("AUA")
print ("The position of AUA is:", AUApos)

#Replacing AUA with UAG to
FinalSeq = trGene.replace("AUA", "UAG")
print (FinalSeq)
