# -*- encoding: utf-8 -*-
import os
import csv
import xlrd
import xlwt
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

csv_reader = csv.reader(open('E:\enron\week\week_jishu_shuzhi.csv','rb'))
data_jiaohu = csv.reader(open('E:\enron\edge_02.csv','rb'))#6000条交互数据
f = open('activity_03.txt','w') #直接打开一个文件，如果文件不存在则创建文件

#读取每周参与讨论用户列表
list_people = [[] for a in range(1200)]
i = 0
j = 0
k = 0
for row in csv_reader:
    while row[j]:
        list_people[i].append(row[j])
        j += 1
    print list_people[i]
    #print len(list_people[i])
    #print i
    i += 1
    j = 0
#输出['1490', '9924', '1416']第72行报错  但输出到73行就报错，300长度应该是够的，很奇怪


#读取交互信息 收发邮件用户列表 两个分别存储
#读取交互拼接字典 成功存储
list_jiaohu = [[] for a in range(6300)]
list_jiaohu_pinjie = [[] for a in range(1200)]
list_jiaohu1 = []
list_jiaohu2 = []
list_jiaohu_pinjie1 = []
list_jiaohu_pinjie2 = []
list_time = []
jj = 0
for row in data_jiaohu:
    list_jiaohu1.append(row[0])
    list_jiaohu2.append(row[1])
    list_jiaohu_pinjie1.append(row[2])
    list_jiaohu_pinjie2.append(row[3])
    list_time.append(row[5])
    if not row[4].strip():
        break
    if row[4] == str(jj):
        #print row[4]
        list_jiaohu_pinjie[jj].append(row[2])
        list_jiaohu_pinjie[jj].append(row[3])
    else:
        #print jj
        #print list_jiaohu_pinjie[jj]
        jj += 1
        list_jiaohu_pinjie[jj].append(row[2])
        list_jiaohu_pinjie[jj].append(row[3])
#成功读入全部数据


#检索当前元素所在位置
def read_line(line,a,b,p):#返回当前索引元素所在位置
    sample = []
    for i in range(a,b):
        if line[i] == p:
            sample.append(i)
    return sample

#for x in range(0,115):
list_count = [[] for a in range(1200)]
p_position = []
p_jiaohu = []
for t in range(0,115):
    f.write(str(t))
    f.write("\n")
    for p in list_people[t]:
        print p
        #找索引  是否需要转型为int
        weizhi_s = list_time.index(str(t+1))#当前时刻首位索引
        weizhi_b = list_time.index(str(t+2))#下一时刻首位索引
        print weizhi_s
        p_position1 = read_line(list_jiaohu1,weizhi_s,weizhi_b,p)#p出现的地址 第一列
        p_position2 = read_line(list_jiaohu2,weizhi_s,weizhi_b,p)#p出现的地址 第二列
        p_position.extend(p_position1)
        p_position.extend(p_position2)#拼接成完整地址
        #print p_position1
        #print p_position2
        #print p_position
        for p1 in p_position:
            p_jiaohu.append(list_jiaohu_pinjie1[p1])
            p_jiaohu.append(list_jiaohu_pinjie2[p1])
        #print p_jiaohu
        #print len(p_jiaohu)
        a = set(p_jiaohu)
        b = set(list_jiaohu_pinjie[t+1])
        c = a & b
        cp = len(c)/2#存储每个元素的稳定度
        print cp
        #count_p.append(cp)
        f.write(p)
        f.write(":")
        f.write(str(cp))
        f.write(",")
    f.write("\n")


