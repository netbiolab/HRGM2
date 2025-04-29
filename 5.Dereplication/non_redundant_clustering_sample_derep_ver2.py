#!/usr/bin/env python3

import math
import pickle as pk
import pandas as pd
import fastcluster
from scipy.cluster.hierarchy import cut_tree
from itertools import combinations
import os

def comb2(N):
    return int(N*(N-1)/2)


'''
m = pd.read_csv("all_order.mash_cluster0.1",sep='\t',header=None,index_col=None)
m = m[m[1] != 1]
m = m.reset_index()
'''

m = pd.read_csv("../3.Nucmer_results/HRGMv2_Cluster_metadata_ori.tsv",sep='\t',header=0,index_col=0)
m = m[m['# of Genomes'] != 1]

f_dict = open('../3.Nucmer_results/genome_pair_distance_dict_cov0.81.p','rb')
distance_dict = pk.load(f_dict)
f_dict.close()

result_dir = './cluster_results'

cutoff = 0.001

genome_meta = pd.read_csv("../../Dereplication_genomes_metadata.tsv",sep='\t',header=0,index_col=1)

for hrgm_cluster in m.index:
    #genome_list = m[2][pri_cluster].split(";")
    genome_list = m['Genomes'][hrgm_cluster].split(";")

    ####### UPDATE ########## NEW genome_list (sample derep)
    remove_list = []
    hrgm_genome_meta = genome_meta[genome_meta['HRGMv2 cluster'] == hrgm_cluster]
    
    assert set(genome_list) == set(hrgm_genome_meta.index)

    sample_group = hrgm_genome_meta.groupby('Sample')
    for sample,group in sample_group:
        if len(group) == 1:
            continue

        ##### UPDATE2 #####
        dataset_list = list(set(group['Data set']))
        assert len(dataset_list) == 1
        dataset = dataset_list[0]

        if dataset != 'HRGM v1':
            continue

        ###################

        dup_list = list(group.index)
        
        rep_genome = ''
        max_score = -1

        for g in dup_list:
            gscore = group['Completeness'][g] - 5 * group['Contamination'][g] + 0.5 * math.log10(group['N50'][g])

            if gscore > max_score:
                rep_genome = g
                max_score = gscore

        dup_list.remove(rep_genome)
        remove_list.extend(dup_list)

    for rm_genome in remove_list:
        genome_list.remove(rm_genome)

    if len(genome_list) == 1:
        print(hrgm_cluster+"\t"+genome_list[0])
        continue        

    ##########################

    genome_list = [x+".fa" for x in genome_list] 
    genome_list.sort()

    genome2index_dict = dict()
    for index,genome in enumerate(genome_list):
        genome2index_dict[genome] = index

    for test in genome_list:
        if genome_list[genome2index_dict[test]] != test:
            raise(ValueError)

    n = len(genome_list)
    #if n != m['# of Genomes'][hrgm_cluster]:
    #    raise(ValueError)

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

    f_cluster = open(result_dir+"/{}.cluster0.001".format(hrgm_cluster),"w")
   
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


