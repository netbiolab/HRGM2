#!/usr/bin/env python3

import pandas as pd

m = pd.read_csv("../1.length_filtering/90_length_filtered.cluster_info.tsv",sep='\t',header=None,index_col=0)

target_list = []

for i in m[1]:
	d = dict()
	
	for hrgmgene in i.split(";"):
		hrgm,gene = hrgmgene.split("|")
		if hrgm not in d:
			d[hrgm] = 1
		else:
			d[hrgm] += 1

	assert sum(d.values()) == len(i.split(";"))

	for value in d.values():
		if value >= 2:
			target_list.append(i.split(";")[0])
			break

f = open('filtering_target.list','w')
for target in target_list:
	f.write(target+"\n")

f.close()
