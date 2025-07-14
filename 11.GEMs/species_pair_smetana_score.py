#!/usr/bin/env python3

import pandas as pd

result = pd.read_csv('detailed.tsv',sep='\t',header=0,index_col=None)
cd_enriched = pd.read_csv('cd_enriched_taxa.tsv',sep='\t',header=0,index_col=0)

m = result.copy()

def pair_index(df):
    return df['receiver']+' <- '+df['donor']

m['Index'] = m.apply(pair_index,axis=1)
m = m.set_index('Index')
m = m[['receiver','donor']]
m = m.drop_duplicates()

m['receiver (taxa)'] = m['receiver'].map(cd_enriched['Scientific name'])
m['donor (taxa)'] = m['donor'].map(cd_enriched['Scientific name'])

def smetana_score(df):
    receiver = df['receiver']
    donor = df['donor']

    score = sum(result[(result['receiver'] == receiver) & (result['donor'] == donor)]['smetana'])

    return score

m['smetana'] = m.apply(smetana_score,axis=1)

m.to_csv('cd_species_pair_smetana_score.tsv',sep='\t') 
