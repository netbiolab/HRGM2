#!/usr/bin/env python3
import argparse
import os

parser = argparse.ArgumentParser(description='Hifiasm-meta : HiFi assembler')
parser.add_argument('set',help='Set name',metavar='Set name')
parser.add_argument('sample',help='Sample name',metavar='Sample name')
parser.add_argument('--input',default='/nbl/user/mjy1064/0_data/fastq_file/3_After_reference_genome_removal/hifi',help='Input directory (Default : %(default)s)',metavar='DIR')
parser.add_argument('--output',default='/nbl/user/mjy1064/5_long_read_genome_assembly/1_genome_assembly/hifiasm_meta/hifiasm_meta_result',help='Output directory (Default : %(default)s)',metavar='DIR')
parser.add_argument('--threads',default='1',help='# of threads (Default : %(default)s)',metavar='INT')
parser.add_argument('--input-format',default='fastq',choices=['fastq','fasta'],help='Input format [%(choices)s] (Default : %(default)s)',metavar='FORMAT')
parser.add_argument('--gziped',default=False,action='store_true',help='Input file is gziped')
args = parser.parse_args()

in_dir = args.input+"/"+args.set
out_dir = args.output+"/"+args.set
if not os.path.isdir(out_dir):
        os.system("mkdir "+out_dir)
out_dir = out_dir+"/"+args.sample
os.system("mkdir "+out_dir)
sample = in_dir+"/"+args.sample+"."+args.input_format
if args.gziped:
        sample = sample+".gz"

os.system("cd "+out_dir)
os.system("hifiasm_meta -o "+args.sample+" -t "+args.threads+" "+sample+" 2> "+args.sample+".log")
os.system("awk '/^S/{print \">\"$2;print $3}' "+args.sample+".p_ctg.gfa > "+args.sample+".contigs.fasta")
os.system("mv "+args.sample+"* "+out_dir)
