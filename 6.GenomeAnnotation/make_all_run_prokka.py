#!/usr/bin/env python3

import pandas as pd

m = pd.read_csv("../Dereplication_genomes_metadata.tsv",sep='\t',header=0,index_col=0)

f = open("all_run_prokka.sh","w")

for genome in m.index:
    fa = '../5.Dereplication/0.Dereplication_genomes/'+m['Original name'][genome]+".fa"
    kingdom = m['Domain'][genome].split("__")[-1]
    f.write('prokka --outdir ./prokka_results/{} --prefix {} --locustag {} --kingdom {} --cpus 3 {}\n'.format(genome,genome,genome,kingdom,fa))

f.close()
