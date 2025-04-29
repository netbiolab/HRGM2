#Python

#first: sample name
#second: output_bed dir
#third: output_concoct dir
#fourth: output_merged_clustering dir

import os,sys

sample_name = sys.argv[1]
dir_bed = sys.argv[2]
dir_cc = sys.argv[3]
dir_merged = sys.argv[4]

bed = dir_bed+"/"+sample_name+"/"+sample_name+"_contigs_10K.bed"
cc = dir_cc+"/"+sample_name+"/clustering_gt1000.csv"
merged = dir_merged+"/"+sample_name+"/"+sample_name+".clustering_merged.csv"

os.system("mkdir "+dir_merged+"/"+sample_name)
os.system("python3.7 /nbl/user/mjy1064/3_genome_assembly/2_binning/5_binning/3_concoct/4_merge/merge_cutup_clustering_custom.py "+bed+" "+cc+" > "+merged)
