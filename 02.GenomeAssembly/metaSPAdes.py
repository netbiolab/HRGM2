# Python

# first: input dir
# second: sample name
# third: output dir
# fourth: thread
# fifth: paired t/f (default = paired)
# sixth: input gzip t/f (default = false)

import os
import sys

indir = sys.argv[1]
inname = sys.argv[2]
outdir = sys.argv[3]
thread = sys.argv[4]
try:
	paired = sys.argv[5]
except:
	paired = "t"

try:
	gzip = sys.argv[6]
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

outdir = outdir + "/" + inname
os.system("mkdir "+outdir)
if pbool:
	if gbool:
		os.system("metaspades.py -1 "+indir+"/"+inname+".1.fastq.gz -2 "+indir+"/"+inname+".2.fastq.gz -t "+thread+" -o "+outdir)
	else:
		os.system("metaspades.py -1 "+indir+"/"+inname+".1.fastq -2 "+indir+"/"+inname+".2.fastq -t "+thread+" -o "+outdir)
else:
	if gbool:
		os.system("metaspades.py -s "+indir+"/"+inname+".fastq.gz -t "+thread+" -o "+outdir)
	else:	
		os.system("metaspades.py -s "+indir+"/"+inname+".fastq -t "+thread+" -o "+outdir)
