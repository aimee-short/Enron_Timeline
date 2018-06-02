# -*- encoding: utf-8 -*-
import os
import csv
import xlrd
import xlwt
import time
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
#算交集，少的
data = xlrd.open_workbook('E:\enron_02\week\week_dict.xlsx','rb')
table = data.sheet_by_index(0)#通过索引获取
nrows = table.nrows
ncols = table.ncols
data_jiaohu = xlrd.open_workbook('E:\enron_02\week\edge.xls','rb')#6000条交互数据
table_jiaohu = data_jiaohu.sheet_by_index(0)#通过索引获取
nrows_jiaohu = table_jiaohu.nrows
ncols_jiaohu = table_jiaohu.ncols
f = open('activity_21.txt','w') #直接打开一个文件，如果文件不存在则创建文件
t1 = time.time()

#读取每周参与讨论用户列表
list_people = [[] for a in range(1200)]
for i in range(nrows):# r入网 w稳定 l离网
    for j in range(ncols):
        if table.cell(i,j).value:
            list_people[i].append(table.cell(i,j).value)
        else:
            break

print list_people[94]
print list_people[95]
print list_people[96]


#读取交互信息 收发邮件用户列表 两个分别存储
#读取交互拼接字典 成功存储
list_jiaohu = [[] for a in range(6300)]
list_jiaohu_pinjie = [[] for a in range(4000)]
list_jiaohu1 = []
list_jiaohu2 = []
list_jiaohu_pinjie1 = []
list_jiaohu_pinjie2 = []
list_time = []
ii = 1
for i in range(nrows_jiaohu):
    list_jiaohu1.append(table_jiaohu.cell(i,0).value)
    list_jiaohu2.append(table_jiaohu.cell(i,1).value)
    list_jiaohu_pinjie1.append(table_jiaohu.cell(i,2).value)
    list_jiaohu_pinjie2.append(table_jiaohu.cell(i,3).value)
    list_time.append(int(table_jiaohu.cell(i,4).value))
    if table_jiaohu.cell(i,4).value == ii:
        #print table_jiaohu.cell(i,4).value
        list_jiaohu_pinjie[ii].append(table_jiaohu.cell(i,2).value)
        list_jiaohu_pinjie[ii].append(table_jiaohu.cell(i,3).value)
    else:
        #print ii
        #print list_jiaohu_pinjie[ii]
        ii += 1
        list_jiaohu_pinjie[ii].append(table_jiaohu.cell(i,2).value)
        list_jiaohu_pinjie[ii].append(table_jiaohu.cell(i,3).value)
#成功读入全部数据
print list_jiaohu_pinjie[94]
print list_jiaohu_pinjie[95]
print list_jiaohu_pinjie[96]

#检索当前元素所在位置
def read_line(line,a,b,p):#返回当前索引元素所在位置
    sample = []
    for i in range(a,b):
        if line[i] == p:
            sample.append(i)
    return sample
    del sample[:]

#for x in range(0,115):
list_count = [[] for a in range(1200)]
p_position = []
p_jiaohu = []
for t in range(1,100):
    print ('第%d周：'%t)
    if t == 96:
        t2 = time.time()
        print("稳定度计算完成，耗时："+str(t2-t1)+"秒。") #反馈结果
        break
    f.write(str(t))
    f.write("\n")
    weizhi_s = list_time.index(t)#当前时刻首位索引
    weizhi_b = list_time.index(t+1)#下一时刻首位索引
    weizhi_e = list_time.index(t+2)#下下时刻首位索引
    #print weizhi_s
    #print weizhi_b
    #print weizhi_e
    for p in list_people[t-1]:
        #print p
        # 查找当前周p出现的位置
        p_position1 = read_line(list_jiaohu1,weizhi_s,weizhi_b,int(p))#p出现的地址 第一列
        p_position2 = read_line(list_jiaohu2,weizhi_s,weizhi_b,int(p))#p出现的地址 第二列
        p_position.extend(p_position1)
        p_position.extend(p_position2)#拼接成完整地址
        #print p_position1
        #print p_position2
        print p_position
        for p1 in p_position:
            p_jiaohu.append(list_jiaohu_pinjie1[p1])
            p_jiaohu.append(list_jiaohu_pinjie2[p1])
        #print p_jiaohu
        #print len(p_jiaohu)
        a = set(p_jiaohu)
        b = set(list_jiaohu_pinjie[t+1])
        c = a & b
        cp = len(c)/2#存储每个元素的稳定度
        cc = a | b
        cj = len(cc)/2
        #count_p.append(cp)
        f.write(str(p))
        f.write(":")
        f.write(str(cp))
        f.write(",")
        del p_position1[:]
        del p_position2[:]
        del p_position[:]
        del p_jiaohu[:]
    f.write("\n")
