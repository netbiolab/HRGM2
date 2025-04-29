#!/usr/bin/env python3

#Assemblr: Megahit
#first: sample name
#second: output_bin dir

import sys,os

sample_name = sys.argv[1]
dir_bin = sys.argv[2]

sample_list = os.listdir(dir_bin)
sample_exist = False
for sample in sample_list:
        if sample == sample_name:
                sample_exist = True
                break

if not sample_exist:
        raise(ValueError)

indir = dir_bin+"/"+sample_name

for b in os.listdir(indir):
        pb = indir+"/"+b
        f_in = open(pb)

        nb = indir+"/new_"+b
        f_new = open(nb,'w')

        for line in f_in:
                if '>' in line:
                        f_new.write(line.split(' ')[0]+'\n')
                else:
                        f_new.write(line)

        f_in.close()
        f_new.close()

        os.system("rm "+pb)
        os.system("mv "+nb+" "+pb)

