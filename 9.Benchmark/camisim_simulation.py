#!/usr/bin/env python3

import sys
import os
import pandas as pd
import random

genome_num = sys.argv[1] # int
complexity = sys.argv[2] # L or M or H
sample_id = sys.argv[3] # int

assert complexity in ['L','M','H']

sample_name = '_'.join([genome_num,complexity,sample_id])
sample_dir = './camisim_in_out/{}'.format(sample_name)
os.mkdir(sample_dir)

# 1. Genome selection --> genome_list
if complexity == 'L':
	m = pd.read_csv("/nbl/user/mjy1064/3_genome_assembly/6_new_criteria/0.final_data/genome_catalog/HRGMv2_Cluster_metadata.tsv",sep='\t',header=0,index_col=0)
	genome_list = list(m['Representative Genome'])
	random.shuffle(genome_list)
	genome_list = genome_list[:int(genome_num)]

elif complexity == 'M':
	m = pd.read_csv("/nbl/user/mjy1064/3_genome_assembly/6_new_criteria/Dereplication_genomes_metadata.tsv",sep='\t',header=0,index_col=0)
	m = m[m['Non-redundant'] == True]
	
	hrgm_list = list(set(m['HRGMv2 cluster']))
	random.shuffle(hrgm_list)
	hrgm_list = hrgm_list[:int(genome_num)]
	hrgm_set = set(hrgm_list)

	genome_list = []
	g = m.groupby('HRGMv2 cluster')
	for hrgm,group in g:
		if hrgm in hrgm_set:
			tmp_list = list(group.index)
			random.shuffle(tmp_list)
			genome_list.append(tmp_list[0])

elif complexity == 'H':
	m = pd.read_csv("/nbl/user/mjy1064/3_genome_assembly/6_new_criteria/Dereplication_genomes_metadata.tsv",sep='\t',header=0,index_col=0)
	m = m[m['Non-redundant'] == True]

	g = m.groupby('HRGMv2 cluster')
	group_list = []
	for hrgm,group in g:
		group_list.append((hrgm,group))
	random.shuffle(group_list)

	temp_count = int(genome_num)
	genome_list = []
	for hrgm,group in group_list:
		tmp_list = list(group.index)
		random.shuffle(tmp_list)

		if temp_count < 5:
			tmp_list = tmp_list[:temp_count]
		else:
			tmp_list = tmp_list[:5]
	
		genome_list.extend(tmp_list)
		temp_count -= len(tmp_list)
		
		if temp_count == 0:
			break

else:
	raise(ValueError)


assert len(genome_list) == int(genome_num)

# 2. Make sample metadata
total_meta = pd.read_csv("total_metadata.tsv",sep='\t',header=0,index_col=0)
total_meta = total_meta.loc[genome_list]
total_meta.to_csv(sample_dir+"/metadata.tsv",sep='\t')

total_path = pd.read_csv("total_id_to_genome_file.tsv",sep='\t',header=None,index_col=0)
total_path = total_path.loc[genome_list]
total_path.to_csv(sample_dir+"/id_to_genome_file.tsv",sep='\t',header=False)

# 3. Make ini
f_default = open("default.ini")
f_ini = open(sample_dir+"/config.ini","w")

for line in f_default:
	if line.startswith('output_directory'):
		line = line.strip()+"/"+sample_name+"/out\n"
	elif line.startswith('metadata'):
		line = line.strip()+"/"+sample_name+"/metadata.tsv\n"
	elif line.startswith('id_to_genome_file'):
		line = line.strip()+"/"+sample_name+"/id_to_genome_file.tsv\n"
	elif line.startswith('genomes_total') or line.startswith('num_real_genomes'):
		line = line.strip()+genome_num+"\n"
	f_ini.write(line)

f_default.close()
f_ini.close()

# 4. Run CAMISIM
os.system("/usr/bin/time -v python ./CAMISIM/metagenomesimulation.py {}/config.ini".format(sample_dir))
