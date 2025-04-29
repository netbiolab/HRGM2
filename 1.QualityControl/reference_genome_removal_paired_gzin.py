#Python
#Paired mode, gzip input

#first: human genome reference index file name
#second: sample name
#third: input dir
#fourth: output dir
#fifth: thread
#sixth: gzip result t/f

import sys,os

index_file_name = sys.argv[1]
sample_name = sys.argv[2]
dir_in = sys.argv[3]
dir_out = sys.argv[4]
thread = sys.argv[5]
gzip = sys.argv[6]

if gzip == "t":
    gzip_bool = True
elif gzip == "f":
    gzip_bool = False
else:
    raise(ValueError)

fastq_1 = dir_in+"/"+sample_name+".1.fastq.gz"
fastq_2 = dir_in+"/"+sample_name+".2.fastq.gz"

if gzip_bool:
    out_file = dir_out+"/"+sample_name+".%.fastq.gz"
    os.system("bowtie2 --threads "+thread+" --un-conc-gz "+out_file+" -x "+index_file_name+" -1 "+fastq_1+" -2 "+fastq_2)
else:
    out_file = dir_out+"/"+sample_name+".%.fastq"
    os.system("bowtie2 --threads "+thread+" --un-conc "+out_file+" -x "+index_file_name+" -1 "+fastq_1+" -2 "+fastq_2)
