#!/usr/bin/env python3

import pandas as pd

hrgm_meta = pd.read_csv("/nbl/user/mjy1064/3_genome_assembly/6_new_criteria/0.final_data/genome_catalog/HRGMv2_Cluster_metadata.tsv",sep='\t',header=0,index_col=0)

def hrgm_coreness_threshold(hrgm):
	n = hrgm_meta['# of Genomes'][hrgm]
	if n < 100:
		threshold = 60
	else:
		threshold = 50

	return threshold

f_in = open('coreness.tsv')
f_out = open('coreness_filtered.tsv','w')

f_out.write(f_in.readline())

for line in f_in:
	cluster,hrgm,coreness = line.strip().split()
	coreness = float(coreness)
	t = hrgm_coreness_threshold(hrgm)
	
	if coreness > t:
		f_out.write(line)

f_in.close()
f_out.close()		
