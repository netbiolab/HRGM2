#!/usr/bin/env python3

f = open("../0.Pangenome_gene_summary/Total_sequence_ptn.tsv")

ptn_gene_dict = dict()

f.readline()
for line in f:
	hrgmgene,protein = line.strip().split()
	
	if protein not in ptn_gene_dict:
		ptn_gene_dict[protein] = [hrgmgene]
	else:
		ptn_gene_dict[protein].append(hrgmgene)

f.close()

test = 0
for valuelist in ptn_gene_dict.values():
	test += len(valuelist)
assert test == 14381080

# Writing
f_cluster = open('unique_protein.cluster_info.tsv','w')
f_fasta = open('unique_proteins.faa','w')

for protein_sequence,member_list in ptn_gene_dict.items():
	rep = member_list[0]
	
	f_cluster.write(rep+"\t"+";".join(member_list)+"\n")
	
	f_fasta.write('>'+rep+"\n")
	f_fasta.write(protein_sequence+"\n")

f_cluster.close()
f_fasta.close()	
