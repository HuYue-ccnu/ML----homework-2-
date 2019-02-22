# -*- coding: utf-8 -*-

import re

"""
读取鸢尾花数据
"""
def read_iris():
	attributes = []
	classes = []
	with open("data/HW2_cluster/iris.data.txt", "r", encoding="utf-8") as f:
		for line in f:
			if len(line.strip()) == 0:
				pass
			else:
				attrs = re.split(',', line.strip())
				if len(attrs) != 5:
					print(attrs)
				else:
					attr = [float(attrs[i]) for i in range(len(attrs) - 1)]
					attributes.append(attr)
					classes.append(attrs[4])
	return attributes, classes

def read_random1():
	datas = []
	with open("random_4.txt", 'r', encoding='utf-8') as f:
		for line in f:
			if len(line.strip()) == 0:
				pass
			else:
				data = re.split("\\s+", line.strip())
				if len(data) != 2:
					print(data)
				else:
					data = [float(i) for i in data]
					datas.append(data)
	return datas

def read_random_label():
	"""
	返回两组数据
	1、data = "1,0.697,0.46,Y,2,0.774,0.376, Y"
	用作LVQ
	2、data = "[[0.697, 0.46], [0.774,0.376]]"
	用作Kmeans
	3、
	用作mixturesOfGaussian
	"""
	data_LVQ = ""
	data_Kmeans = []
	attrs = []
	labels = []
	attrs_t = []
	attrs_str = []
	i = 0
	with open("random_label.txt", 'r', encoding='utf-8') as f:
		for line in f:
			data = re.split("\t", line.strip())
			if len(data) == 2:
				attrs_t.append(data[0].strip())
				labels.append(data[1].strip())
			else:
				print(data)
	

	for att_str in attrs_t:
		att_str = att_str[2:len(att_str)-2].strip()
		attr = re.split("\\s+", att_str)
		assert len(attr) == 2
		attr = [float(x) for x in attr]
		attrs.append(attr)

	assert len(attrs) == len(labels)
	#构造data_LVQ
	for i in range(len(attrs)):
		data_LVQ += str(i)
		data_LVQ += ','
		data_LVQ += ','.join([str(att) for att in attrs[i]])
		data_LVQ += ','
		data_LVQ += labels[i]
		data_LVQ += ','

		
	data_LVQ = data_LVQ[:len(data_LVQ)-1]
	data_Kmeans = attrs
	return data_LVQ, data_Kmeans

if __name__ == "__main__":

	read_random_label()