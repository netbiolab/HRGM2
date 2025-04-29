#!/usr/bin/env python3

import pandas as pd

genome_meta = pd.read_csv('../Dereplication_genomes_metadata.tsv',sep='\t',header=0,index_col=0)

f_out = open('rRNA_summary.tsv','w')
f_out.write('Genome\t# of 5S rRNA\t# of 16S rRNA\t# of 23S rRNA\n')

for genome in genome_meta.index:
	domain_tag = genome_meta['Domain'][genome][3:7].lower()
	f_in = open('./barrnap_results/{}/{}.barrnap.1e-04.{}.tsv'.format(genome,genome,domain_tag))
	f_in.readline()

	n_5 = 0
	n_16 = 0
	n_23 = 0

	for line in f_in:
		line = line.strip()
		region,barrnap,rRNA,start,end,evalue,direction,point,name = line.split('\t')
		evalue = float(evalue)
		
		if rRNA != 'rRNA':
			continue

		if '5S' in name:
			n_5 += 1
		elif '16S' in name and evalue < 1e-05:
			n_16 += 1
		elif '23S' in name and evalue < 1e-05:
			n_23 += 1

		
	f_out.write('{}\t{}\t{}\t{}\n'.format(genome,n_5,n_16,n_23))
	f_in.close()

f_out.close()

