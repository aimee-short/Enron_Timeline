# -*- encoding: utf-8 -*-
import os
import csv
import xlrd
import xlwt
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#计数
list = []
csv_reader = csv.reader(open('E:\enron\edge_00.csv','rb'))
#f = open('week_11.txt','w') #直接打开一个文件，如果文件不存在则创建文件
f = open('week_12.xls','w')

j = 1
a = {}
for row in csv_reader:
    if row:
        if row[5] == str(j):
            list.append(row[0])
            list.append(row[1])
        else:
            #f.write('%d\n'%j)
            for i in list :
                if list.count(i) >= 1:
                    a[i] = list.count(i)
            print>>f,a
            f.write("\n")
            '''
            for ii in a:
                f.write(ii)
                f.write(",")
            f.write("\n")
            '''
            j += 1
            del list[:]
            a = {}
            list.append(row[0])
            list.append(row[1])
    else:
        print('Fininsh!')




'''
#find the cols and save to a txt
outputfilename=testin + '.txt'
outputfile=open(outputfilename,'w')

#find the rows which you want to select and write to a txt file
for i in range(nrows):
    cell_value=sh.cell_value(i, columnnum)
    if testin in str(cell_value):
        outputs=sh.row_values(i)
        for tim in outputs:
            outputfile.write('%s    ' %(tim))
        outputfile.write('%s' %(os.linesep))
outputfile.close()
'''