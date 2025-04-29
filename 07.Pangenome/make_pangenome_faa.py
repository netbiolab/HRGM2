#!/usr/bin/env python3

import pandas as pd
import os

ptn_df = pd.read_csv("/nbl/user/mjy1064/3_genome_assembly/6_new_criteria/11.Marker/0.Pangenome_gene_summary/Total_sequence_ptn.tsv",sep='\t',header=0,index_col=0)

ptn_df['HRGMv2'] = [x.split("|")[0] for x in ptn_df.index]

for i in ptn_df.index:
	if not i.startswith(ptn_df['HRGMv2'][i]):
		raise(ValueError)

meta = pd.read_csv("/nbl/user/mjy1064/3_genome_assembly/6_new_criteria/0.final_data/genome_catalog/HRGMv2_Cluster_metadata.tsv",sep='\t',header=0,index_col=0)

size_1_set = set(meta[meta['# of Genomes'] == 1].index)

g = ptn_df.groupby('HRGMv2')

for hrgm,group in g:
	if hrgm in size_1_set:
		continue

	if os.path.isfile('./panaroo_outputs/{}/pan_genome_reference.faa'.format(hrgm)):
		raise(ValueError)

	f = open('./panaroo_outputs/{}/pan_genome_reference.faa'.format(hrgm),'w')
	for hrgmgene in group.index:
		genename = hrgmgene.split("|")[-1]
		
		f.write('>{}\n'.format(genename))
		f.write('{}\n'.format(group['ptn_sequence'][hrgmgene]))

	f.close()

	
