#Python

#first: sample name
#second: assemblr result dir
#third: output_contig_abundance dir
#fourth: output_bin dir
#fifth: min contig length
#sixth: threads
#seventh: assemblr name [metaspades|megahit]

import os,sys

sample_name = sys.argv[1]
dir_assemblr = sys.argv[2]
dir_ca = sys.argv[3]
dir_bin = sys.argv[4]
minContigLength = sys.argv[5]
thread = sys.argv[6]
assemblr_name = sys.argv[7]

if assemblr_name == "metaspades":
	contig = dir_assemblr+"/"+sample_name+"/contigs.fasta"
elif assemblr_name == "megahit":
	contig = dir_assemblr+"/"+sample_name+"/"+sample_name+".contigs.fa"
else:
	raise(ValueError)

abundance_file = dir_ca+"/"+sample_name+"/"+sample_name+".abundance.txt"
out_bin = dir_bin+"/"+sample_name+"/"+sample_name+".bin"
print_file = dir_bin+"/"+sample_name+"/"+sample_name+".print.txt"

os.system("mkdir "+dir_bin+"/"+sample_name)
os.system("run_MaxBin.pl -contig "+contig+" -abund "+abundance_file+" -thread "+thread+" -out "+out_bin+" -min_contig_length "+minContigLength+" > "+print_file)
