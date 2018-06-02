# -*- encoding: utf-8 -*-
import os
import csv
import xlrd
import xlwt
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#network = csv.reader(open('E:\enron\week\week_network.csv','rb'))
data = xlrd.open_workbook('E:\enron_02\week\week_jishu.xlsx','rb')
table = data.sheet_by_name(u'Network_deal')#通过名称获取
nrows = table.nrows
ncols = table.ncols
w = open(r"week_mark_02.txt","w")

#存储交互网络数据  首行问题未解决
list_people = []
list_mark = []*100

j = 1
for i in range(nrows):# r入网 w稳定 l离网
    list_mark.append(table.cell(i,0).value)
    for j in range(1,97):
        if table.cell(i,j).value:#如果存在
            if table.cell(i,j-1).value:#如果存在
                list_mark.append('w')
            else:#如果不存在，即前一时刻无交互
                list_mark.append('r')
        else:#如果不存在
            if table.cell(i,j-1).value:#如果存在，前一时刻有交互
                list_mark.append('l')
            else:#前一时刻无交互
                list_mark.append('?')

    print>>w,list_mark
    del list_mark[:]
    j = 1

'''
#csv读取方式
for row in network:# r入网 w稳定 l离网
    list_mark.append(row[0])
    while row[j]:
        if row[j] >= 1:
            if row[j-1] == 0:
                list_mark.append('r')
            else:
                list_mark.append('w')
        else:
            if row[j-1] >= 1:
                list_mark.append('l')
            else:
                list_mark.append(' ')
        j += 1
    print list_mark
    del list_mark[:]
    j = 1
'''
