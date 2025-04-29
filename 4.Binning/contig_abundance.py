#Python

#first: sample name
#second: output_depthfile dir
#third: output_contig_abundance dir

import os,sys

sample_name = sys.argv[1]
dir_depth = sys.argv[2]
dir_ca = sys.argv[3]

os.system("mkdir "+dir_ca+"/"+sample_name)

depth_file = dir_depth+"/"+sample_name+"/"+sample_name+".depth.txt"
ca_file = dir_ca+"/"+sample_name+"/"+sample_name+".abundance.txt"

os.system("cut -f 1,3 "+depth_file+" | tail -n +2 > "+ca_file)
