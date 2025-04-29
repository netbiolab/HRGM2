#!/usr/bin/env python3

# Update : Add 'Count of member proteins' column

import sys

d = sys.argv[1]
n, name = d.split('.')

f_in = open(f'./{d}/{name}.cluster_info.tsv')
f_out = open(f'./{d}/{name}.cluster_info.updated.tsv','w')

for line in f_in:
    rep, members = line.strip().split()
    count = len(members.split(';'))
    
    f_out.write(f'{rep}\t{count}\t{members}\n')

f_in.close()
f_out.close()
