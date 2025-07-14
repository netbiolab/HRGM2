#!/usr/bin/env python3

import sys
import os

genome = sys.argv[1]
outdir = sys.argv[2]

faa = f'/nbl/user/mjy1064/3_genome_assembly/6_new_criteria/7.Protein_catalog/0.redundant_CDS/prokka_CDS/{genome}/{genome}.faa'
xml = f'{outdir}/{genome}.xml'

os.system(f'carve {faa} --output {xml}')
