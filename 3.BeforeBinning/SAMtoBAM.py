#Python

#first: sample name
#second: output_sam dir
#third: output_bam dir
#fourth: threads

import sys
import os

sample_name = sys.argv[1]
dir_sam = sys.argv[2]
dir_bam = sys.argv[3]
thread = sys.argv[4]

os.system("mkdir "+dir_bam+"/"+sample_name)

sam_file = dir_sam+"/"+sample_name+"/"+sample_name+".sam"
bam_file = dir_bam+"/"+sample_name+"/"+sample_name+".bam"

os.system("samtools view -@ "+thread+" -bS "+sam_file+" > "+bam_file)
