# -*- encoding: utf-8 -*-
import os
import csv
import xlrd
import xlwt
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

csv_reader = csv.reader(open('E:\enron\week\week_jishu_shuzhi.csv','rb'))
csv_dan = csv.reader(open('E:\enron\week\week_jishu.csv','rb'))#单行字符串集
data_jiaohu = csv.reader(open('E:\enron\edge_02.csv','rb'))#6000条交互数据
f = open('activity_01.txt','w') #直接打开一个文件，如果文件不存在则创建文件

#读取每周参与讨论用户列表
list_people = [[] for a in range(300)]
i = 0
j = 0
k = 0
'''
#方法1
for row in csv_reader:
    while row[j]:
        list_people[i].append(row[j])
        j += 1
    print list_people[i]
    print len(list_people[i])
    i += 1
    j = 0
#输出['1490', '9924', '1416']  但输出到73行就报错，300长度应该是够的，很奇怪
'''
#方法2
for row in csv_dan:
    str = row[0]
    list_people[i].append(str.split(','))
    print list_people[i]
    i += 1
# 输出[['1490', '9924', '1416', '']] 可成功读入所有数据  无法使用，所有数据均为一列


#读取时间列表
list_time = []
for row in data_jiaohu:
    list_time.append(row[4])
    if not row[4].strip():
        break
#print list_time
#输出['1', '1', '1'...应该是字符类型


#读取交互信息
#方法1 二维列表
list_jiaohu = [[] for a in range(6300)]
ii = 0
for row in data_jiaohu:
    list_jiaohu[ii].append(row[0])
    list_jiaohu[ii].append(row[1])
    #print list_jiaohu[ii]
    ii += 1
#成功读入全部数据


'''
#方法2 两个二维列表
list_jiaohu1 = []
list_jiaohu2 = []
list_pinjie1 = []
list_pinjie2 = []
list_time = []
for row in data_jiaohu:
    list_jiaohu1.append(row[0])
    list_jiaohu2.append(row[1])
    list_pinjie1.append(row[2])
    list_pinjie2.append(row[3])
    list_time.append(row[4])
    if not row[4].strip():
        break
'''

#for x in range(0,115):
list_count = [[] for a in range(1200)]
for x,rows in enumerate(data_jiaohu):
    #找索引
    xx = str(x)
    xy = str(x+1)
    xz = str(x+2) #是否需要转型 int
    weizhi_s = list_time.index(xx)#当前时刻首位索引
    weizhi_b = list_time.index(xy)#下一时刻首位索引
    weizhi_e = list_time.index(xz)#下下时刻首位索引
    print weizhi_e

    #读每周参与人员列表
    list_p = list_people[x]
    list_p_c = []
    p_position = []
    p_desitination = []
    for p in list_p:#依次检索当前周内每个用户
        #检索当前周 p 所在的所有位置
        p_position1 = read_line(list_jiaohu1,weizhi_s,weizhi_b,p)
        p_position2 = read_line(list_jiaohu2,weizhi_s,weizhi_b,p)
        p_position.extend(p_position1)
        p_position.extend(p_position2)
        for pp in p_position:
            p_current.append(p_position[pp])
        #检索下一周 p 所在的所有位置
        p_desitination1 = read_line(list_jiaohu1,weizhi_b,weizhi_e,p)
        p_desitination2 = read_line(list_jiaohu2,weizhi_b,weizhi_e,p)
        p_desitination.extend(p_desitination1)
        p_desitination.extend(p_desitination2)
        for pp in p_desitination:
            p_next.append(p_desitination[pp])




                '''
        #方法1 检索另一个用户
        for px in p_position1:#在当前周时间内进行检索
            count_p = 0
            temp1 = list_pinjie1[px]
            temp2 = list_pinjie2[px]
            for py in p_desitination1:
                if list_jiaohu2 == temp or :
                    count_p += 1
                    break
            for pz in p_desitination2:
                if list_jiaohu1 == temp:
                    count_p +=1
                    break
            list_count[x].append(count_p)
            '''
        #方法2 检索拼接字符串
        for px in range(weizhi_b,weizhi_e):
            if list_jiaohu1[x] == list_jiaohu1[px] or list_jiaohu1[x] == list_jiaohu2[px] or list_jiaohu2 == list_jiaohu1[px] or list_jiaohu2[x] == list_jiaohu2[px]:
                count_p += 1
                break
        list_count[x].append(count_p)

        #方法3 存成列表最后匹配



print list_count
#数据如何存储是个大问题



#检索当前元素所在位置
'''
#方法1 枚举 ×
def find_bing(x,y,z，p):
list_1 = []
list_2 = []
for idx, e in enumerate(a) if e == p
'''

#方法2 √
def read_line(line,a,b,p):#返回当前索引元素所在位置
    sample = []
    for i in range(a,b):
        if line[i] == p:
            sample.append(i)
    return sample