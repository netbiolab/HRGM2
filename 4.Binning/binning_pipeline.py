#!/usr/bin/env python3
#Binning : MetaBAT2, Maxbin2, Concoct

#first: sample name
#second: assemblr result dir
#third: min contig length
#fourth: thraed
#fifth: assemblr name [metaspades|megahit]

import sys,os

sample_name = sys.argv[1]
assemble_res_dir = sys.argv[2]
min_contig_len = sys.argv[3]
thread = sys.argv[4]
assemblr_name = sys.argv[5]

if int(min_contig_len) <= 0:
    raise(ValueError)

if int(thread) <= 0:
    raise(ValueError)

if assemblr_name != "metaspades" and assemblr_name != "megahit":
    raise(ValueError)

parameter = sample_name+" "+assemble_res_dir+" "+min_contig_len+" "+thread+" "+assemblr_name

os.system("python3.7 /nbl/user/mjy1064/3_genome_assembly/2_binning/5_binning/1_metaBAT2/metaBAT2_pipeline.py "+parameter)
os.system("python3.7 /nbl/user/mjy1064/3_genome_assembly/2_binning/5_binning/2_maxbin2/maxbin2_pipeline.py "+parameter)
os.system("python3.7 /nbl/user/mjy1064/3_genome_assembly/2_binning/5_binning/3_concoct/concoct_pipeline.py "+parameter)

