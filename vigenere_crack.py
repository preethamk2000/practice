# Vigenere Cipher Basics (and if you need to use this with cuda-with numba you need to optimize and simplify the loops)

import os
from itertools import product
from string import ascii_uppercase

keylen = 3
keywords = [''.join(i) for i in product(ascii_uppercase, repeat = keylen)]

ans = []

a = 'Js tes ynzevbz osavbw. Js znjx gvx NW ihfibgx. Jwmu bh tcty wm jol wilg sqvgmvbz.Ysm hg abdx vh wbsl acm swgq havg drm.'

for key in keywords:
    i = -1
    new = ""
    for letter in a:
        if letter.isalpha():
            i = i + 1
            if ord(letter) <= 90:
                newchar = chr(((ord(letter)-65) - (ord(key[i%keylen])-65))%26 + 65)
            else:
                newchar = chr(((ord(letter)-97) - (ord(key[i%keylen])-65))%26 + 97)
        else:
            newchar = letter
        new = new + newchar
    # print(new) debug your reverser
    retval = os.system('cat /usr/share/dict/american-english | grep -iw "'+two+'"')
    if retval == 0:
        ans.append(new)
        ans.append(key)

for i in ans:
    print(i)
