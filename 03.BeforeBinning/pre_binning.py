#!/usr/bin/env python3
#1_indexing ~ 4_sorting

#first: assemble result dir
#second: fastq dir
#third: sample name
#fourth: thread
#fifth: assemblr name [metaspades|megahit]
#sixth: fastq paired t/f 
#seventh: fastq input gzip t/f 

import os,sys
import os.path

assemble_res_dir = sys.argv[1]
fastq_dir = sys.argv[2]
sample_name = sys.argv[3]
thread = sys.argv[4]
assemblr_name = sys.argv[5]
pbool = sys.argv[6]
gzip = sys.argv[7]

if int(thread) <= 0:
    raise(ValueError)

if assemblr_name != "metaspades" and assemblr_name != "megahit":
    raise(ValueError)

if pbool != 't' and pbool != 'f':
    raise(ValueError)

if gzip != 't' and gzip != 'f':
    raise(ValueError)


cohort_name = assemble_res_dir.strip().split('/')[-1]

index_dir = '/nbl/user/mjy1064/3_genome_assembly/2_binning/1_indexing/index/assemblr_' + assemblr_name + "/" + cohort_name
if not os.path.isdir(index_dir):
    os.system("mkdir "+index_dir)
os.system('python3.7 /nbl/user/mjy1064/3_genome_assembly/2_binning/1_indexing/build_contig_index.py '+assemble_res_dir+" "+sample_name+" "+index_dir+" "+thread+" "+assemblr_name)

sam_dir = "/nbl/user/mjy1064/3_genome_assembly/2_binning/2_alignment/output_sam/"+cohort_name
if not os.path.isdir(sam_dir):
    os.system("mkdir "+sam_dir)
os.system("python3.7 /nbl/user/mjy1064/3_genome_assembly/2_binning/2_alignment/align_read_to_contig.py "+sample_name+" "+fastq_dir+" "+index_dir+" "+sam_dir+" "+thread+" "+pbool+" "+gzip)

bam_dir = '/nbl/user/mjy1064/3_genome_assembly/2_binning/3_conversion/output_bam/'+cohort_name
if not os.path.isdir(bam_dir):
    os.system("mkdir "+bam_dir)
os.system("python3.7 /nbl/user/mjy1064/3_genome_assembly/2_binning/3_conversion/SAMtoBAM.py "+sample_name+" "+sam_dir+" "+bam_dir+" "+thread)

sorted_bam_dir = '/nbl/user/mjy1064/3_genome_assembly/2_binning/4_sorting/output_sortedbam/'+cohort_name
if not os.path.isdir(sorted_bam_dir):
    os.system("mkdir "+sorted_bam_dir)
os.system("python3.7 /nbl/user/mjy1064/3_genome_assembly/2_binning/4_sorting/sortingBAMfile.py "+sample_name+" "+bam_dir+" "+sorted_bam_dir+" "+thread)
os.system("python3.7 /nbl/user/mjy1064/3_genome_assembly/2_binning/4_sorting/indexingBAMfile.py "+sample_name+" "+sorted_bam_dir+" "+thread)
