#!/usr/bin/env python3

import pandas as pd
import os

summary_dir = '/home2/shlee354/microbiome/hrgmv2_bracken_thr_test/classification_evaluation_metrics' # 수정됨
file_list = os.listdir(summary_dir)
file_list.sort()

m_list = []

for tsv in file_list:
	sample = tsv.split(".")[0]
	genomenum,complexity,temp = sample.split('_')
	
	m = pd.read_csv(summary_dir+"/"+tsv,sep='\t',header=0,index_col=0)
	m.index.name = 'Classification method'
	m['Sample'] = sample
	m['# of Genomes'] = genomenum
	m['Complexity'] = complexity
	m = m.reset_index()
	
	m_list.append(m)

total = pd.concat(m_list)

total.to_csv('all_samples.metrics_summary_2.tsv',sep='\t',index=False) #수정됨
