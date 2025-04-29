#!/usr/bin/env python3

import sys
import subprocess
import os

mash_version = subprocess.check_output(['mash','--version']).decode().strip()

if mash_version != '2.3':
    raise(ValueError)

order = sys.argv[1]
thread = sys.argv[2]

genome_dir = '/nbl/user/mjy1064/3_genome_assembly/6_new_criteria/5.Dereplication/1.Genomes_by_order/'+order
out_dir = '/nbl/user/mjy1064/3_genome_assembly/6_new_criteria/5.Dereplication/2.Mash_results'

#1. Make input list
input_file = out_dir+"/"+order+".list"
f = open(input_file,"w")
genomes = os.listdir(genome_dir)
genomes.sort()

for g in genomes:
    f.write(genome_dir+"/"+g+"\n")

f.close()

#2. Sketch
sketch_file = out_dir+"/"+order
os.system("mash sketch -p {} -s 10000 -o {} -l {}".format(thread,sketch_file,input_file))
sketch_file = sketch_file+".msh"

#3. Calculate mash distance
result_file = out_dir+"/"+order+".result"
os.system("mash dist -p {} -s 10000 {} {} > {}".format(thread,sketch_file,sketch_file,result_file))
