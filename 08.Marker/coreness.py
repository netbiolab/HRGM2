#!/usr/bin/env python3

import pandas as pd

# Cluster metadata
cluster = pd.read_csv("../../2.filtering/2.paralog_filtering/90_length_paralog_filtered.cluster_info.tsv",sep='\t',header=None,index_col=0)
cluster.index.name = 'Cluster'
cluster.columns = ['HRGMGENE members']

# HRGM metadata
hrgm_meta = pd.read_csv("/nbl/user/mjy1064/3_genome_assembly/6_new_criteria/0.final_data/genome_catalog/HRGMv2_Cluster_metadata.tsv",sep='\t',header=0,index_col=0)

def hrgm_size(hrgm):
	return hrgm_meta['# of Genomes'][hrgm]

# HRGM panaroo dictionary
hrgm_panaroo_dict = dict()

for hrgm in hrgm_meta[hrgm_meta['# of Genomes'] >= 2].index:
	hrgm_panaroo_dict[hrgm] = pd.read_csv('/nbl/user/mjy1064/3_genome_assembly/6_new_criteria/10.Pangenome/panaroo_outputs/'+hrgm+'/gene_presence_absence.Rtab',sep='\t',header=0,index_col=0)

# Coreness matrix
#m = pd.DataFrame(0,index=list(cluster.index),columns=list(hrgm_meta.index))

# Coreness result file
f = open('coreness.tsv','w')
f.write('Cluster\tHRGMv2\tCoreness\n')

# Main
for clu in cluster.index: #m --> cluster
	hrgmgene_list = cluster['HRGMGENE members'][clu].split(";")

	hrgm_gene_dict = dict()
	for hrgmgene in hrgmgene_list:
		hrgm,gene = hrgmgene.split("|")
		if hrgm not in hrgm_gene_dict:
			hrgm_gene_dict[hrgm] = [gene]
		else:
			hrgm_gene_dict[hrgm].append(gene)

	for hrgm in hrgm_gene_dict.keys():
		if hrgm_size(hrgm) == 1:
			#m[hrgm][clu] = 100
			f.write("{}\t{}\t{}\n".format(clu,hrgm,100))
		else:
			exist_list = list(hrgm_panaroo_dict[hrgm].loc[hrgm_gene_dict[hrgm]].sum())
			exist_count = 0
			for c in exist_list:
				if c >= 1:
					exist_count += 1
			#m[hrgm][clu] = exist_count / len(exist_list) * 100
			f.write("{}\t{}\t{}\n".format(clu,hrgm,exist_count / len(exist_list) * 100))

#m.to_csv('coreness.tsv',sep='\t')
f.close()
