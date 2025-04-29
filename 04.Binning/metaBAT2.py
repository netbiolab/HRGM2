#Python

#first: sample name
#second: assemblr result dir
#third: output_depthfile dir
#fourth: output_bin dir
#fifth: min contig length
#sixth: threads
#seventh: assemblr name [metaspades|megahit]

import sys,os

sample_name = sys.argv[1]
dir_assemblr = sys.argv[2]
dir_depth = sys.argv[3]
dir_bin = sys.argv[4]

minContigLength = sys.argv[5]
if int(minContigLength) < 1500:
	minContigLength = "1500"

thread = sys.argv[6]
assemblr_name = sys.argv[7]

if assemblr_name == "metaspades":
	contig_file = dir_assemblr+"/"+sample_name+"/contigs.fasta"
elif assemblr_name == "megahit":
	contig_file = dir_assemblr+"/"+sample_name+"/"+sample_name+".contigs.fa"
else:
	raise(ValueError)

bin_file = dir_bin+"/"+sample_name+"/"+sample_name+".bin"
depth_file = dir_depth+"/"+sample_name+"/"+sample_name+".depth.txt"

os.system("mkdir "+dir_bin+"/"+sample_name)
os.system("metabat2 -m "+minContigLength+" -t "+thread+" -a "+depth_file+" -i "+contig_file+" -o "+bin_file)
