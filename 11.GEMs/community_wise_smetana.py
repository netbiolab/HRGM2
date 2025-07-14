#!/usr/bin/env python3

import sys
import os
import pandas as pd
import random

disease = sys.argv[1]
Disease = disease.upper()

disease_enriched_list = sorted(list(pd.read_csv(f'{disease}_enriched_taxa.tsv',sep='\t',header=0,index_col=0).index))
community_size = len(disease_enriched_list)

prevalent_taxa_list = sorted(list(pd.read_csv('/nbl/user/mjy1064/3_genome_assembly/6_new_criteria/18.GEM/smetana_analysis/prevalent_species/prevalence_top_1000_species.list',sep='\t',header=None,index_col=0).index))

f_tsv = open(f'{disease}_community_composition.tsv','w')
f_tsv.write('Community\tSpecies list\n')

outdir = f'./{disease}_community'
os.mkdir(outdir)

model_dir = '../HRGMv2_rep_model_sbml'

def hrgm_list_to_model_list_string(hrgm_list):
    new_list = [f'{model_dir}/{hrgm}.xml' for hrgm in hrgm_list]
    return ' '.join(new_list)

# 1. Disease enriched community --> SMETANA
model_list_string = hrgm_list_to_model_list_string(disease_enriched_list)
os.system(f'smetana {model_list_string} -o {outdir}/{Disease}_Enriched --flavor bigg -g --molweight')
f_tsv.write('{}_Enriched\t{}\n'.format(Disease, ';'.join(disease_enriched_list)))

# 2. Random X 100 --> SMETANA
for i in range(1,101):
    name_tag = 'RANDOM'+'0'*(3-len(str(i))) + str(i)
    random.shuffle(prevalent_taxa_list)
    random_list = prevalent_taxa_list[:community_size]
    random_list.sort()
    
    model_list_string = hrgm_list_to_model_list_string(random_list)
    os.system(f'smetana {model_list_string} -o {outdir}/{name_tag} --flavor bigg -g --molweight')

    f_tsv.write('{}\t{}\n'.format(name_tag, ';'.join(random_list)))

f_tsv.close()
