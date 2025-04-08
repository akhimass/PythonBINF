#!/usr/bin/env python

#list colors create
colors = ["Red", "Green", "Blue", "Purple"]

#reverse list
colors.reverse()

#for loop to iterate through colors and print each
for color in colors:
    print(color)

#print fourth letter p from purple
for color in colors:
    if color == "Purple":
        print ("\nFourth letter in 'Purple': ", color[3])

#create variable x set equal to 0
x = 0

#while loop to print colors and increment to size of list minus 2
while x < len(colors) - 2:
    print(colors[x])
    x = x + 1


