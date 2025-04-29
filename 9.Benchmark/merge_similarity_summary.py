#!/usr/bin/env python3

import pandas as pd
import os

summary_out = './bray_curtis_similarity'
similarity_summary_list = [x for x in os.listdir(summary_out) if 'similarity_summary' in x]
similarity_summary_list.sort()

m_list = []

for tsv in similarity_summary_list:
	sample = tsv.split(".")[0]
	genomenum,complexity,temp = sample.split('_')

	m = pd.read_csv(summary_out+"/"+tsv,sep='\t',header=0,index_col=0)
	m.index.name = 'Classification method'
	m['Sample'] = sample
	m['# of Genomes'] = genomenum
	m['Complexity'] = complexity
	m = m.reset_index()
	
	m_list.append(m)

total = pd.concat(m_list)
total = total.replace({'Complexity': {'M': 'Single strain', 'H': 'Multiple strains'}})

total.to_csv('all_samples.similarity_summary.tsv',sep='\t',index=False)
