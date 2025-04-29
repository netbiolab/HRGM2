#!/usr/bin/env python3
#Trimmomatic PE

#first: sample name
#second: raw fastq dir
#third: after trimming fastq dir
#fourth: adapter sequence
#fifth: thread
#sixth: output gzip [t/f]

import os, sys
import os.path

sample_name = sys.argv[1]
raw_fastq_dir = sys.argv[2]
after_fastq_dir = sys.argv[3]
adapter = sys.argv[4]
thread = sys.argv[5]
out_gzip = sys.argv[6]

if out_gzip == "t":
    gzip = True
elif out_gzip == "f":
    gzip = False
else:
    raise(ValueError)

cohort_name = raw_fastq_dir.strip().split('/')[-1]
out_log_sum_dir = '/nbl/user/mjy1064/1_trimming/trimmomatic/output_log_summary/'+cohort_name
if not os.path.isdir(out_log_sum_dir):
    os.system("mkdir "+out_log_sum_dir)

out_log_sum_dir += ("/"+sample_name)
os.system("mkdir "+out_log_sum_dir)

log = out_log_sum_dir+"/"+sample_name+".log"
summary = out_log_sum_dir+"/"+sample_name+".summary"

raw_list = os.listdir(raw_fastq_dir)
fastq1 = ""
fastq2 = ""
for f in raw_list:
    if sample_name in f and ".1.fastq" in f:
        fastq1 = f
    elif sample_name in f and ".2.fastq" in f:
        fastq2 = f

if fastq1 == "" or fastq2 == "":
    raise(ValueError)

in_fastq1 = raw_fastq_dir+"/"+fastq1
in_fastq2 = raw_fastq_dir+"/"+fastq2

out_fastq1 = after_fastq_dir+"/"+sample_name+".1.fastq"
out_fastq2 = after_fastq_dir+"/"+sample_name+".2.fastq"
if gzip:
    out_fastq1 += ".gz"
    out_fastq2 += ".gz"

out_fastq1_singlet = out_log_sum_dir+"/"+sample_name+".singlet.1.fastq.gz"
out_fastq2_singlet = out_log_sum_dir+"/"+sample_name+".singlet.2.fastq.gz"

os.system('trimmomatic PE -threads '+thread+" -phred33 -trimlog "+log+" -summary "+summary+" "+in_fastq1+" "+in_fastq2+" "+out_fastq1+" "+out_fastq1_singlet+" "+out_fastq2+" "+out_fastq2_singlet+" ILLUMINACLIP:"+adapter+":2:30:7 LEADING:5 TRAILING:5 SLIDINGWINDOW:4:5 MINLEN:36")

