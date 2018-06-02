# -*- encoding: utf-8 -*-
import os
import csv
import xlrd
import xlwt
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#network = csv.reader(open('E:\enron\week\week_network.csv','rb'))
data = xlrd.open_workbook('E:\enron_02\week\week_dict.xlsx','rb')
table = data.sheet_by_index(0)#通过索引获取
nrows = table.nrows
ncols = table.ncols
wt = open(r"week_timeset_03.txt","w")

data_p = xlrd.open_workbook('E:\enron_02\people.xls','rb')
t_people = data_p.sheet_by_index(0)#通过名称获取
nrowp = t_people.nrows
ncolp = t_people.ncols

def findtimeset(w):
    list_set = []
    for i in range(nrows):
        for j in range(ncols):
            if table.cell(i,j).value == w:
                list_set.append(i+1)
                break
    #wt.write(str(w));
    wt.write(str(list_set))
    wt.write('\n')
    del list_set[:]

for i in range(1,nrowp):
    findtimeset(t_people.cell(i,0).value)