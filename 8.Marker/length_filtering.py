#!/usr/bin/env python3

import pandas as pd

total = pd.read_csv("../../0.Pangenome_gene_summary/Total_sequence_ptn.tsv",sep='\t',header=0,index_col=0)
cluster = pd.read_csv("../../1.linclust/90/90.cluster_info.tsv",sep='\t',header=None,index_col=0)

cluster90_rep_list = list(cluster.index)
cluster90_rep_list.sort()

m = total.loc[cluster90_rep_list]
m.index.name = 'HRGMv2|Gene'

m.to_csv('cluster90_rep_ptn_sequences.tsv',sep='\t')

f_in = open('cluster90_rep_ptn_sequences.tsv')
f_out = open('length_filtering_results.tsv','w')

f_out.write(f_in.readline().strip()+"\tptn_length\tpass\n")

for line in f_in:
	hrgmgene,protein = line.strip().split()
	length = len(protein)
	PASS = 150 <= length <= 1500
	tokens = [hrgmgene,protein,str(length),str(PASS)]
	f_out.write('\t'.join(tokens)+"\n")

f_in.close()
f_out.close()

result = pd.read_csv('length_filtering_results.tsv',sep='\t',header=0,index_col=0)
result = result[result['pass'] == True]

f_list = open('length_filter_passed.list','w')
for i in result.index:
	f_list.write(i+"\n")
f_list.close()


