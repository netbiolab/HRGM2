#!/usr/bin/env python3

import sys
ext = sys.argv[1]

# 1.Make unique protein set
f_cluster = open('unique_protein_{}.cluster'.format(ext))

unique_protein_set = set()
for line in f_cluster:
	unique_protein_set.add(line.strip().split(";")[0])

f_cluster.close()

# 2.Extract unique protein sequences
f_in = open('../0.redundant_CDS/all_redundant_CDS.{}'.format(ext))
f_out = open('HRGMv2_unique_proteins.{}'.format(ext),'w')

for line in f_in:
	if line.strip().startswith('>'):
		gene = line.strip()[1:]
		if gene in unique_protein_set:
			write_flag = True
			f_out.write(line)
		else:
			write_flag = False
	else:
		if write_flag:
			f_out.write(line)

f_in.close()
f_out.close()
