#!/usr/bin/env python

import re

def main():
    filename = "lab6input"

    with open(filename, "r") as file:
        ascension_names = file.read().rstrip().split(", ")
        for name in ascension_names:
            searchFunc(name)

def searchFunc(name):
    if re.search(r"5", name):
        print("Contains the number 5:", name)
    if re.search(r"[de]", name):
        print("\nContains the letter d or e:", name)
    if re.search(r"de", name):
        print("\nContains the letters d and e in exactly order(de):", name)
    if re.search(r"d[a-z]e",name):
         print("\nContains the letters d and e with a single letter between:", name)
    if re.search(r"de|ed", name):
        print("\nContains the letters d and e in any order(ed or de):", name)
    if re.search(r"^[xy]", name):
        print("\nStarts with x or y (removing x or y):", name[1:])
    if re.search(r"^[xy].*e$", name):
        print("\nStarts with x or y and ends with e (removing x or y: ", name[1:])
    if re.search(r"^x.{3}\d", name):
        print("\nStarts with x followed by any three characters then any number:", name)
    if re.search(r"\d{3,}", name):
        print("\nContains three or more numbers in a row:", name)
    if re.search(r"d[arp]$", name):
        if re.search(r"da$", name):
            print("\nEnds with d followed by a,r, or p and removed 'da' if matched:", name[:-2])
        else:
            print("Ends with d followed by a,r,p",name)
    if re.search(r"yy?", name):
        print("\nContains the letter y followed by exactly zero or one y's:", name)

main()