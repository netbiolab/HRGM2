#!/usr/bin/env python3

import pandas as pd
from scipy.stats import fisher_exact
import numpy as np

lmi_clades = ['o__TANB77','o__RF39']

m = pd.read_csv('LMI_smetana_detail_summary.tsv',sep='\t',header=0,index_col=None)
meta = pd.read_csv('prevalent1000_additional_meta.tsv',sep='\t',header=0,index_col=0)
pair_m = pd.read_csv('prevalent1000_lmi_result.pair_type_order_add.tsv',sep='\t',header=0,index_col=0)

bigg = pd.read_csv('./disease_association/bigg_models_metabolites.txt',sep='\t',header=0,index_col=1)
bigg = bigg[['name']]
bigg = bigg.drop_duplicates()
bigg = bigg['name'].to_dict()

m['receiver (order)'] = m['receiver'].map(meta['Order'])
m = m[m['receiver (order)'].isin(lmi_clades)]
m = m[m['mus'] > 0.9]

def generate_pair(df):
    return '__'.join(sorted([df['receiver'], df['donor']]))

m['pair'] = m.apply(generate_pair,axis=1)
m['pair type'] = m['pair'].map(pair_m['Pair type'])

idx = 0
result_dict = dict()

for lmi in lmi_clades:
    m_sub = m[m['receiver (order)'] == lmi]
    pair_m_sub = pair_m[(pair_m['Order 1'] == lmi) | (pair_m['Order 2'] == lmi)]

    total_coopO_count = len(pair_m_sub[pair_m_sub['Pair type'] == 'Cooperative'])
    total_coopX_count = len(pair_m_sub[pair_m_sub['Pair type'] != 'Cooperative'])

    one_percent = len(pair_m_sub) / 100
    
    g = m_sub.groupby('compound')
    for compound,group in g:

        if len(group) <= one_percent:
            continue

        name = bigg[compound[2:-2]]

        coopO_transO_count = len(group[group['pair type'] == 'Cooperative'])
        coopX_transO_count = len(group[group['pair type'] != 'Cooperative'])
        coopO_transX_count = total_coopO_count - coopO_transO_count    
        coopX_transX_count = total_coopX_count - coopX_transO_count

        coopO_transO_percentage = coopO_transO_count / total_coopO_count * 100
        coopX_transO_percentage = coopX_transO_count / total_coopX_count * 100

        log2_fold_change = np.log2(coopO_transO_percentage/coopX_transO_percentage)

        pvalue = fisher_exact([[coopO_transO_count, coopX_transO_count], [coopO_transX_count, coopX_transX_count]], alternative='two-sided')[1]
        log_pvalue = -np.log10(pvalue)

        result_dict[idx] = [lmi, name, coopO_transO_count, coopX_transO_count, coopO_transX_count, coopX_transX_count, coopO_transO_percentage, coopX_transO_percentage, log2_fold_change, log_pvalue]
        idx += 1


result = pd.DataFrame.from_dict(result_dict, orient='index')
result.columns = ['LMI','Metabolite','CoopO.TransO','CoopX.TransO','CoopO.TransX','CoopX.TransX','CoopO.TransO %','CoopX.TransO %','Log2 Fold Change','-Log10 P value']

result = result.replace({'Fe2+ mitochondria':'Fe2+', 'H2O H2O':'H2O', 'Iron (Fe3+)':'Fe3+', 'Sulfur':'S'})
result = result[result['Metabolite'] != 'O2 O2']

result.to_csv('metabolite_donation_to_LMI.tsv',sep='\t',index=False)
