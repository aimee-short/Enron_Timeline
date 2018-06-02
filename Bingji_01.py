# -*- encoding: utf-8 -*-
import os
import csv
import xlrd
import xlwt
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

f = open(r"E:\enron\week\week_heng_wuhang.txt","r")
w = open(r"E:\enron\week\week_jishu.txt","w")
line = f.readline()
week_list = []
a = []
j = 1
i = 0
while line:
    week_list.append(list(map(int,line.split(','))))
    for i in week_list:
            if week_list.count(i)>1:
                a[i] = week_list.count(i)
    print(a)
    w.write('%d\n'%j)
    w.write(a)
    w.write('\n')
    j += 1
