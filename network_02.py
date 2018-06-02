# -*- encoding: utf-8 -*-
import os
import csv
import xlrd
import xlwt
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

data = xlrd.open_workbook('E:\enron_02\edge_02.xlsx')
table = data.sheet_by_name(u'edge')#通过名称获取
w1 = data.sheet_by_name(u'w1')#通过名称获取
nrowp = table.nrows
ncolp = table.ncols

#导入每周用户参与列表
dict = xlrd.open_workbook('E:\enron_02\week\week_dict.xlsx','rb')
t_dict = dict.sheet_by_index(0)#通过索引获取
nrowd = t_dict.nrows
ncold = t_dict.ncols

#每周参与用户列表
list_people = [[] for a in range(1200)]
for i in range(nrowd):
    for j in range(ncold):
        if t_dict.cell(i,j).value:
            list_people[i].append(str(t_dict.cell(i,j).value))
        else:
            break
    #print list_people[i][i]
#存储时间索引
list_time = []
for i in range(nrowd):
    list_time.append(int(table_jiaohu.cell(i,4).value))


#检索当前元素所在位置
def read_line(line,a,b,p):#返回当前索引元素所在位置
    sample = []
    for i in range(a,b):
        if line[i] == p:
            sample.append(i)
    return sample
    del sample[:]

wb = xlwt.Workbook()

list_row = []
w = 1
j = 1
for i in range(0,97):
    '''
    a = ('%d.txt'%(i))
    f = open(a,'w')
    f.write(i)
    f.write(' ');
    f.write(list_people[i])
    '''
    ws = wb.add_sheet(i)

    print list_people[i]
    weizhi_s = list_time.index(i+1)#当前时刻首位索引
    weizhi_b = list_time.index(i+2)#下一时刻首位索引
    for p in list_people[i]:
        f.write(p);
        for ii in range(weizhi_s,weizhi_b):
            if table.cell(ii,0).value == p:
                a = list_people[i].index(table.cell(i,b).value)
                weizhi_m = list_people.index(p)
                list_row[p] = 1
            else:
                f.write(list_row)
            del list_row[:]
                f.close()
            break



    for ii in list_people[i]:
        x = int(ii)
        print list_people[i][x]

        y = list_people[w][x]
        sheet_t.write(x+1,0,y)
        sheet_t.write(0,x+1,y)