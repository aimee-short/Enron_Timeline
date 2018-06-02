# -*- encoding: utf-8 -*-
import os
import csv
import xlrd
import xlwt
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

csv_reader = csv.reader(open('E:\enron\week\week_jishu_shuzhi.csv','rb'))
csv_reader1 = csv.reader(open('E:\enron\week\week_jishu_s1.csv','rb'))
csv_reader2 = csv.reader(open('E:\enron\week\week_jishu_s1.csv','rb'))
data_jiaohu = csv.reader(open('E:\enron\edge_02.csv','rb'))#6000条交互数据
f = open('activity_02.txt','w') #直接打开一个文件，如果文件不存在则创建文件

#读取每周参与讨论用户列表
list_people = [[] for a in range(1000)]
i = 0

k = 0
for row in csv_reader:
    for j in range(0,300):
        if row[j].strip():
            '''
            Traceback (most recent call last):
             File "E:/enron/week/Read_01.py", line 23, in <module>
            if row[j].strip():
            IndexError: list index out of range

            '''
            list_people[i].append(row[j])
            #j += 1
    print list_people[i]
    print len(list_people[i])
    print i
    i += 1

#输出['1490', '9924', '1416']第72行报错  但输出到73行就报错，300长度应该是够的，很奇怪
