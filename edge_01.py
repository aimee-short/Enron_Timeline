# -*- encoding: utf-8 -*-
import os
import csv
import xlrd
import xlwt
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#network = csv.reader(open('E:\enron\week\week_network.csv','rb'))
data = xlrd.open_workbook('E:\enron_02\edge\edgemap.xlsx')
table = data.sheet_by_index(0)#通过名称获取
nrows = table.nrows
ncols = table.ncols

#存储时间索引
list_time = []
for i in range(nrows):
    list_time.append(table.cell(i,6).value)

#检索当前元素所在位置
def read_line(line,a,b,p):#返回当前索引元素所在位置
    sample = []
    for i in range(a,b):
        if line[i] == p:
            sample.append(i)
    return sample
    del sample[:]


def paintnet(w,ws,we):
    week = xlwt.Workbook()
    sheet1 = week.add_sheet('%d'%(w+1),cell_overwrite_ok=True)
    for j in range(9):
        a = table.cell(0,j).value
        sheet1.write(0,j,a)
    t = 1
    for i in range(ws,we):
        if table.cell(i,6).value == w+1:
            for ii in range(9):
                sheet1.write(t,ii,table.cell(i,ii).value)
            t += 1
        else:
            break
    s = 'E:\enron_02\\edge\edgemap_%d.xls'%(w+1)
    week.save(s)

for w in range(97):
    weizhi_s = list_time.index(w+1)#当前时刻首位索引
    weizhi_b = list_time.index(w+2)#下一时刻首位索引
    paintnet(w,weizhi_s,weizhi_b)



