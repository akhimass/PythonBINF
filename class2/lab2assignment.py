#!/usr/bin/env python

#input for two sequences
hemoglobin = input("Enter the first DNA sequence: ")
hemoglobin_sicklecell = input("Enter the second DNA sequence: ")

#converting to RNA
RNA_hemoglobin = hemoglobin.replace("T","U")
RNA_hemoglobin_sicklecell = hemoglobin_sicklecell.replace("T","U")

#converting to lower case
lcRNA_hemoglobin = RNA_hemoglobin.lower()
lcRNA_hemoglobin_sicklecell = RNA_hemoglobin_sicklecell.lower()

totalSequence = lcRNA_hemoglobin + lcRNA_hemoglobin_sicklecell
print (totalSequence)






