#!/usr/bin/env python3

import pandas as pd
import sys
import skbio.diversity as sd

sample = sys.argv[1]
classification_out_dir = './classification_outputs/{}'.format(sample)

size_df = pd.read_csv('normalization_size.tsv',sep='\t',header=0,index_col=0)

# 0. Summary DataFrame
method_list = ['Kraken2_Rep__0.0.bracken','Kraken2_Rep__0.2.bracken','Kraken2_Concat__0.0.bracken','Kraken2_Concat__0.2.bracken','Metaphlan4_Marker__None.txt']
method_norm_list = ['Answer']

for method in method_list:
	method_norm_list.append(method+'|None')
	if 'Kraken2' in method:
		method_norm_list.append(method+'|Rep')
		if 'Concat' in method:
			method_norm_list.append(method+'|Avg')

summary_df = pd.DataFrame(0.0,index=size_df.index,columns=method_norm_list)

# 1. Answer_composition
answer_sheet = pd.read_csv('../camisim_in_out/{}/out/taxonomic_profile_0.txt'.format(sample),sep='\t',header=0,index_col=0,skiprows=4)
answer_sheet = answer_sheet[answer_sheet['RANK'] == 'strain']

g = answer_sheet.groupby('_CAMI_OTU')
for hrgm,group in g:
	summary_df['Answer'][hrgm] = sum(list(group['PERCENTAGE'])) * 0.01


# 2. Each method composition
for method in summary_df.columns:
	if method == 'Answer':
		continue
	
	tool_method,norm = method.split('|')
	
	if tool_method.startswith('Kraken2'):
		bracken = pd.read_csv('{}/{}__{}'.format(classification_out_dir,sample,tool_method),sep='\t',header=0,index_col=0)
		bracken['HRGMv2'] = [x.split('/')[-1] for x in bracken.index]
		bracken = bracken.set_index('HRGMv2')
		bracken = bracken[['new_est_reads']]
		
		rpt = '{}/{}__{}'.format(classification_out_dir,sample,tool_method).replace('.bracken','.rpt')
		f_rpt = open(rpt)
		temp_count_1 = int(f_rpt.readline().strip().split()[1])
		temp_count_2 = int(f_rpt.readline().strip().split()[1])
		f_rpt.close()

		total_count = temp_count_1 + temp_count_2
		root_count = sum(list(bracken['new_est_reads']))
		ori_root_ra = root_count / total_count

		if norm == 'None':
			bracken['new_est_reads'] = bracken['new_est_reads'] / total_count
		else:
			for hrgm in bracken.index:
				bracken['new_est_reads'][hrgm] = bracken['new_est_reads'][hrgm] / size_df[norm][hrgm]
			normalized_root_count = sum(list(bracken['new_est_reads']))
			bracken['new_est_reads'] = bracken['new_est_reads'] / normalized_root_count * ori_root_ra
		
		summary_df[method] = bracken['new_est_reads']

	else:
		m = pd.read_csv('{}/{}__{}'.format(classification_out_dir,sample,tool_method),sep='\t',header=0,index_col=0,skiprows=4)
		t_list = []
		for i in m.index:
			if 't__' in i:
				t_list.append(i)
		m = m.loc[t_list]
		m = m[['relative_abundance']]
		for name in m.index:
			hrgm = name.split('/')[-1]
			summary_df[method][hrgm] = m['relative_abundance'][name] * 0.01


summary_df.to_csv('./bray_curtis_similarity/{}.abundance_summary.tsv'.format(sample),sep='\t')

# 3. Bray curtis distance matrix
m_t = summary_df.transpose()
d = sd.beta_diversity("braycurtis",m_t,ids=m_t.index)
dm = d.to_data_frame()
dm = dm[['Answer']]
dm = dm.drop('Answer')
dm['Bray Curtis Similarity'] = 1 - dm['Answer']
del dm['Answer']
dm.to_csv('./bray_curtis_similarity/{}.similarity_summary.tsv'.format(sample),sep='\t')
	
