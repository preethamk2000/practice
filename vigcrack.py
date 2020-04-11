import os
from itertools import product
from string import ascii_lowercase,ascii_letters,ascii_uppercase

keywords = [''.join(i) for i in product(ascii_uppercase, repeat = 3)]
# keywords = ['NOT']
ans = []

# print(ord(keywords[34][2])-65)

a = 'Js tes ynzevbz osavbw. Js znjx gvx NW ihfibgx. Jwmu bh tcty wm jol wilg sqvgmvbz.Ysm hg abdx vh wbsl acm swgq havg drm.'
# a = ''.join( c for c in a if  c not in '}{_. ' )

for key in keywords:
    i = -1
    new = ""
    for letter in a:
        if letter.isalpha():
            i = i + 1
            if ord(letter) <= 90:
                newchar = chr(((ord(letter)-65) - (ord(key[i%3])-65))%26 + 65)
            else:
                newchar = chr(((ord(letter)-97) - (ord(key[i%3])-65))%26 + 97)
        else:
            newchar = letter
        new = new + newchar
    # print(new)
    retval = os.system('cat /usr/share/dict/american-english | grep -iw "'+two+'"')
    if retval == 0:
        ans.append(new)
        ans.append(key)

for i in ans:
    print(i)
