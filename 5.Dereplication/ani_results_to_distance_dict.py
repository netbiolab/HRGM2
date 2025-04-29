#!/usr/bin/env python3

import pickle as pk

f_in = open('ani_all_results.tsv')
f_out = open("genome_pair_distance_dict.p",'wb')
d = dict() #d[genome1][genome2] = distance

cov_threshold = 0.6

for line in f_in:
    genome1,genome2,ani,cover = line.strip().split()
    ani = float(ani)
    cover = float(cover)
    
    if cover < cov_threshold:
        ani = float(0)

    distance = 1 - ani
    if not (0<= distance <= 1):
        raise(ValueError)

    l = [genome1,genome2]
    l.sort()

    if l[0] not in d:
        d[l[0]] = dict()
        d[l[0]][l[1]] = distance
    else:
        d[l[0]][l[1]] = distance

f_in.close()
pk.dump(d,f_out)
f_out.close()
 
