#!/usr/bin/env python

#fileName to variable and opening file
fh = open("dna.txt")
#read the contents of file and strip new line
#assigning text to read text
readText = fh.read().rstrip("\n")
#close file
fh.close()
print(readText)

#open file for writing and assign to x
x = open("output2.txt", "w")
#write contents of readText into putput2.txt
x.write(readText)
#close file object x
x.close()

#open file for reading and assign to x
with open('output2.txt', 'r') as f:
    #read file to content and strip last nucleotide
    content = f.read().rstrip("A\n")
    #convert text to lowercase and print with newline to standard output
    print (content.lower() + "\n")
quit()












