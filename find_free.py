# -*- coding:utf-8 -*-
import os
dirname = os.getcwd()
f = open('martinwolf.txt','r',encoding='utf-8')
lines = f.readlines()
for i in lines:
    i=i.lower()
writefile = 'write2.txt'
wpath = os.path.join(dirname, writefile)
c=open(wpath, 'w',encoding='utf-8')
for line in lines:
   if "free" in line:
       c.write(line)
       c.write('\n')
