# _*_ coding: utf-8 _*_
import os
from collections import Counter
# 假设要读取文件名为read，位于当前路径
filename = 'martinwolf.txt'
# 当前进程工作目录
dirname = os.getcwd()
fname = os.path.join(dirname, filename)
with open(fname,encoding='utf-8') as f:
    s = f.read()
    s = s.lower()
    for ch in '''!"@#$%^&*()+,-./:;<=>?@'[\\]_`~{|}''': #替换特殊字符
        s=s.replace(ch, ' ')
counter = Counter(s.replace('\n', ' ').split(' '))

#替换停用词
file = open('stopwords.txt','r',encoding='utf-8')
for line in file.readlines():
    curLine=line.strip().split(" ")

results = []
a=0
for w, c in counter.most_common():
    if w != '' and w != '   ' and w != ' -':
        a+=c
for w, c in counter.most_common():
    if w != ''and w != '   ' and w not in curLine:
        results.append((w, c/a*1000))
sorted(results, key=lambda x: x[1], reverse=True)
# 将统计结果写入文件write.txt中
writefile = 'write1.txt'
wpath = os.path.join(dirname, writefile)
with open(wpath, 'w',encoding='utf-8') as f:
    f.write('Word' + '                ' + 'Fre/‰')
    f.write('\n')
    for h in results:
        f.write(h[0]+'                ')
        f.write(str(h[1]))
        f.write('\n')
