#!/usr/bin/env python3

import sys, os

hrgm = sys.argv[1]
thread = sys.argv[2]

input_file = "./panaroo_outputs/{}/pan_genome_reference.fa".format(hrgm)
out_dir = './panaroo_outputs/{}/emapper_results'.format(hrgm)
os.mkdir(out_dir)

os.system("emapper.py -i {} -o {} --output_dir {} --cpu {} --data_dir /dev/shm/eggnog_data --itype CDS".format(input_file,hrgm,out_dir,thread))
