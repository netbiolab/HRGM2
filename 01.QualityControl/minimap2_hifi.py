#!/usr/bin/env python3
import argparse
import os

parser = argparse.ArgumentParser(description='Reference genome removal for hifi reads using Minimap2')
parser.add_argument("set",help="Set name",metavar="SET NAME")
parser.add_argument("sample",help="Sample name",metavar='SAMPLE NAME')
parser.add_argument("--input",default='/nbl/user/mjy1064/0_data/fastq_file/2_After_trimming/hifi',help='Input directory (Default: %(default)s)',metavar='DIR')
parser.add_argument("--output",default='/nbl/user/mjy1064/0_data/fastq_file/3_After_reference_genome_removal/hifi',help='Output directory (Default: %(default)s)',metavar='DIR')
parser.add_argument("--ref",default='/nbl/user/mjy1064/0_data/fasta_file/human_genome_ref_GRCh38.p13/human_genome_ref.fa',help='Referance genome fasta file (Default: %(default)s)',metavar='FASTA')
parser.add_argument("--threads",default='1',help='# of threads (Default: %(default)s)',metavar='INT')
args = parser.parse_args()

# Variable setting
sample_fastq = args.input+"/"+args.set+"/"+args.sample+".fastq"
out_sam = args.input+"/"+args.set+"/"+args.sample+".sam"
out_dir = args.output+"/"+args.set
if not os.path.isdir(out_dir):
    os.system("mkdir "+out_dir)
out_fastq = out_dir+"/"+args.sample+".fastq"

# Minimap 2
os.system("minimap2 -ax asm20 "+args.ref+" "+sample_fastq+" -t "+args.threads+" > "+out_sam)

# Make fastq file removed referance mapped read
# 1) SAM parsing to make a set that consists of referance genome mapped read
remove_count = 0
sam_header = ['@HD','@SQ','@RG','@PG','@CO']
ref_mapped_reads = set()
f_sam = open(out_sam)
for line in f_sam:
    line = line.strip()
    tokens = line.split("\t")
    if tokens[0] in sam_header:
        continue
    
    read_name = tokens[0]
    flag = tokens[2]
    if flag != '*': # Reference genome mapped read
        ref_mapped_reads.add(read_name)

f_sam.close()
removed_read_num = len(ref_mapped_reads)

# 2) Make fastq file removed reference mapped read
f_in = open(sample_fastq)
f_out = open(out_fastq,"w")
total_read_num = 0

while True:
    # Per Read
    line1 = f_in.readline()
    line2 = f_in.readline()
    line3 = f_in.readline()
    line4 = f_in.readline()
    
    if line1 == '' and line2 == '' and line3 == '' and line4 == '':
        break

    total_read_num += 1
    read_name = line1.strip()[1:]
    if read_name in ref_mapped_reads:
        continue
    else:
        f_out.write(line1)
        f_out.write(line2)
        f_out.write(line3)
        f_out.write(line4)

f_in.close()
f_out.close()
# os.system("rm "+out_sam)

print("Total read num : {}".format(total_read_num))
print("Survived read num : {}".format(total_read_num - removed_read_num))
print("Removed read num : {}".format(removed_read_num))
print("{} % survived".format( (total_read_num - removed_read_num) / total_read_num * 100))
