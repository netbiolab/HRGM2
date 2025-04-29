#!/usr/bin/env python3

import pandas as pd

dna_m = pd.read_csv("/nbl/user/mjy1064/3_genome_assembly/6_new_criteria/11.Marker/0.Pangenome_gene_summary/Total_sequence_dna.tsv",sep='\t',header=0,index_col=0)
candidate_m = pd.read_csv("/nbl/user/mjy1064/3_genome_assembly/6_new_criteria/11.Marker/3.Marker/1.coreness/final_final_filtered_marker_candidates.tsv",sep='\t',header=0,index_col=0)

dna_m = dna_m.loc[candidate_m.index]
assert len(dna_m) == 3781152

f = open("candidate_reads.fa","w")

for cluster in dna_m.index:
    dna = dna_m['dna_sequence'][cluster]
    dna_len = len(dna)

    q = dna_len // 150

    for i in range(1,q+1):
        read_name = cluster+"|"+str(i)
        dna_read = dna[150*(i-1):150*i]
        f.write('>{}\n'.format(read_name))
        f.write(dna_read+"\n")

f.close() 
