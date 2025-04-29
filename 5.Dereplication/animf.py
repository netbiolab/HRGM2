#!/usr/bin/env python3

import sys, os

genome1, genome2, genome1_l, genome2_l = sys.argv[1:]

'''
home_dir = '/home/ihgmc/'
tmpout_dir = home_dir+'.mummer_tmp/'
genome1_dir = tmpout_dir + genome1+'/'
os.system('mkdir -p '+genome1_dir)
'''

genome1_name = genome1.split("/")[-1]
genome2_name = genome2.split("/")[-1]

prefix = genome1_name+'___'+genome2_name

delta = prefix+'.delta'
delta_filtered = delta+'.filtered'

command = ['nucmer', '--mum', '-p', prefix , '-c 65 -g 90 -t 1', genome1, genome2]
#print(' '.join(command))
os.system(' '.join(command))
command = ['delta-filter', '-r', '-q', delta, '>', delta_filtered]
#print(' '.join(command))
os.system(' '.join(command))

aln_length, sim_errors = 0, 0
with open(delta_filtered) as f:
	for line in f:
		line = line.strip().split()
		if line[0] == 'NUCMER' or line[0].startswith('>'):
			continue
		if len(line) == 7:
			aln_length += abs(int(line[1]) - int(line[0]))
			sim_errors += int(line[4])

cover1 = float(aln_length) / float(genome1_l)
cover2 = float(aln_length) / float(genome2_l)
try:
	ani = 1.0 - float(sim_errors) / aln_length
except ZeroDivisionError:
	ani = 0
cover = max([cover1, cover2])

os.system("rm "+delta+" "+delta_filtered)
print (genome1_name+'\t'+genome2_name+'\t'+str(ani)+'\t'+str(cover))

