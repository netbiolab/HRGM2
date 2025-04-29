#Python

#first: assemble result dir
#second: sample name
#third: output dir
#fourth: thread
#fifth: assemblr name [metaspades|megahit]

import sys
import os

result_dir = sys.argv[1]
sample_name = sys.argv[2]
out_dir = sys.argv[3]
thread = sys.argv[4]
assemblr_name = sys.argv[5]

out_dir = out_dir+"/"+sample_name

if assemblr_name == "metaspades":
	contig = result_dir+"/"+sample_name+"/contigs.fasta"
elif assemblr_name == "megahit":
	contig = result_dir+"/"+sample_name+"/"+sample_name+".contigs.fa"
else:
	raise(ValueError)

index_name = out_dir+"/"+sample_name+"_index"

os.system("mkdir "+out_dir)
os.system("bowtie2-build -q --threads "+thread+" "+contig+" "+index_name)

