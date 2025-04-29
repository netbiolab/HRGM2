#!/usr/bin/env python3

import pandas as pd

genome_meta = pd.read_csv('../Dereplication_genomes_metadata.tsv',sep='\t',header=0,index_col=0)

f_out = open('tRNA_summary.tsv','w')
f_out.write('Genome\t# tRNA\n')

for genome in genome_meta.index:
	domain_tag = genome_meta['Domain'][genome][3:7].lower()
	f_in = open('./tRNAscanSE_results/{}/{}.tRNAscanSE.{}.summary'.format(genome,genome,domain_tag))
	lines = f_in.readlines()
	f_in.close()

	count_lines = lines[-25:]

	if not count_lines[0].startswith('Isotype / Anticodon Counts:'):
		f_out.write('{}\tNA\n'.format(genome))
		continue

	error_flag = False
	trna = 0

	for line in count_lines[2:-1]:
		head = line.split('\t')[0]
		colon_index = head.find(':')
		name = head[:colon_index].strip()

		if name in ['Supres','SelCys','Undet']:
			continue
		
		try:
			c = int(head[colon_index+1:])
			if c > 0:
				trna += 1
			
		except:
			error_flag = True
			break

	if error_flag:
		f_out.write('{}\tNA\n'.format(genome))
	else:
		f_out.write('{}\t{}\n'.format(genome,trna))

f_out.close()
