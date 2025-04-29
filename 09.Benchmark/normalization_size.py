#!/usr/bin/env python3

import pandas as pd

cluster_meta = pd.read_csv("/nbl/user/mjy1064/3_genome_assembly/6_new_criteria/0.final_data/genome_catalog/HRGMv2_Cluster_metadata.tsv",sep='\t',header=0,index_col=0)
genome_meta = pd.read_csv("/nbl/user/mjy1064/3_genome_assembly/6_new_criteria/Dereplication_genomes_metadata.tsv",sep='\t',header=0,index_col=0)
genome_meta = genome_meta[genome_meta['Non-redundant'] == True]

m = pd.DataFrame(index=cluster_meta.index,columns=['Rep','Avg'])

for hrgm in m.index:
    # 1. Fill Rep size
    rep_genome = cluster_meta['Representative Genome'][hrgm]
    rep_size = genome_meta['Length'][rep_genome]
    m['Rep'][hrgm] = rep_size * 1e-06

    # 2. Fill Avg size
    hrgm_genomes = genome_meta[genome_meta['HRGMv2 cluster'] == hrgm]
    avg_size = sum(list(hrgm_genomes['Length'])) / len(hrgm_genomes)
    m['Avg'][hrgm] = avg_size * 1e-06

for c in m.columns:
    if True in set(m[c].isna()):
        raise(ValueError)

m.to_csv('normalization_size.tsv',sep='\t')    
