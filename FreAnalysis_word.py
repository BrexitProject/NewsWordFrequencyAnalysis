# _*_ coding: utf-8 _*_
import os
from collections import Counter
# 假设要读取文件名为read，位于当前路径
filename = 'abstract5.txt'
# 当前进程工作目录
dirname = os.getcwd()
fname = os.path.join(dirname, filename)
with open(fname,encoding='utf-8') as f:
    s = f.read()
    s = s.lower()
    for ch in '''!"@#$%^&*()+,-./:;<=>?@'[\\]_`~{|}''': #替换特殊字符
        s=s.replace(ch, ' ')
counter = Counter(s.replace('\n', ' ').split(' '))
# 格式化要输出的每行数据，尾占8位，首占18位
def geshi(a, b):
    return "{:<18}""{:>8}".format(a,b) + '\n'
title = geshi('词', '频率')
results = []
# 要输出的数据，每一行由：词、频率+'\n'构成，序号=List.index(element)+1
for w, c in counter.most_common(300):
    results.append((w, c))
sorted(results, key=lambda x: x[1], reverse=True)
# 将统计结果写入文件write.txt中
writefile = 'write1.txt'
wpath = os.path.join(dirname, writefile)
with open(wpath, 'w',encoding='utf-8') as f:
    for h in results:
        f.write(h[0]+'                ')
        f.write(str(h[1]))
        f.write('\n')