# -*- encoding: utf-8 -*-
import os
import csv
import xlrd
import xlwt
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#network = csv.reader(open('E:\enron\week\week_network.csv','rb'))
data = xlrd.open_workbook('E:\enron_02\week\week_network_deal_wuhang.xls','rb')
table = data.sheet_by_name(u'Network_jishu')#通过名称获取
nrows = table.nrows
ncols = table.ncols
w = open(r"week_mark_10.txt","w")

#存储交互网络数据  首行问题未解决
list_people = []
list_mark = []*100

j = 1
for i in range(nrows):# r入网 w稳定 l离网
    list_mark.append(table.cell(i,0).value)
    for j in range(1,97):
        if type(table.cell(i,j).value) == float:#如果存在
            if type(table.cell(i,j-1).value) == float:#如果存在
                aw = table.cell(i,j-1).value
                print aw
                print type(aw)
                list_mark.append('w')
            else:#如果不存在，即前一时刻无交互
                ar = table.cell(i,j-1).value
                print ar
                print type(ar)
                list_mark.append('r')
        else:#如果不存在
            if type(table.cell(i,j-1).value) == float:#如果存在，前一时刻有交互
                al = table.cell(i,j-1).value
                print al
                print type(al)
                list_mark.append('l')
            else:#前一时刻无交互
                list_mark.append('?')

    print>>w,list_mark
    del list_mark[:]
    j = 1
