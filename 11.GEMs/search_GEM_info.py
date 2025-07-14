#!/usr/bin/env python3

from cobra.io import read_sbml_model
import os

model_path = '/nbl/vault3/home/wjkim/2022/gem/finished_xml'
xml_list = sorted(os.listdir(model_path))

f_out = open('all_GEM_info.tsv','w')
f_out.write('Genome\t# Metabolites\t# Reactions\t# Gene-associated reactions\n')

i = 1

for xml in xml_list:
    genome = xml.split('.')[0]
    model = read_sbml_model(f'{model_path}/{xml}')
    
    num_metabolites = len(model.metabolites)
    num_reactions = len(model.reactions)
    num_gene_associated_reactions = len([rxn for rxn in model.reactions if rxn.gene_reaction_rule]) 

    f_out.write(f'{genome}\t{num_metabolites}\t{num_reactions}\t{num_gene_associated_reactions}\n')

    if i % 100 == 0:
        print(f'Writing {i}th model ...')

    i += 1

f_out.close()


