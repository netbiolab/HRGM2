#!/usr/bin/env python3

import pandas as pd

m = pd.read_csv("../Dereplication_genomes_metadata.tsv",sep='\t',header=0,index_col=0)

f = open("all_run_tRNAscanSE.sh","w")

for genome in m.index:
	fa = '../5.Dereplication/0.Dereplication_genomes/'+m['Original name'][genome]+".fa"
	option = '-'+m['Domain'][genome].split("__")[-1][0]
	tag = m['Domain'][genome].split("__")[-1][:4].lower()
	filename = './tRNAscanSE_results/{}/{}.tRNAscanSE.{}'.format(genome,genome,tag)
	f.write('tRNAscan-SE {} -Q -o {}.tsv -m {}.summary --thread 3 {}\n'.format(option,filename,filename,fa))

f.close()
