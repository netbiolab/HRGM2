#!/usr/bin/env python3

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import gridspec

matplotlib.rcParams['pdf.fonttype'] = 42

m = pd.read_csv('detailed.tsv',sep='\t',header=0,index_col=None)

main_donors = ['HRGMv2_1765','HRGMv2_1879']
m = m[m['donor'].isin(main_donors)]

mus_threshold = 0.9
m = m[m['mus'] > mus_threshold]

donor_summary_list = []

for donor in main_donors:
    series = m[m['donor'] == donor]['compound'].value_counts()
    series = series.rename(donor)
    donor_summary_list.append(series)

result = pd.concat(donor_summary_list, axis=1)
result = result.fillna(0.0)
result = result.astype(int)

result.index.name = 'Compound'
result = result.reset_index()

def bigg_id(df):
    return df['Compound'][2:-2]

result['BIGG ID'] = result.apply(bigg_id,axis=1)

bigg = pd.read_csv('bigg_models_metabolites.txt',sep='\t',header=0,index_col=1)
bigg = bigg[['name']]
bigg = bigg.drop_duplicates()

result['Name'] = result['BIGG ID'].map(bigg['name'])

# Manually convert compound name
result = result.set_index('Name')
result = result.rename(index={'Copper':'Cu2+', 'L-alanine-D-glutamate-meso-2,6-diaminoheptanedioate-D-alanine':'LalaDgluMdapDala', 'Sulfur':'S', 'Fe2+ mitochondria':'Fe2+'})
result = result.reset_index()

# Amino acid annotation
amino_acid_set = {'L-Leucine', 'L-Valine', 'L-Arginine', 'L-Glutamate', 'L-Methionine', 'L-Tryptophan', 'L-Tyrosine', 'L-Phenylalanine', 'L-Threonine', 'L-Lysine', 'L-Isoleucine', 'L-Cysteine', 'L-Serine'}

def is_AA(df):
    return 'Amino acids' if df['Name'] in amino_acid_set else 'Others'

result['Type'] = result.apply(is_AA,axis=1)

# Sorting
result['Sum'] = result['HRGMv2_1765'] + result['HRGMv2_1879']
result = result.sort_values(by=['Sum','Type'], ascending=[False,True])

# Saving
result = result.set_index('Name')
result = result[['Type','BIGG ID','Compound','HRGMv2_1765','HRGMv2_1879','Sum']]
result = result.rename(columns={'HRGMv2_1765':'Klebsiella pneumoniae', 'HRGMv2_1879':'Pseudescherichia sp002298805'})

result.to_csv('cd_essential_metabolites_from_main_donors.tsv',sep='\t')
