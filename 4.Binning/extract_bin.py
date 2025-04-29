#Python

#first: sample name
#second: assemblr result dir
#third: output_merged_clustering dir
#fourth: output_bin dir
#fifth: assemblr name [metaspades|megahit]

import os,sys

sample_name = sys.argv[1]
dir_assemblr = sys.argv[2]
dir_merged = sys.argv[3]
dir_bin = sys.argv[4]
assemblr_name = sys.argv[5]

if assemblr_name == "metaspades":
	contig = dir_assemblr+"/"+sample_name+"/contigs.fasta"
elif assemblr_name == "megahit":
	contig = dir_assemblr+"/"+sample_name+"/"+sample_name+".contigs.fa"
else:
	raise(ValueError)

merged = dir_merged+"/"+sample_name+"/"+sample_name+".clustering_merged.csv"
out_bin = dir_bin+"/"+sample_name

os.system("mkdir "+dir_bin+"/"+sample_name)
os.system("extract_fasta_bins.py "+contig+" "+merged+" --output_path "+out_bin) 
