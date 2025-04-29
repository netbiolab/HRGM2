#!/usr/bin/env python3

import pandas as pd

cluster = pd.read_csv("/nbl/user/mjy1064/3_genome_assembly/6_new_criteria/11.Marker/2.filtering/2.paralog_filtering/90_length_paralog_filtered.cluster_info.tsv",sep='\t',header=None,index_col=0)
cluster_list = list(cluster.index)

cluster_uniqueness_dict = dict()

for c in cluster_list:
	hrgm_set = set()

	hrgmgene_list = cluster[1][c].split(";")
	
	for hrgmgene in hrgmgene_list:
		hrgm,gene = hrgmgene.split("|")
		hrgm_set.add(hrgm)

	cluster_uniqueness_dict[c] = len(hrgm_set)

result = pd.DataFrame.from_dict(cluster_uniqueness_dict,orient='index')

result.index.name = 'Cluster'
result.columns = ['# of shared species (Uniqueness)']

result.to_csv("all_uniqueness.tsv",sep='\t')
