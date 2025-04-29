#!/usr/bin/env python3

import pandas as pd

f_out = open('align_coreness.tsv','w')
f_out.write('HRGMv2 species\tCluster\tAlign coreness\n')

genome_meta = pd.read_csv("/nbl/user/mjy1064/3_genome_assembly/6_new_criteria/Dereplication_genomes_metadata.tsv",sep='\t',header=0,index_col=0)
genome_meta = genome_meta[genome_meta['Non-redundant'] == True]
genome_meta = genome_meta[['HRGMv2 cluster']]

summary = pd.read_csv('./sam_results/sam_summary.tsv',sep='\t',header=0,index_col=0)

assert set(genome_meta.index) == set(summary.index)

g = genome_meta.groupby('HRGMv2 cluster')

for hrgm,group in g:
	summary_group = summary.loc[group.index]
	
	n = len(summary_group)

	hrgmgene_count_dict = dict()

	for i in summary_group['Aligned clusters']:
		hrgmgene_list = i.split(",")
		for hrgmgene in hrgmgene_list:
			if hrgmgene not in hrgmgene_count_dict:
				hrgmgene_count_dict[hrgmgene] = 1
			else:
				hrgmgene_count_dict[hrgmgene] += 1

	
	key_list = list(hrgmgene_count_dict.keys())
	key_list.sort()

	for key in key_list:
		align_coreness = hrgmgene_count_dict[key] / n * 100
		f_out.write('{}\t{}\t{}\n'.format(hrgm,key,align_coreness))

f_out.close()
