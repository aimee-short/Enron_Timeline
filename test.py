# -*- encoding: utf-8 -*-
import os
import csv
import xlrd
import xlwt
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
'''
data = xlrd.open_workbook('E:\enron_02\week\week_dict.xlsx','rb')
table = data.sheet_by_index(0)#通过索引获取
nrows = table.nrows
ncols = table.ncols
#读取每周参与讨论用户列表
list_people = [[] for a in range(1200)]
for i in range(nrows):# r入网 w稳定 l离网
    for j in range(ncols):
        if table.cell(i,j).value:
            list_people[i].append(table.cell(i,j).value)
        else:
            break
    print type(list_people[i][0])

print list_people[94]
print list_people[95]
print list_people[96]

data = xlrd.open_workbook('E:\enron_02\edge_02.xlsx')
table = data.sheet_by_name(u'edge')#通过名称获取
w1 = data.sheet_by_name(u'w1')#通过名称获取
nrows = table.nrows
ncols = table.ncols

w = 1
for i in range(nrows):
        if table.cell(i,5).value == w:
            a = type(table.cell(i,0).value)
            b = table.cell(i,1).value
            print a
            print b
            print type(table.cell(i,0).value)

'''

wbk_1 = xlwt.Workbook()                     #建一个新文件
a = 1
sheet_1 = wbk_1.add_sheet('%d'%(a+1),cell_overwrite_ok=True)
sheet_2 = wbk_1.add_sheet('XXX2',cell_overwrite_ok=True)           #新文件表名称，可改写

sheet_1.write(0,0,'test1')
sheet_2.write(0,0,'test2')
b = 'E:\enron_02\\network\week_network_%d.xls'%(a+1)

wbk_1.save(b)