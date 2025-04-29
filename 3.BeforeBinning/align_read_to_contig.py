#Python

#first: sample name
#second: fastq dir
#thrid: index dir
#fourth: output dir
#fifth: thread
#sixth: paired t/f (default = paired)
#seventh: input gzip t/f (default = false)

import os
import sys

sample_name = sys.argv[1]
fastq_dir = sys.argv[2]
index_dir = sys.argv[3]
output_dir = sys.argv[4]
thread = sys.argv[5]

try:
        paired = sys.argv[6]
except:
        paired = "t"

try:
        gzip = sys.argv[7]
except:
        gzip = "f"

if paired == "t":
        pbool = True
elif paired == "f":
        pbool = False
else:
        raise(ValueError)

if gzip == "t":
        gbool = True
elif gzip == "f":
        gbool = False
else:
        raise(ValueError)

os.system("mkdir "+output_dir+"/"+sample_name)

out_sam = output_dir+"/"+sample_name+"/"+sample_name+".sam"
fastq_1 = fastq_dir+"/"+sample_name+".1.fastq"
fastq_2 = fastq_dir+"/"+sample_name+".2.fastq"
fastq = fastq_dir+"/"+sample_name+".fastq"
idx = index_dir+"/"+sample_name+"/"+sample_name+"_index"

if pbool:
	if gbool:
		os.system("bowtie2 --threads "+thread+" -1 "+fastq_1+".gz"+" -2 "+fastq_2+".gz"+" -x "+idx+" -S "+out_sam+" --very-sensitive")
	else:
		os.system("bowtie2 --threads "+thread+" -1 "+fastq_1+" -2 "+fastq_2+" -x "+idx+" -S "+out_sam+" --very-sensitive")
else:
	if gbool:
		os.system("bowtie2 --threads "+thread+" -U "+fastq+".gz"+" -x "+idx+" -S "+out_sam+" --very-sensitive")
	else:	
		os.system("bowtie2 --threads "+thread+" -U "+fastq+" -x "+idx+" -S "+out_sam+" --very-sensitive")
