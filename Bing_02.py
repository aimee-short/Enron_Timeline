# -*- encoding: utf-8 -*-
import os
import csv
import xlrd
import xlwt
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

csv_reader = csv.reader(open('E:\enron\week\week_jishu.csv','rb'))

lists = [[] for i in range(115)]
#lists = [] *300
i = 0
for row in csv_reader:
    str = row[0]
    lists[i].append(str.split(','))
    print lists[i]
    i += 1#输出[['1490', '9924', '1416', '']]
''''
    lists.append(str.split(','))
    print lists
    del lists[:]#输出[['1490', '9924', '1416', '']] 二维列表？
'''



