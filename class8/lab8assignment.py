#usr/bin/env python
def burrow_wheeler_transform(s):
    s = s + "$"
    rotations = []
    for i in range(len(s)):
        rotations.append(s[i:] + s[:i])

    for i in range(len(rotations)):
        for j in range(len(rotations)-1):
            if rotations[j] > rotations[j+1]:
                rotations[j], rotations[j+1] = rotations[j+1], rotations[j]
    bwt = ""
    for i in rotations:
        bwt += i[-1]
    return bwt

def reverse_burrow_wheeler_transform(s):
    table = [""] * len(s)
    for i in range(len(s)):
        table = [s[i] + table[i] for i in range (len(s))]
        for j in range(len(table) -1):
            for k in range(len(table) - 1 - j):
                if table[k] > table[k+1]:
                    table[k], table[k+1] = table[k+1], table[k]
    for i in table:
        if i.endswith("$"):
            return i[:-1]

original = "banana"
bwt_result = burrow_wheeler_transform(original)
print(bwt_result)
reverse_bwt_result = reverse_burrow_wheeler_transform(bwt_result)
print(reverse_bwt_result)

word = "banana"
wordlist = []
print (wordlist)
for x in range(1, len(wordlist)):
    end = word
    end = end[-x:]
    start = word[:-x]
    wordlist.append(end+start)
print(wordlist)
