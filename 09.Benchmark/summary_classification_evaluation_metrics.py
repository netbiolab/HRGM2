#!/usr/bin/env python3

import sys
import pandas as pd

sample = sys.argv[1]

# 1. Answer_set
answer_sheet = pd.read_csv('../camisim_in_out/{}/out/taxonomic_profile_0.txt'.format(sample),sep='\t',header=0,index_col=0,skiprows=4)
answer_sheet = answer_sheet[answer_sheet['RANK'] == 'strain']
answer_set = set(answer_sheet['_CAMI_OTU'])


# 2. Prediction_set & Calculate classification evaluation metrics

method_list = ['Kraken2_Rep__0.0.bracken','Kraken2_Rep__0.2.bracken','Kraken2_Concat__0.0.bracken','Kraken2_Concat__0.2.bracken','Metaphlan4_Marker__None.txt']
summary_df = pd.DataFrame(columns=['TP','FP','FN'], index=method_list)

classification_out_dir = './classification_outputs/{}'.format(sample)

for method in method_list:
	file_path = '{}/{}__{}'.format(classification_out_dir,sample,method)

	# 1) Prediction set	
	prediction_set = set()
	m = ''

	if method.endswith('bracken'):
		m = pd.read_csv(file_path,sep='\t',header=0,index_col=0)
		m['HRGMv2'] = [x.split('/')[-1] for x in m.index]
		m = m[m['new_est_reads'] != 0]
		prediction_set = set(m['HRGMv2'])
		
	elif method.endswith('txt'):
		m = pd.read_csv(file_path,sep='\t',header=0,index_col=0,skiprows=4)

		t_list = []
		for i in m.index:
			if 't__' in i:
				t_list.append(i)
		m = m.loc[t_list]

		m['HRGMv2'] = [x.split('/')[-1] for x in m.index]
		m = m[m['relative_abundance'] != 0]
		prediction_set = set(m['HRGMv2'])
		
	else:
		raise(ValueError)

	# 2) Calculate classification evaluation metrics
	TP = len(answer_set.intersection(prediction_set))
	FP = len(prediction_set - answer_set)
	FN = len(answer_set - prediction_set)

	summary_df['TP'][method] = TP
	summary_df['FP'][method] = FP
	summary_df['FN'][method] = FN


summary_df['Precision'] = summary_df['TP'] / (summary_df['TP'] + summary_df['FP'])
summary_df['Recall'] = summary_df['TP'] / (summary_df['TP'] + summary_df['FN'])
summary_df['F1 score'] = 2 / ((1/summary_df['Precision']) + (1/summary_df['Recall']))

summary_df.to_csv('./classification_evaluation_metrics/{}.metrics_summary.tsv'.format(sample),sep='\t')
