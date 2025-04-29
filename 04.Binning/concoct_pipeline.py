#!/usr/bin/env python3
#1_cut_contig ~ 5_extract_bin_as_fasta

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

bed_dir = '/nbl/user/mjy1064/3_genome_assembly/2_binning/5_binning/3_concoct/1_cut_contig/output_bed/'+cohort_name
contig_part_dir = '/nbl/user/mjy1064/3_genome_assembly/2_binning/5_binning/3_concoct/1_cut_contig/output_contig_part_fasta/'+cohort_name
if not os.path.isdir(bed_dir):
    os.system("mkdir "+bed_dir)
if not os.path.isdir(contig_part_dir):
    os.system("mkdir "+contig_part_dir)
os.system("python3.7 /nbl/user/mjy1064/3_genome_assembly/2_binning/5_binning/3_concoct/1_cut_contig/cut_contig.py "+sample_name+" "+assemble_res_dir+" "+bed_dir+" "+contig_part_dir+" "+assemblr_name)

sorted_bam_dir = '/nbl/user/mjy1064/3_genome_assembly/2_binning/4_sorting/output_sortedbam/'+cohort_name
coverage_table_dir = '/nbl/user/mjy1064/3_genome_assembly/2_binning/5_binning/3_concoct/2_coverage_table/output_coverage_table/'+cohort_name
if not os.path.isdir(coverage_table_dir):
    os.system("mkdir "+coverage_table_dir)
os.system("python3.7 /nbl/user/mjy1064/3_genome_assembly/2_binning/5_binning/3_concoct/2_coverage_table/coverage_table.py "+sample_name+" "+bed_dir+" "+sorted_bam_dir+" "+coverage_table_dir)

concoct_dir = '/nbl/user/mjy1064/3_genome_assembly/2_binning/5_binning/3_concoct/3_run_concoct/output_concoct/'+cohort_name
if not os.path.isdir(concoct_dir):
    os.system("mkdir "+concoct_dir)
os.system("python3.7 /nbl/user/mjy1064/3_genome_assembly/2_binning/5_binning/3_concoct/3_run_concoct/concoct.py "+sample_name+" "+contig_part_dir+" "+coverage_table_dir+" "+concoct_dir+" "+min_contig_len+" "+thread)

merged_dir = '/nbl/user/mjy1064/3_genome_assembly/2_binning/5_binning/3_concoct/4_merge/output_merged_clustering/'+cohort_name
if not os.path.isdir(merged_dir):
    os.system("mkdir "+merged_dir)
os.system("python3.7 /nbl/user/mjy1064/3_genome_assembly/2_binning/5_binning/3_concoct/4_merge/merge_subcontig_clustering.py "+sample_name+" "+bed_dir+" "+concoct_dir+" "+merged_dir)

bin_dir = '/nbl/user/mjy1064/3_genome_assembly/2_binning/5_binning/3_concoct/5_extract_bin_as_fasta/output_genome/'+cohort_name
if not os.path.isdir(bin_dir):
    os.system("mkdir "+bin_dir)
os.system("python3.7 /nbl/user/mjy1064/3_genome_assembly/2_binning/5_binning/3_concoct/5_extract_bin_as_fasta/extract_bin.py "+sample_name+" "+assemble_res_dir+" "+merged_dir+" "+bin_dir+" "+assemblr_name)

if assemblr_name == "megahit":
    os.system("python3.7 /nbl/user/mjy1064/3_genome_assembly/2_binning/5_binning/3_concoct/5_extract_bin_as_fasta/megahit_bin_change_header.py "+sample_name+" "+bin_dir)
