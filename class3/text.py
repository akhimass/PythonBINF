#!/usr/bin/env python

my_file = open("output")
print(type(my_file))
file_contents = my_file.read()
print(file_contents)
print (file_contents.rstrip())
