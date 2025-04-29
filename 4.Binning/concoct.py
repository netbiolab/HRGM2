#Python

#first: sample name
#second: output_contig_part_fasta dir
#third: output_coverage_table dir
#fourth: output_concoct dir
#fifth: min contig length
#sixth: threads

import os,sys

sample_name = sys.argv[1]
dir_cpf = sys.argv[2]
dir_ct = sys.argv[3]
dir_cc = sys.argv[4]
minContigLength = sys.argv[5]
thread = sys.argv[6]

os.system("mkdir "+dir_cc+"/"+sample_name)

cpf = dir_cpf+"/"+sample_name+"/"+sample_name+"_contigs_10K.fa"
ct = dir_ct+"/"+sample_name+"/"+sample_name+".coverage_table.tsv"
cc = dir_cc+"/"+sample_name+"/"
pf = dir_cc+"/"+sample_name+"/"+sample_name+".print.txt"

os.system("concoct -t "+thread+" -l "+minContigLength+" --composition_file "+cpf+" --coverage_file "+ct+" -b "+cc+" > "+pf)
