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
nrows = table.nrows
ncols = table.ncols

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

#存储时间索引
list_time = []
for i in range(nrows):
    list_time.append(int(table.cell(i,4).value))

#检索当前元素所在位置
def read_line(line,a,b,p):#返回当前索引元素所在位置
    sample = []
    for i in range(a,b):
        if line[i] == p:
            sample.append(i)
    return sample
    del sample[:]

w = 0


def paintnet(w,ws,we):
    week = xlwt.Workbook()
    sheet1 = week.add_sheet('%d'%(w+1),cell_overwrite_ok=True)
    for j in range(len(list_people[w])):
        sheet1.write(j+1,0,list_people[w][j])
        sheet1.write(0,j+1,list_people[w][j])
    for i in range(ws,we):
        if table.cell(i,5).value == w+1:
            a = list_people[w].index(table.cell(i,0).value)
            b = list_people[w].index(table.cell(i,1).value)
            sheet1.write(a+1,b+1,1)
        else:
            break
    s = 'E:\enron_02\\network\week_network_%d.xls'%(w+1)
    week.save(s)


for w in range(97):
    weizhi_s = list_time.index(w+1)#当前时刻首位索引
    weizhi_b = list_time.index(w+2)#下一时刻首位索引
    paintnet(w,weizhi_s,weizhi_b)



