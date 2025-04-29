#!/usr/bin/env python3

import networkx as nx
import pandas as pd
import sys

hrgm = sys.argv[1]

panaroo_dir = '/nbl/user/mjy1064/3_genome_assembly/6_new_criteria/10.Pangenome/panaroo_outputs'
out_dir = './node_summary'

gml = panaroo_dir+"/"+hrgm+"/final_graph.gml"
G = nx.read_gml(gml)
node_dict = dict()
for node in G.nodes.keys():
	node_info = G.nodes[node]
	node_name = '%s|%s'%(hrgm,node_info['name'])
	node_ptn = node_info['protein'].split(';')[0]
	node_dna = node_info['dna'].split(';')[0]
	node_dict[node_name] = {'ptn_sequence':node_ptn, 'dna_sequence':node_dna}
node_df = pd.DataFrame.from_dict(node_dict, orient = 'index')
node_df.to_csv("./node_summary/%s_node.tsv"%hrgm, sep='\t', index=True)
