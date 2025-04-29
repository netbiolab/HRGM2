#!/usr/bin/env python3

import pandas as pd

meta = pd.read_csv('/nbl/user/mjy1064/3_genome_assembly/6_new_criteria/0.final_data/genome_catalog/HRGMv2_Cluster_metadata.tsv',sep='\t',header=0,index_col=0)
meta = meta[['# of Genomes']]

def get_threshold(hrgm):
	num = meta['# of Genomes'][hrgm]

	threshold = ''
	if num < 100:
		threshold = 60
	else:
		threshold = 50

	return threshold

ac_m = pd.read_csv('align_coreness_corrected.tsv',sep='\t',header=0,index_col=0)
candidate_m = pd.read_csv('../1.coreness/final_final_filtered_marker_candidates.tsv',sep='\t',header=0,index_col=0)

marker_list = []

g = ac_m.groupby('Cluster')

for candidate,group in g:
	hrgm = candidate_m['HRGMv2'][candidate]

	if hrgm not in group.index:
		continue

	t = get_threshold(hrgm)
	if group['Align coreness'][hrgm] <= t:
		continue

	is_marker = True
	for other_hrgm in group.index:
		if other_hrgm == hrgm:
			continue
		if group['Align coreness'][other_hrgm] > 1:
			is_marker = False
			break

	if is_marker:
		marker_list.append(candidate)


marker_m = candidate_m.loc[marker_list]
marker_m.to_csv("final_markers.tsv",sep='\t')
