# -*- encoding: utf-8 -*-
import os
import csv
import xlrd
import xlwt
import math
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

data = xlrd.open_workbook('E:\enron_02\week\week_network_deal.xls')
network = data.sheet_by_name(u'Network_jishu')#网络
mark = data.sheet_by_name(u'Network_mark')#标记
bingji = data.sheet_by_name(u'Network_bingji')#并集
jiaoji = data.sheet_by_name(u'Network_jiaoji')#交集
timeline = data.sheet_by_name(u'Timeline')#result
nrows = network.nrows
ncols = network.ncols

for i in range(1,nrows):
    for j in range(1,ncols):
        if mark.cell(i,j).value == 'l':
            print network.cell(i,j).value
            a = network.cell(i,j).value.encode("utf-8")
            al = round(float(a))
            t = math.log10(al+1)
            timeline.write(i,j,math.fabs(t))
        else:
            if mark.cell(i,j).value == 'r':
                print network.cell(i,j+1).value
                a = network.cell(i,j+1).value.encode("utf-8")
                print a
                print type(a)
                ar = round(float(a))
                print ar
                br = math.log10(ar+1)
                #print(ar)
                tt = math.pow(br,-1)
                timeline.write(i,j,math.fabs(tt))
            else:
                if mark.cell(i,j).value == 'w':
                    a = network.cell(i,j+1).value.encode("utf-8")
                    b = network.cell(i,j).value.encode("utf-8")
                    c = bingji.cell(i,j).value.encode("utf-8")
                    d = jiaoji.cell(i,j).value.encode("utf-8")

                    aw = round(float(network.cell(i,j+1).value))
                    bw = round(float(network.cell(i,j).value))
                    cw = round(float(bingji.cell(i,j).value))
                    dw = round(float(jiaoji.cell(i,j).value))

                    tw = math.log10(bw/aw)
                    ttw = math.log10(dw/aw)
                    ttt = math.fabs(tw) + math.fabs(ttw)
                    timeline.write(i,j,math.fabs(ttt))
