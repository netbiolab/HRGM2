#!/usr/bin/env python3

import sys, os, subprocess

gtdbtk_version = subprocess.check_output(['gtdbtk','--version']).decode().strip().split()[2]

if gtdbtk_version != '1.7.0':
    raise(ValueError)

dataset = sys.argv[1]
thread = sys.argv[2]

dir_in = '/nbl/user/mjy1064/3_genome_assembly/3_bin_refinement_QC/4_dataset_total_bins/'+dataset
dir_out = '/nbl/user/mjy1064/3_genome_assembly/5_additional_info/2_GTDB_TK/results/'+dataset
os.mkdir(dir_out)

os.system("gtdbtk classify_wf --genome_dir "+dir_in+" --out_dir "+dir_out+" --cpus "+thread+" --pplacer_cpus "+thread+" -x fa")


