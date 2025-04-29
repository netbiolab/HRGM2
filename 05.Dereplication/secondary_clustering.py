#!/usr/bin/env python3

import pickle as pk
import pandas as pd
import fastcluster
from scipy.cluster.hierarchy import cut_tree
from itertools import combinations
import os

def comb2(N):
    return int(N*(N-1)/2)

file_list = []

m = pd.read_csv("all_order.mash_cluster0.1",sep='\t',header=None,index_col=None)
m = m[m[1] != 1]
m = m.reset_index()

f_dict = open('genome_pair_distance_dict.p','rb')
distance_dict = pk.load(f_dict)
f_dict.close()

result_dir = './cluster_files'

cutoff = 0.05

for pri_cluster in m.index:
    genome_list = m[2][pri_cluster].split(";")
    genome_list.sort()

    genome2index_dict = dict()
    for index,genome in enumerate(genome_list):
        genome2index_dict[genome] = index

    for test in genome_list:
        if genome_list[genome2index_dict[test]] != test:
            raise(ValueError)

    n = len(genome_list)
    if n != m[1][pri_cluster]:
        raise(ValueError)

    distance_array = [-1] * comb2(n)

    comb_list = list(combinations(genome_list,2))
    for tup in comb_list:
        genome1 = tup[0]
        genome2 = tup[1]

        distance = distance_dict[genome1][genome2]

        i = genome2index_dict[genome1]
        j = genome2index_dict[genome2]
        
        assert i < j

        da_i = comb2(n) - comb2(n-i) + (j-i-1)

        distance_array[da_i] = distance

    if -1 in distance_array:
        raise(ValueError)

    z = fastcluster.linkage(distance_array, method='average', preserve_input=False)
    cutree = cut_tree(z, height = cutoff)

    f_cluster = open(result_dir+"/primary_cluster_{}.cluster0.05".format(pri_cluster),"w")
    file_list.append(result_dir+"/primary_cluster_{}.cluster0.05".format(pri_cluster)) 
   
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


os.system("cat "+" ".join(file_list)+" > all_secondary_clusters.tsv")
