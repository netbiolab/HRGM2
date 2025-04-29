#!/usr/bin/env python3

#first: sample name
#second: set name
#third: thread

import sys,os,os.path

sample_name = sys.argv[1]
set_name = sys.argv[2]
thread = sys.argv[3]

bin_metaBAT2_dir = '/nbl/user/mjy1064/3_genome_assembly/2_binning/5_binning/1_metaBAT2/2_binning/output_genome/'+set_name
bin_maxbin2_dir = '/nbl/user/mjy1064/3_genome_assembly/2_binning/5_binning/2_maxbin2/2_binning/output_genome/'+set_name
bin_concoct_dir = '/nbl/user/mjy1064/3_genome_assembly/2_binning/5_binning/3_concoct/5_extract_bin_as_fasta/output_genome/'+set_name

bin_ref_dir = '/nbl/user/mjy1064/3_genome_assembly/3_bin_refinement_QC/0_output_bin_refinement/'+set_name

if not os.path.isdir(bin_ref_dir):
	os.system("mkdir "+bin_ref_dir)

os.system("python3 /nbl/user/mjy1064/3_genome_assembly/3_bin_refinement_QC/1_bin_refinement/metaWRAP.py "+sample_name+" "+bin_metaBAT2_dir+" "+bin_maxbin2_dir+" "+bin_concoct_dir+" "+bin_ref_dir+" "+thread)
