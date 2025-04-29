#!/usr/bin/env python3

import pandas as pd

m = pd.read_csv("../1.length_filtering/90_length_filtered.cluster_info.tsv",sep='\t',header=None,index_col=0)

target_list = []
f = open('filtering_target.list')
for line in f:
	target_list.append(line.strip())
f.close()

assert len(target_list) == 68078

m = m.loc[target_list]
m.index.name = 'Target cluster'
m.columns = ['HRGMGENE members']
m['Mean cluster-genome coverage'] = ''
m['pass'] = ''

#################################################################################################################

hrgm_meta = pd.read_csv("/nbl/user/mjy1064/3_genome_assembly/6_new_criteria/0.final_data/genome_catalog/HRGMv2_Cluster_metadata.tsv",sep='\t',header=0,index_col=0)

panaroo_result_dir = '/nbl/user/mjy1064/3_genome_assembly/6_new_criteria/10.Pangenome/panaroo_outputs'

hrgm_panaroo_dict = dict()
for hrgm in hrgm_meta[hrgm_meta['# of Genomes'] >= 2].index:
	hrgm_panaroo_dict[hrgm] = pd.read_csv(panaroo_result_dir+"/"+hrgm+"/gene_presence_absence.Rtab",sep='\t',header=0,index_col=0)

assert len(hrgm_panaroo_dict) == 2639

for cluster in m.index:
	hrgmgene_member_list = m['HRGMGENE members'][cluster].split(";")
	
	hrgm_set = set()
	count = 0

	for hrgmgene in hrgmgene_member_list:
		hrgm,gene = hrgmgene.split("|")
		hrgm_set.add(hrgm)
		
		if hrgm_meta['# of Genomes'][hrgm] == 1:
			count += 1
		else:
			count += sum(list(hrgm_panaroo_dict[hrgm].loc[gene]))

	N = 0
	for hrgm in hrgm_set:
		N += hrgm_meta['# of Genomes'][hrgm]
	
	#m['Mean cluster-genome coverage'][cluster] = count / N

	cov = count / N
	m['Mean cluster-genome coverage'][cluster] = cov
	m['pass'][cluster] = cov < 1.5

m.to_csv('paralog_filtering_results.tsv',sep='\t')

###############################################################################################################

past = pd.read_csv("../1.length_filtering/90_length_filtered.cluster_info.tsv",sep='\t',header=None,index_col=0)

total_set = set(past.index)
remove_set = set(m[m['pass'] == False].index)
pass_set = total_set - remove_set
pass_list = list(pass_set)
pass_list.sort()

past = past.loc[pass_list]
past.to_csv('90_length_paralog_filtered.cluster_info.tsv',sep='\t')
