#!/usr/bin/env python3

import sys
import pandas as pd
import os

genome = sys.argv[1]

prokka_dir = '/nbl/user/mjy1064/3_genome_assembly/6_new_criteria/6.Genome_annotation/prokka_results/'+genome
out_dir = '/nbl/user/mjy1064/3_genome_assembly/6_new_criteria/7.Protein_catalog/0.redundant_CDS/prokka_CDS/'+genome
os.mkdir(out_dir)

ori_tsv = prokka_dir+"/"+genome+".tsv"
ori_fna = prokka_dir+"/"+genome+".ffn"
ori_faa = prokka_dir+"/"+genome+".faa"

new_tsv = out_dir+"/"+genome+".tsv"
new_fna = out_dir+"/"+genome+".fna"
new_faa = out_dir+"/"+genome+".faa"

# 1. Rename header
m = pd.read_csv(ori_tsv,sep='\t',header=0,index_col=0)
m = m[m['ftype'] == 'CDS']
m = m[['length_bp']]
m = m.reset_index()
m['cds_tag'] = [genome+"_"+str(i+1) for i in m.index]
m = m.set_index('locus_tag')
m.to_csv(new_tsv,sep='\t')

# 2. Rename fna
f_ori_fna = open(ori_fna)
f_new_fna = open(new_fna,'w')

for line in f_ori_fna:
    # Header
    if line.startswith('>'):
        locus_tag = line.strip().split()[0][1:]
        if locus_tag in m.index:
            cds_tag = m['cds_tag'][locus_tag]
            f_new_fna.write('>'+cds_tag+"\n")
            write_flag = True
        else:
            cds_tag = 'NOCDSTAG'
            write_flag = False
    
    # NC line
    else:
        if write_flag:
            f_new_fna.write(line)

f_ori_fna.close()
f_new_fna.close()

# 3. Rename faa
f_ori_faa = open(ori_faa)
f_new_faa = open(new_faa,'w')

for line in f_ori_faa:
    # Header
    if line.startswith('>'):
        locus_tag = line.strip().split()[0][1:]
        cds_tag = m['cds_tag'][locus_tag]
        f_new_faa.write('>'+cds_tag+"\n")
    
    # AA line
    else:
        f_new_faa.write(line)

f_ori_faa.close()
f_new_faa.close()
