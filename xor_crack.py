import os
from itertools import product
from string import ascii_lowercase

keywords = [''.join(i) for i in product(ascii_lowercase, repeat = 4)]
ans = []
a = "51 38 91 81 28 14 7 4 56 14 27 62 29 4 27 14 56 3 28 21 56 15 6 21 56 3 6 21 15 28"

a = a.split(" ")

for key in keywords:
    i = -1
    new = ""
    for letter in a:   
        i = i + 1
        newchar = chr(int(letter) ^ ord(key[i%4]))
        new = new + newchar
    # print(new) debug for rev
    if new.find("TG20",0,len(a)-1) != -1:
        ans.append(new)

for i in ans:
    print(i)
    print()
