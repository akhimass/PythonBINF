#!/usr/bin/env python

#string creation and declaration
TrP1 = "CCTAGA"
print (TrP1)

#Length string operator
length = len(TrP1)
c_count = TrP1.count("C")
print (c_count)

#Replace string operator
RNA_Seq = TrP1.replace("T","U")
print (RNA_Seq)

#lowercase operator
lcRna = RNA_Seq.lower()
print (lcRna)

#indexing access
print (lcRna[3:5])

#user input
DNA_Seq = input("Enter DNA Sequence: ")

#adding strings together
print (RNA_Seq + lcRna + TrP1)



