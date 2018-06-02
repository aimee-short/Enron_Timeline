# -*- encoding: utf-8 -*-
import os
import csv
import xlrd
import xlwt
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#network = csv.reader(open('E:\enron\week\week_network.csv','rb'))
data = xlrd.open_workbook('E:\enron_02\edge_02.xlsx')
table = data.sheet_by_name(u'edge')#通过名称获取
w1 = data.sheet_by_name(u'w1')#通过名称获取
nrows = table.nrows
ncols = table.ncols

nrowp = w1.nrows
ncolp = w1.ncols

#导入每周用户参与列表
dict = xlrd.open_workbook('E:\enron_02\week\week_dict.xlsx','rb')
t_dict = dict.sheet_by_index(0)#通过索引获取
nrowd = t_dict.nrows
ncold = t_dict.ncols

#每周参与用户列表
list_people = [[] for a in range(255)]
for i in range(nrowd):
    for j in range(ncold):
        if t_dict.cell(i,j).value:
            list_people[i].append(t_dict.cell(i,j).value)
        else:
            break
    #print list_people[i][0]#type float


w = 0
week = xlwt.Workbook()
sheet1 = week.add_sheet('%d'%(w+1),cell_overwrite_ok=True)
for i in range(0,nrows):
        if table.cell(i,5).value == 1:
            #a = table.cell(i,0).value # type float
            a = list_people[w].index(table.cell(i,0).value)
            b = list_people[w].index(table.cell(i,1).value)
            sheet1.write(a,b,1)
        else:
            print w


week.save('E:\enron_02\\network\week_network_01.xls')