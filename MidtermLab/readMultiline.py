#!/usr/bin/env python
seq = []
header = []
def readMultiline():
    with open ('dnaseqs.txt') as f:
        lines = f.readlines() #lines into list
        x=0 #counter for the line #
        tempSeq = "" #empty seq
        while x<len(lines)-1: #going to line before last
            line = lines[x].rstrip()
            if (line[0] == ">"):
                header.append(line)
                tempSeq = ""
                x+=1
            else:
                while (line[0]!=">" and x<len(lines)-1): #not a header not and EOF we cant push #past lenght list
                    tempSeq+=line
                    x+=1
                    line = lines[x].rstrip()
                    if (x == len(lines)-1): #im at second to last line
                        tempSeq += line
                seq.append(tempSeq)
    print (header, "\n")
    print (seq, "\n")

def readfile():
    with open("dnaseq.txt", "r") as file:
        lines = file.readlines()
        sequences = {}
        header = None
        for line in lines:
            line = line.rstrip()
            if line.startswith(">"):
                header = line[1:] #removing carrot
                sequences[header] = ""
            else:
                sequences[header] = line
