# -*- encoding: utf-8 -*-
import os
import csv
import xlrd
import xlwt
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

lis = []
csv_reader = csv.reader(open('E:\enron\edge_00.csv','rb'))
f = open('week_16.txt','w') #直接打开一个文件，如果文件不存在则创建文件

j = 1
a = {}
for row in csv_reader:
    if row:
        if row[5] == str(j):
            lis.append(row[0])
            lis.append(row[1])
        else:
            #f.write('%d\n'%j)
            ids = list(set(lis))
            '''
            for i in lis: #写入全部数据
                f.write(i)
                f.write(",")
            f.write("\n")
            print(lis)

            for i in ids:#写入去重后数据
                f.write(i)
                f.write(",")
            f.write("\n")
            print(ids)
             '''
            for i in lis:#计数
                if lis.count(i) >= 1:
                    a[i] = lis.count(i)
            print>>f,a
            f.write("\n")

            del lis[:]
            #del ids[:]
            a = {}
            j += 1
            lis.append(row[0])
            lis.append(row[1])
    else:
        break