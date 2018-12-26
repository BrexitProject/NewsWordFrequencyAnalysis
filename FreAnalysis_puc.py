# -*- coding: utf-8 -*-
# coding=utf-8

import collections
import os
filename = 'abstract5.txt'
# 当前进程工作目录
dirname = os.getcwd()
fname = os.path.join(dirname, filename)
def geshi(a, b):
    return "{:<18}""{:>8}".format(a,b) + '\n'
# 读取文本文件，把所有的汉字拆成一个list
f = open("abstract5.txt", 'r', encoding='utf8')  # 打开文件，并读取要处理的大段文字
txt1 = f.read()
txt1 = txt1.replace('\n', '')  # 删掉换行符
txt1 = txt1.lower()
for ch in 'abcdefghijklmnopqrstuvwxyz1234567890,.':
    txt1 = txt1.replace(ch, '')
mylist = list(txt1)
mycount = collections.Counter(mylist)
results = []
for key, val in mycount.most_common():
    results.append((key, val))
sorted(results, key=lambda x: x[1], reverse=True)

writefile = 'write51.txt'
wpath = os.path.join(dirname, writefile)
with open(wpath, 'w',encoding='utf-8') as f:
    for h in results:
        f.write(h[0]+'                ')
        f.write(str(h[1]))
        f.write('\n')