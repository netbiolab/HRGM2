#Python

#first: sample name
#second: assemblr result
#third: output_bed dir
#fourth: output_contig_part_fasta dir
#fifth: assemblr name [metaspades|megahit]

import os,sys

sample_name = sys.argv[1]
dir_assemblr = sys.argv[2]
dir_bed = sys.argv[3]
dir_cpf = sys.argv[4]
assemblr_name = sys.argv[5]

if assemblr_name == "metaspades":
	contig = dir_assemblr+"/"+sample_name+"/contigs.fasta"
elif assemblr_name == "megahit":
	contig = dir_assemblr+"/"+sample_name+"/"+sample_name+".contigs.fa"
else:
	raise(ValueError)

bed = dir_bed+"/"+sample_name+"/"+sample_name+"_contigs_10K.bed"
cpf = dir_cpf+"/"+sample_name+"/"+sample_name+"_contigs_10K.fa"

os.system("mkdir "+dir_bed+"/"+sample_name)
os.system("mkdir "+dir_cpf+"/"+sample_name)
os.system("cut_up_fasta.py "+contig+" -c 10000 -o 0 --merge_last -b "+bed+" > "+cpf)
