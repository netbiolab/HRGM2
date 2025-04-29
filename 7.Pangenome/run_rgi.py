#!/usr/bin/env python3

import sys, os

hrgm = sys.argv[1]
ext = sys.argv[2]
thread = sys.argv[3]

if ext not in ['faa','fa']:
	raise(ValueError)

i = './panaroo_outputs/{}/pan_genome_reference.{}'.format(hrgm,ext)
o = './panaroo_outputs/{}/rgi_results/{}.rgi'.format(hrgm,hrgm)

command = 'rgi main -i {} -o {} -n {} --clean '.format(i,o,thread)

if ext == 'fa':
	command += '--split_prodigal_jobs'
elif ext == 'faa':
	command += '-t protein'
	os.mkdir('./panaroo_outputs/{}/rgi_results'.format(hrgm))
else:
	raise(ValueError)

os.system(command)
