#!/usr/bin/env python3

import pandas as pd

m = pd.read_csv("/nbl/user/mjy1064/3_genome_assembly/6_new_criteria/0.final_data/genome_catalog/HRGMv2_Cluster_metadata.tsv",sep='\t',header=0,index_col=0)
m = m[m['# of Genomes'] == 1]

in_dir = '/nbl/user/mjy1064/3_genome_assembly/6_new_criteria/10.Pangenome/panaroo_outputs'
out_dir = './node_summary'

assert len(m) == 2185

for hrgm in m.index:
    fna = in_dir+"/"+hrgm+"/pan_genome_reference.fa"
    faa = in_dir+"/"+hrgm+"/pan_genome_reference.faa"

    dna_dict = dict()
    f_fna = open(fna)
    for line in f_fna:
        line = line.strip()
        if line.startswith('>'):
            gene_name = line[1:]
            if gene_name in dna_dict:
                raise(ValueError)
            dna_dict[gene_name] = ''
        else:
            dna_dict[gene_name] += line
    f_fna.close()

    ptn_dict = dict()
    f_faa = open(faa)
    for line in f_faa:
        line = line.strip()
        if line.startswith('>'):
            ptn_name = line[1:]
            if ptn_name in ptn_dict:
                raise(ValueError)
            ptn_dict[ptn_name] = ''
        else:
            ptn_dict[ptn_name] += line
    f_faa.close()

    assert set(dna_dict.keys()) == set(ptn_dict.keys())

    key_list = list(dna_dict.keys())
    #key_list.sort()

    total_dict = dict()
    for key in key_list:
        total_dict[hrgm+"|"+key] = {'ptn_sequence':ptn_dict[key],'dna_sequence':dna_dict[key]}

    result = pd.DataFrame.from_dict(total_dict,orient='index')
    result.to_csv(out_dir+"/"+hrgm+"_node.tsv",sep='\t')
