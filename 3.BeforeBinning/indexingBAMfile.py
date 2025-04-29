#Python

#first: sample name
#second: output_sortedbam dir
#third: thread

import sys,os

sample_name = sys.argv[1]
dir_sortedbam = sys.argv[2]
thread = sys.argv[3]

bam_file = dir_sortedbam+"/"+sample_name+"/"+sample_name+".sorted.bam"

os.system("samtools index "+bam_file+" -@ "+thread)
