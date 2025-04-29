#!/usr/bin/env python3

import pandas as pd
import sys

# col 1 : Representative
# col 2 : LCA level
# col 3 : LCA
# col 4 : origin_HRGMv2

level_list = ['Species','Genus','Family','Order','Class','Phylum','Domain']

d = sys.argv[1]
n, name = d.split('.')

gmeta = pd.read_csv('/nbl/user/mjy1064/3_genome_assembly/6_new_criteria/Dereplication_genomes_metadata.tsv',sep='\t',header=0,index_col=0)
bin2otuid = pd.read_csv('/nbl/user/mjy1064/4_MWAS/1_classification/kraken2/0_kraken_DB_info/HRGMv2_Concat/bin2otuid.tsv',sep='\t',header=None,index_col=0)

meta = bin2otuid[2].str.split(';',expand=True)
meta.index.name = 'HRGMv2 cluster'
meta.columns = ['Domain','Phylum','Class','Order','Family','Genus','Species','Strain']
meta = meta.sort_index()
meta = meta.drop('Species',axis=1)

def change(df):
    return df['Strain'].replace('t__','s__')

meta['Species'] = meta.apply(change,axis=1)
meta = meta.drop('Strain',axis=1)

f_in = open(f'./{d}/{name}.cluster_info.updated.tsv')
f_out = open(f'./{d}/{name}.taxonomic_map.tsv','w')

for line in f_in:
    rep,count,members = line.strip().split()

    hrgm_set = set()
    for member in members.split(';'):
        genome = member.split('_')[0]
        hrgm_set.add(gmeta['HRGMv2 cluster'][genome])

    hrgm_list = list(hrgm_set)
    hrgm_list.sort()

    temp_meta = meta.loc[hrgm_list]
    lca_level = 'Root'
    lca = 'Root'

    for level in level_list:
        temp_set = set(temp_meta[level])
        if len(temp_set) == 1:
            lca_level = level
            lca = temp_set.pop()
            break

    f_out.write('{}\t{}\t{}\t{}\n'.format(rep,lca_level,lca,';'.join(hrgm_list))) 

f_in.close()
f_out.close()
