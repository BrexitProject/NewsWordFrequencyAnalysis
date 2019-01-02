# -*- coding:utf-8 -*-

import os
dirname = os.getcwd()
def getText():
    txt=open("abstract7.txt","r",encoding="utf-8").read()
    txt=txt.lower()
    for ch in '''!"@#$%^&*()+,-./:;<=>?@'[\\]_`~{|}''': #替换特殊字符
        txt=txt.replace(ch, ' ')
    return txt
ma=getText()
words = ma.replace('\n', ' ').split(" ")
counts={}
for i in range(len(words)):
    if words[i] == "free":
        jkl="free" + " " + words[i+1]+" "+words[i+2] + " " +words[i+3]
        counts[jkl] = counts.get(jkl,0) + 1
a=0
for j in counts.values():
    a+=j
items = list(counts.items())
items.sort(key= lambda x:x[1],reverse=True)

writefile = 'write1.txt'
wpath = os.path.join(dirname, writefile)
with open(wpath, 'w',encoding='utf-8') as f:
    f.write('Word' + '                ' + 'Fre/%')
    f.write('\n')
    for h in items:
        f.write(h[0]+'                ')
        f.write(str(h[1]/a*100))
        f.write('\n')
