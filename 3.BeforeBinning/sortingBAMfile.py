#Python

#first: sample name
#second: output_bam dir
#third: output_sortedbam dir
#fourth: thread

import sys
import os

sample_name = sys.argv[1]
dir_bam = sys.argv[2]
dir_sortedbam = sys.argv[3]
thread = sys.argv[4]

os.system("mkdir "+dir_sortedbam+"/"+sample_name)

bam_file = dir_bam+"/"+sample_name+"/"+sample_name+".bam"
sortedbam_file = dir_sortedbam+"/"+sample_name+"/"+sample_name+".sorted.bam"

os.system("samtools sort "+bam_file+" -@ "+thread+" -o "+sortedbam_file)
