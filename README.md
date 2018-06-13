# Enron_Timeline
以时间轴为线索，构建每周的交互网络，利用Timeline计算网络演化过程中的波动情况
Timeline监测
1.数据以周围单位划分周期
2.将每周交互信息（a→b）网络化（	 a b
				a  1	
				b 1）
	并分别存储
3.统计每周进行交互行为的节点名单
4.判断节点类型（稳定节点、入网节点、离网节点）
5.统计节点每两周邻居节点的交集、并集格式
6.带入节点波动性公式中计算每个节点每周的波动情况
7.以周为单位汇总计算Timeline数值
8.绘制整个时间段内网络的Timeline波动情况，监测并锁定事件发生时段
9.用Gephi软件绘制时间轴内网络结构演化情况，可视化网络舆情演化


Step1：
	目的：划分周数
	工具：Excel   weeknum
	结果：edge_00.xlsx

Step2：
	目的：存储每周出现节点信息
	工具：
	结果：week_quchogn.txt	week_quchong_wuhang.txt	week_heng_wuhang.txt
Step3：
	目的：计算每周节点出现次数并集
	工具：Bingji_01.py   week_heng_wuhang.txt
	结果：week_jishu.txt
---------------------------------------
Step4：
	目的：分别存储每周交互数据
	工具：edge_01.py	E:\enron_02\edge\edgemap.xlsx
	结果：E:\enron_02\\edge\edgemap_%d.xls
Step5：
	目的：网络化每周交互数据
	工具：network_04.py	E:\enron_02\edge_02.xlsx
				E:\enron_02\week\week_dict.xlsx
	结果：E:\enron_02\\network\week_network_%d.xls
Step6：
	目的：计算每两周出现的所有节点数（并集）
	工具：Bing_06.py	E:\enron_02\week\week_dict.xlsx
				E:\enron_02\week\edge.xls
	结果：activity_21.txt
Step7：
	目的：计算每两周同时出现的节点数（交集）
	工具：Jiaoji_01.py	E:\enron_02\week\week_dict.xlsx
				E:\enron_02\week\edge.xls
	结果：jiaoji_02.txt
Step8：	
	目的：判断节点类型（入网，稳定，出网）
	工具：Distinguish_01.py		E:\enron_02\week\week_jishu.xlsx 
	结果：week_mark_02.txt
Step9：
	目的：计算每个节点每周邻居节点数目
	工具：Timeline_01.py	E:\enron\edge_00.csv
	结果：week_16.txt
Step10：
	目的：计算Timeline
	工具：Excel
	结果：E:\enron_02\week\week_network_deal.xls
-----------------------------------------

Stepa：
	目的：多个Excel合并
	工具：Excel	宏  Sub 合并当前目录下所有工作簿的全部工作表()
	结果：E:\enron_02\network\week_network.xls
Stepb：
	目的：多个Excel批量转存为csv
	工具：Excel	宏  Sub SaveToCSVs()
	结果：E:\enron_02\edge_node_csv
Stepc：
	目的：根据一列内容合并多个表格
	工具：Excel	VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])
	结果：E:\enron_03\PageRan\PageRank_all.xls

----------------------------------------------
Step11：
	目的：为Gephi提供每周交互节点集合
	工具：Timeset_01.py	E:\enron_02\week\week_dict.xlsx
				E:\enron_02\people.xls
	结果：week_timeset_03.txt
Step11：
	目的：为Gephi提供每周交互边集合
	工具：edge_01.py	E:\enron_02\edge\edgemap.xlsx
	结果：E:\enron_02\\DL\edge_%d.xls
Step11：
	目的：为Gephi提供Timeline 47~77 交互所有节点集合
	工具：network_00.py	E:\enron_02\edge_02.xlsx
	结果：E:\enron_03\\Week_all_Timeline_02.txt

Step11：
	目的：为Gephi提供Timeline 47~77 交互所有节点全部信息（姓名）
	工具：Timeline_node.py	E:\enron_02\people.xls
	结果：E:\enron_03\Timeline_all_node.xls
Step11：
	目的：为Ucinet提供Timeline 47~77 交互网络
	工具：network_01.py	E:\enron_03\Timeline_all_edge.xlsx
				E:\enron_03\Week_all_Timeline_02.txt
	结果：E:\enron_03\\Timeline_all_edge_net.xlsx

Ucinet绘制交互网络
-----------------------------------------------

Step1:
	目的：从数据库中提取出邮件内容并分别存储
	工具：Find_01.py	E:\enron_03\messages_fenci
				E:\enron_03\he\negative-words.txt
				E:\enron_03\he\positive-words.txt
	结果：E:\enron_03\he\Sentiment_result.txt


Step1:
	目的：分词
	工具：Senti_Snow_01.py	E:/enron_03/messages_body/%d.txt
				E:\enron_03\he\negative-words.txt
				E:\enron_03\he\positive-words.txt
	结果：E:/enron_03/messages_fenci/%d.txt


Step1:
	目的：计算情感
	工具：Senti_Snow_01.py	E:\enron_03\messages_fenci
				E:\enron_03\he\negative-words.txt
				E:\enron_03\he\positive-words.txt
	结果：E:\enron_03\he\Sentiment_result.txt
Step2：
	目的：汇总47~77人员名单
	工具：Timeline_dict_01.py	E:\enron_02\week\week_dict.xlsx		
	结果：E:\enron_03\\Timeline_dict_01.txt

Step3：
	目的：计算PageRank
	工具：PageRank_01.py	E:\enron_02\\edge\edgemap_%d.xls
				E:\enron_02\week\week_dict.xlsx
	结果：E:\enron_03\\PageRank.xls
Step4：
	目的：整合PageRank
	工具：Timeline_PageRank.py	E:\enron_03\PageRank_shu\All.xlsx
	结果：E:\enron_03\\Timeline_PageRank_01.xls
Step5:
	目的：PageRank周数展示
	工具：Excel	counta/vlookup
	结果：E:\enron_03\\Timeline_PageRank_01.xls

--------------------------------------------------------

Step5:
	目的：PageRank所有周数全部汇总
	工具：PageRank_all.py	E:\enron_02\week\week_dict.xlsx
				E:\enron_02\edge\edgemap.xlsx
	结果：E:\enron_03\\PageRank_all.xls
-----------------------------------------------------------
Step5:
	目的：PageRank滑动窗口计算
	工具：PageRank_window.py	E:\enron_02\week\week_dict.xlsx
					E:\enron_02\edge\edgemap.xlsx
	结果：E:\enron_03\PageRank_time_5\PageRank_%d.xls

Step5:
	目的：PageRank单周影响力汇总（每周前30名）
	工具：Timeline_PageRank_dan_deal.py	E:\enron_03\PageRank_result\PageRank_dan_deal.xlsx
	结果：E:\enron_03\PageRank_result\PageRank_dan_all_deal.xls

Step5:
	目的：PageRank单周节点汇总（每周前30名）
	工具：Timeline_PageRank_dan_deal_02.py	E:\enron_03\PageRank_result\PageRank_dan_deal.xlsx
	结果：E:\enron_03\PageRank_result\PageRank_dan_all_deal.xls
