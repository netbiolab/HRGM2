#!/usr/bin/env python3

import os,sys

hrgm_1 = sys.argv[1]
hrgm_2 = sys.argv[2]

model_dir = '/nbl/vault3/user/mjy1064/3_genome_assembly/6_new_criteria/18.GEM/smetana_analysis/HRGMv2_rep_model_sbml'

hrgm_1_model = f'{model_dir}/{hrgm_1}.xml'
hrgm_2_model = f'{model_dir}/{hrgm_2}.xml'

output_name = f'{hrgm_1}__{hrgm_2}'

output_dir = f'/nbl/vault3/user/mjy1064/3_genome_assembly/6_new_criteria/18.GEM/smetana_analysis/smetana_output/{hrgm_1}'

if not os.path.isdir(output_dir):
    os.mkdir(output_dir)

os.system(f'smetana {hrgm_1_model} {hrgm_2_model} -o {output_dir}/{output_name} --flavor bigg -g --molweight')
