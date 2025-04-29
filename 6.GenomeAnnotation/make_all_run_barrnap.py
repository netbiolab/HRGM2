#!/usr/bin/env python3

import pandas as pd

m = pd.read_csv("../Dereplication_genomes_metadata.tsv",sep='\t',header=0,index_col=0)

f = open("all_run_barrnap.sh","w")

for genome in m.index:
	fa = '../5.Dereplication/0.Dereplication_genomes/'+m['Original name'][genome]+".fa"
	kingdom = m['Domain'][genome].split("__")[-1][:3].lower()
	tag = m['Domain'][genome].split("__")[-1][:4].lower()
	filename = './barrnap_results/{}/{}.barrnap.1e-04.{}'.format(genome,genome,tag)
	f.write('barrnap --kingdom {} --threads 3 --evalue 1e-04 --outseq {}.fa {} > {}.tsv\n'.format(kingdom,filename,fa,filename))

f.close()
