#!/usr/bin/env python3

import pandas as pd
import sys

flag = eval(sys.argv[1])

m = pd.read_csv('prevalent_top1000_result.pair_type_add.tsv',sep='\t',header=0,index_col=0)
meta = pd.read_csv('/nbl/user/mjy1064/3_genome_assembly/6_new_criteria/0.final_data/genome_catalog/HRGMv2_Cluster_metadata.tsv',sep='\t',header=0,index_col=0)

def same_rank(df):
    return df['Rank 1'] == df['Rank 2']

for rank in ['Phylum','Class','Order','Family','Genus']:
    m['Rank 1'] = m['Species 1'].map(meta[rank])
    m['Rank 2'] = m['Species 2'].map(meta[rank])
    m['Same rank'] = m.apply(same_rank,axis=1)

    print('----------------------------------------------')
    print(rank)
    
    same = m[m['Same rank'] == flag]
    print('Total',len(same))

    print()
    print('Count')
    print(same['Pair type'].value_counts())

    print()
    print('Percentage')
    print(same['Pair type'].value_counts(normalize=True) * 100) 

    print('----------------------------------------------')
    print()
