#!/usr/bin/env python3

import pandas as pd

candidate = pd.read_csv("final_filtered_marker_candidates.tsv",sep='\t',header=0,index_col=0)
past_candidate_list = list(candidate.index)

uniq_m = pd.read_csv("../2.uniqueness/core_summary.tsv",sep='\t',header=0,index_col=0)
uniq_m = uniq_m.loc[past_candidate_list]

assert len(candidate) == len(uniq_m)
assert set(candidate.index) == set(uniq_m.index)
assert set(uniq_m['# of core species']) == {1}

remove_set = set()

all_core_m = pd.read_csv("coreness.tsv",sep='\t',header=0,index_col=0)

uniq_m = uniq_m[uniq_m['# of shared species (Uniqueness)'] > 1]
assert len(uniq_m) == 154825

for cluster in uniq_m.index:
	core_hrgm = candidate['HRGMv2'][cluster]
	
	m = all_core_m.loc[cluster]

	assert len(m) == uniq_m['# of shared species (Uniqueness)'][cluster]

	m = m[m['HRGMv2'] != core_hrgm]

	flag = True
	for c in m['Coreness']:
		if c > 1:
			flag = False
			break

	if flag == False:
		remove_set.add(cluster)

print(len(remove_set))
past_candidate_set = set(candidate.index)
cur_candidate_set = past_candidate_set - remove_set
cur_candidate_list = list(cur_candidate_set)
cur_candidate_list.sort()

candidate = candidate.loc[cur_candidate_list]

candidate.to_csv("final_final_filtered_marker_candidates.tsv",sep='\t')
