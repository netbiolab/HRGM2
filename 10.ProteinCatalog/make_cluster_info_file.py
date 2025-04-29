#!/usr/bin/env python3

import sys

past_cluster_info = sys.argv[1]
cur_linclust_cluster = sys.argv[2]
d = "/".join(cur_linclust_cluster.split("/")[:-1])
tag = sys.argv[3]

#1. Make past_cluster_info_dict
past_cluster_info_dict = dict()
f_past = open(past_cluster_info)

for line in f_past:
	rep,members = line.strip().split()
	past_cluster_info_dict[rep] = members

f_past.close()

#2. Make cur_cluster_info_dict
cur_cluster_info_dict = dict()
f_cur = open(cur_linclust_cluster)

for line in f_cur:
	rep,mem = line.strip().split()
	if rep not in cur_cluster_info_dict:
		cur_cluster_info_dict[rep] = [mem]
	else:
		cur_cluster_info_dict[rep].append(mem)

f_cur.close()

#3. Write output cluster_info.tsv
key_list = list(cur_cluster_info_dict.keys())
#key_list.sort()

f_out = open(d+"/"+tag+".cluster_info.tsv","w")
for key in key_list:
	tokens = []
	for mem in cur_cluster_info_dict[key]:
		tokens.append(past_cluster_info_dict[mem])
	new_line = key+"\t"+";".join(tokens)+"\n"
	f_out.write(new_line)

f_out.close()
