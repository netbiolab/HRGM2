#!/usr/bin/env python3

import pandas as pd
import sys

lmi_clade = sys.argv[1]

m = pd.read_csv('prevalent_top1000_result.pair_type_add.tsv',sep='\t',header=0,index_col=0)
meta = pd.read_csv('/nbl/user/mjy1064/3_genome_assembly/6_new_criteria/0.final_data/genome_catalog/HRGMv2_Cluster_metadata.tsv',sep='\t',header=0,index_col=0)

prevalent_1000_species = list(set(m['Species 1']).union(set(m['Species 2'])))
prevalent_1000_species.sort()

meta = meta.loc[prevalent_1000_species]

m['Order 1'] = m['Species 1'].map(meta['Order'])
m['Order 2'] = m['Species 2'].map(meta['Order'])

def lmi_clade_pair(df):
    if df['Order 1'] == df['Order 2']:
        return False
    else:
        return df['Order 1'] == lmi_clade or df['Order 2'] == lmi_clade

m['LMI clade pair'] = m.apply(lmi_clade_pair,axis=1)

m = m[m['LMI clade pair'] == True]

def another_order(df):
    if df['Order 1'] == lmi_clade:
        return df['Order 2']
    elif df['Order 2'] == lmi_clade:
        return df['Order 1']
    else:
        raise(ValueError)

m['Another order'] = m.apply(another_order,axis=1)

def another_species(df):
    if df['Order 1'] == lmi_clade:
        return df['Species 2']
    elif df['Order 2'] == lmi_clade:
        return df['Species 1']
    else:
        raise(ValueError)

m['Another species'] = m.apply(another_species,axis=1)

result = pd.DataFrame(meta['Order'].value_counts())
result.index.name = 'Order'
result.columns = ['Species count']
result = result[result['Species count'] > 10]
result = result.drop(['o__TANB77','o__RF39'])
result.columns.name = lmi_clade

new_columns = ['Pair count','Cooperative pair count','Cooperative pair proportion','Species count (Cultured)', 'Pair count (Cultured)', 'Cooperative pair count (Cultured)', 'Cooperative pair proportion (Cultured)']

for new_column in new_columns:
    result[new_column] = -1

result['Cooperative pair proportion'] = result['Cooperative pair proportion'].astype(float)
result['Cooperative pair proportion (Cultured)'] = result['Cooperative pair proportion (Cultured)'].astype(float)

for order in result.index:
    m_order = m[m['Another order'] == order]
    result['Pair count'][order] = len(m_order)
    result['Cooperative pair count'][order] = len(m_order[m_order['Pair type'] == 'Cooperative'])
    result['Cooperative pair proportion'][order] = result['Cooperative pair count'][order] / result['Pair count'][order] * 100

    meta_order = meta[meta['Order'] == order]
    cultured = list(meta_order[meta_order['Genome type'] != 'MAG'].index)   
    result['Species count (Cultured)'][order] = len(cultured)
    
    m_order_cultured = m_order[m_order['Another species'].isin(cultured)]
    result['Pair count (Cultured)'][order] = len(m_order_cultured)
    result['Cooperative pair count (Cultured)'][order] = len(m_order_cultured[m_order_cultured['Pair type'] == 'Cooperative'])
    result['Cooperative pair proportion (Cultured)'][order] = result['Cooperative pair count (Cultured)'][order] / result['Pair count (Cultured)'][order] * 100
 
result = result.sort_values('Cooperative pair proportion',ascending=False)
result.to_csv(f'cooperative_order_{lmi_clade}.tsv',sep='\t')
