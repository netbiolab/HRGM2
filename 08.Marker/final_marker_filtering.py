#!/usr/bin/env python3

import pandas as pd

m = pd.read_csv("final_markers.tsv",sep='\t',header=0,index_col=0)

# 1. Uniqueness update

temp = pd.read_csv('align_coreness_corrected.tsv',sep='\t',header=0,index_col=None)

candidate_uniqueness_dict = dict()

g = temp.groupby('Cluster')
for candidate,group in g:
	candidate_uniqueness_dict[candidate] = len(group)

uniq = pd.DataFrame.from_dict(candidate_uniqueness_dict,orient='index')
uniq.columns = ['# of shared species']

m['# of shared species'] = uniq['# of shared species']

# 2. Length update

length = pd.read_csv("/nbl/user/mjy1064/3_genome_assembly/6_new_criteria/11.Marker/2.filtering/1.length_filtering/length_filtering_results.tsv",sep='\t',header=0,index_col=0)

m['ptn_length'] = length['ptn_length']

for column in m.columns:
	test_set = set(m[column].isna())
	if True in test_set:
		raise(ValueError)

m.to_csv("final_markers_filtering_info.tsv",sep='\t')

# 3. Filter final markers

filtered_markers = list()

for hrgm, hrgmdf in m.groupby('HRGMv2'):
	# Uniqueness --> ascending ; Length --> descending
	hrgmdf = hrgmdf.sort_values(['# of shared species','ptn_length'],ascending=[True,False])
	filtered_markers.extend(list(hrgmdf.index[:200]))

m = m.loc[filtered_markers]
m = m[['HRGMv2']]

m.to_csv('final_markers_filtered.tsv',sep='\t')
