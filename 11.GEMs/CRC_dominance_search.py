#!/usr/bin/env python3

import pandas as pd

m = pd.read_csv('crc.kraken2.data',sep='\t',header=0,index_col=0)
m = m.T
m = m[m['label'] == 'CRC']

sample_meta = m[['batch','country','label']]

m = m.drop(['batch','country','label'], axis=1)
m = m.T

all_m = m.copy() #all_m : all taxa, relative abundance
for sample in all_m.columns:
    count_sum = sum(all_m[sample].astype(float))
    all_m[sample] = all_m[sample].astype(float) / count_sum

crc_m = m.copy()

crc_enriched = pd.read_csv('crc_enriched_taxa.tsv',sep='\t',header=0,index_col=1)
crc_enriched_taxa = list(crc_enriched.index)

crc_m = crc_m.loc[crc_enriched_taxa]
crc_m = crc_m.astype(float)

#all_m --> relative abundance <= 1e-06 --> crc_m, count zero
for sample in crc_m.columns:
    for species in crc_m.index:
        if all_m[sample][species] <= 1e-06:
            crc_m[sample][species] = 0.0

#crc_m --> relative abundance
for sample in crc_m.columns:
    count_sum = sum(crc_m[sample])

    if count_sum != 0.0:
        crc_m[sample] = crc_m[sample] / count_sum

crc_m = crc_m.T

max_abundance_series = crc_m.max(axis=1)
max_species_series = crc_m.idxmax(axis=1)
species_count_series = (crc_m > 0).sum(axis=1)

assert list(crc_m.index) == list(sample_meta.index)
result = pd.concat([sample_meta,crc_m],axis=1)

result['Max abundance'] = max_abundance_series
result['Species with max abundance'] = max_species_series
result['Species count'] = species_count_series

result.to_csv('crc_dominance.tsv',sep='\t')
