#!/usr/bin/env python3

import pandas as pd

genome_meta = pd.read_csv('../Dereplication_genomes_metadata.tsv',sep='\t',header=0,index_col=0)
genome_meta = genome_meta[genome_meta['Non-redundant'] == True]

prokka_dir = '/nbl/user/mjy1064/3_genome_assembly/6_new_criteria/6.Genome_annotation/prokka_results'

g = genome_meta.groupby('HRGMv2 cluster')
for hrgm,group in g:
	if len(group) == 1:
		continue
	
	genome_list = list(group.index)
	genome_list.sort()

	f = open("./panaroo_inputs/{}.panaroo_input.list".format(hrgm),"w")
	for genome in genome_list:
		f.write("{}/{}/{}.gff\n".format(prokka_dir,genome,genome))
	f.close()


