#!/usr/bin/env python3

import pandas as pd
import numpy as np

m = pd.read_csv('cd.batch_corrected_ra.tsv',sep='\t',header=0,index_col=0)

meta = pd.read_csv('cd.metadata.tsv',sep='\t',header=0,index_col=0)
meta = meta[meta['label'] == 'CD']

cd_sample_list = list(meta.index)

m = m[cd_sample_list]

pair_m = pd.read_csv('cd_species_pair_smetana_score.tsv',sep='\t',header=0,index_col=0)
main_donors = ['HRGMv2_1879','HRGMv2_1765']
pair_m = pair_m[pair_m['donor'].isin(main_donors)]
pair_m = pair_m.sort_values(by=['receiver (taxa)','donor'], ascending=[True,False])
pair_m = pair_m.loc[['HRGMv2_3692 <- HRGMv2_1879'] + [idx for idx in pair_m.index if idx != 'HRGMv2_3692 <- HRGMv2_1879']]

m = m.T

def donor_group(df,donor,median):
    return 'High' if df[donor] > median else 'Low'

for donor in main_donors:
    meta[donor] = m.apply(donor_group, axis=1, args=(donor, np.median(m[donor])))

receivers = sorted(list(set(pair_m['receiver'])))

m = pd.concat([m[receivers], meta[main_donors]], axis=1)
m.to_csv('cd_donor_high_low.tsv',sep='\t')
