#!/usr/bin/env python3

import pickle as pk
import pandas as pd

f_pkl = open('crc_nutritional_requirement_sets.pkl','rb')
d = pk.load(f_pkl)
f_pkl.close()

species_count = len(d.keys())

nutrient_count_dict = dict()

for req_set in d.values():
    for nutrient in req_set:
        if nutrient not in nutrient_count_dict:
            nutrient_count_dict[nutrient] = 1
        else:
            nutrient_count_dict[nutrient] += 1

m = pd.DataFrame.from_dict(nutrient_count_dict, orient='index')

m.index.name = 'BiGG ID'
m.columns = ['Species count']

m['Percentage'] = m['Species count'] / species_count * 100

m = m.sort_values('Species count', ascending=False)

bigg = pd.read_csv('bigg_models_metabolites.txt',sep='\t',header=0,index_col=1)
bigg = bigg[['name']]
bigg = bigg.drop_duplicates()

m['Nutrient'] = bigg['name']
m = m.reset_index().set_index('Nutrient')

m.to_csv('crc_competing_nutrients.tsv',sep='\t')
