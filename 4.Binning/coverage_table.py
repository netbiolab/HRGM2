#Python

#first: sample name
#second: output_bed dir
#third: output_sortedbam dir (.bai file should exist in same dir)
#fourth: output_coverage_table dir

import os,sys

sample_name = sys.argv[1]
dir_bed = sys.argv[2]
dir_sortedbam = sys.argv[3]
dir_coverage_table = sys.argv[4]

os.system("mkdir "+dir_coverage_table+"/"+sample_name)

bed = dir_bed+"/"+sample_name+"/"+sample_name+"_contigs_10K.bed"
sortedbam = dir_sortedbam+"/"+sample_name+"/"+sample_name+".sorted.bam"
ct = dir_coverage_table+"/"+sample_name+"/"+sample_name+".coverage_table.tsv"

os.system("concoct_coverage_table.py "+bed+" "+sortedbam+" > "+ct)
