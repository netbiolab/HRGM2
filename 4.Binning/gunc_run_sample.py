#!/usr/bin/env python3

#first: sample name
#second: input dir (.gz is also possible)
#third: output dir
#fourth: thread

import sys,os

sample_name = sys.argv[1]
in_dir = sys.argv[2]
out_dir = sys.argv[3]
thread = sys.argv[4]

arb_genome = os.listdir(in_dir)[0]
ext = arb_genome.split(".")[-1]
ext = "."+ext

out_dir = out_dir+"/"+sample_name
os.system("mkdir "+out_dir)
os.system("gunc run -d "+in_dir+" -e "+ext+" -o "+out_dir+" -t "+thread)
