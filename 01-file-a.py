# -*- coding: UTF-8 -*-

# Filename :
# author by : （学员ID)

# 目的:


import os
# -------------------------------
# 写文件
filename = "test.txt"
f = open(filename, 'w')  # write 方式第一次写一行

text2write = "该文本会写入到文件中，看到我了吧！\n"
f.write(text2write)

text2write = "再写一行，又看到我了吧！\n"
f.write(text2write)

f.close()
