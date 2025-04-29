#!/usr/bin/env python3

import sys

ext = sys.argv[1]

f = open('../0.redundant_CDS/all_redundant_CDS.{}'.format(ext))

protein_genelist_dict = dict()

for line in f:
	line = line.strip()
	
	#Header line
	if line.startswith('>'):
		try:
			if seq not in protein_genelist_dict:
				protein_genelist_dict[seq] = [gene]
			else:
				protein_genelist_dict[seq].append(gene)
		except:
			pass

		gene = line[1:]
		seq = ''

	#Sequence line
	else:
		seq += line

f.close()

if seq not in protein_genelist_dict:
	protein_genelist_dict[seq] = [gene]
else:
	protein_genelist_dict[seq].append(gene)

f_out = open('unique_protein_{}.cluster'.format(ext),'w')
for key in protein_genelist_dict:
	genelist = protein_genelist_dict[key]
	f_out.write(';'.join(genelist)+'\n')
f_out.close()	
