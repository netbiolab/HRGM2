#!/usr/bin/env python3
#1_contig_abundance ~ 2_binning

#first: sample name
#second: assemblr result dir
#third: min contig length
#fourth: thraed
#fifth: assemblr name [metaspades|megahit]

import os,sys
import os.path

sample_name = sys.argv[1]
assemble_res_dir = sys.argv[2]
min_contig_len = sys.argv[3]
thread = sys.argv[4]
assemblr_name = sys.argv[5]

if int(min_contig_len) <= 0:
    raise(ValueError)

if int(thread) <= 0:
    raise(ValueError)

if assemblr_name != "metaspades" and assemblr_name != "megahit":
    raise(ValueError)

cohort_name = assemble_res_dir.strip().split('/')[-1]

depth_dir = '/nbl/user/mjy1064/3_genome_assembly/2_binning/5_binning/1_metaBAT2/1_depth/output_depthfile/'+cohort_name
contig_abundance_dir = '/nbl/user/mjy1064/3_genome_assembly/2_binning/5_binning/2_maxbin2/1_contig_abundance/output_contig_abundance/'+cohort_name
if not os.path.isdir(contig_abundance_dir):
    os.system("mkdir "+contig_abundance_dir)
os.system("python3.7 /nbl/user/mjy1064/3_genome_assembly/2_binning/5_binning/2_maxbin2/1_contig_abundance/contig_abundance.py "+sample_name+" "+depth_dir+" "+contig_abundance_dir)

bin_dir = '/nbl/user/mjy1064/3_genome_assembly/2_binning/5_binning/2_maxbin2/2_binning/output_genome/'+cohort_name
if not os.path.isdir(bin_dir):
    os.system("mkdir "+bin_dir)
os.system("python3.7 /nbl/user/mjy1064/3_genome_assembly/2_binning/5_binning/2_maxbin2/2_binning/maxbin2.py "+sample_name+" "+assemble_res_dir+" "+contig_abundance_dir+" "+bin_dir+" "+min_contig_len+" "+thread+" "+assemblr_name)
