# -*- coding:utf-8 -*-
import os

# root_dir为要读取文件的根目录
root_dir = r"D:\spider_news\thesun"
# 读取批量文件后要写入的文件
with open("abstract5.txt", "w",encoding='utf-8') as abstract5:

    # 依次读取根目录下的每一个文件
    for file in os.listdir(root_dir):
        file_name = root_dir + "\\" + file
        filein = open(file_name, "r",encoding='UTF-8')
        # 按行读取每个文件中的内容
        for line in filein:
            abstract5.write(line.rstrip("\n"))
        abstract5.write("\n")
        filein.close()
