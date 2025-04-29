#!/usr/bin/env python3
# cutoff 0.2 --> 0.1
# outname cluster0.1

import sys, fastcluster
from scipy.cluster.hierarchy import cut_tree

def comb2(N):
    return int(N*(N-1)/2)

order = sys.argv[1]

cutoff = 0.1
d = '/nbl/user/mjy1064/3_genome_assembly/6_new_criteria/5.Dereplication/2.Mash_results'

genome_list = []
genome2index_dict = dict()

f_list = open(d+"/"+order+".list")
for i,line in enumerate(f_list):
    genome_name = line.strip().split("/")[-1]
    genome_list.append(genome_name)
    genome2index_dict[genome_name] = i
f_list.close()

n = len(genome_list)
distance_array = [-1] * comb2(n)

f_mash = open(d+"/"+order+".result")
for line in f_mash:
    genome1,genome2,distance,p,overlap = line.strip().split("\t")
    genome1 = genome1.split("/")[-1]
    genome2 = genome2.split("/")[-1]
    distance = float(distance)

    i = genome2index_dict[genome1]
    j = genome2index_dict[genome2]
    if not (i < j):
        continue
    
    da_i = comb2(n) - comb2(n-i) + (j-i-1)

    distance_array[da_i] = distance

f_mash.close()

if -1 in distance_array:
    raise(ValueError)

z = fastcluster.linkage(distance_array, method='average', preserve_input=False)
cutree = cut_tree(z, height = cutoff)

f_cluster = open(d+"/"+order+".cluster0.1","w")
cluster2genomes = dict()
for idx in range(n):
    cluster = cutree[idx][0]
    try:
        cluster2genomes[cluster].append(genome_list[idx])
    except KeyError:
        cluster2genomes[cluster] = [genome_list[idx]]

clusters = list(cluster2genomes.keys())
clusters.sort()

for cluster in clusters:
    genomes = cluster2genomes[cluster]
    f_cluster.write(str(cluster)+'\t'+str(len(genomes))+'\t'+';'.join(genomes)+"\n")

f_cluster.close()
