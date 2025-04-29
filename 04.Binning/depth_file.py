#Python

#first: sample name
#second: output_sortedbam dir
#third: output_depthfile dir
#fourth: min contig length

import sys,os

sample_name = sys.argv[1]
dir_sortedbam = sys.argv[2]
dir_depthfile = sys.argv[3]
minContigLength = sys.argv[4]

sortedbam_file = dir_sortedbam+"/"+sample_name+"/"+sample_name+".sorted.bam"
depth_file = dir_depthfile+"/"+sample_name+"/"+sample_name+".depth.txt"

os.system("mkdir "+dir_depthfile+"/"+sample_name)
os.system("jgi_summarize_bam_contig_depths --outputDepth "+depth_file+" --minContigLength "+minContigLength+" --minContigDepth 1 "+sortedbam_file)
