#!/usr/bin/env python3

import os
import sys

sample_name = sys.argv[1]
thread = sys.argv[2]

sample_camisim_out_dir = '../camisim_in_out/{}/out'.format(sample_name)

outfiles = os.listdir(sample_camisim_out_dir)
for outfile in outfiles:
    if os.path.isdir(sample_camisim_out_dir+"/"+outfile) and outfile.endswith('sample_0'):
        tempname = outfile
        break

read_dir = '{}/{}/reads'.format(sample_camisim_out_dir,tempname)

# 1. Decompress
os.system("pigz -d -k -p {} {}/anonymous_reads.fq.gz".format(thread,read_dir))

# 2. Split fastq file to make paired-end reads files
fq = read_dir+"/anonymous_reads.fq"
fq1 = fq[:-2]+"1.fastq"
fq2 = fq[:-2]+"2.fastq"

f_fq = open(fq)
f_fq1 = open(fq1,'w')
f_fq2 = open(fq2,'w')

f_list = ['temp',f_fq1,f_fq2]

while True:
    line1 = f_fq.readline()
    line2 = f_fq.readline()
    line3 = f_fq.readline()
    line4 = f_fq.readline()

    if line1 == '' and line2 == '' and line3 == '' and line4 == '':
        break

    flag = int(line1.strip()[-1])

    f_list[flag].write(line1)
    f_list[flag].write(line2)
    f_list[flag].write(line3)
    f_list[flag].write(line4)
    
f_fq.close()
f_fq1.close()
f_fq2.close()

# 3. Run classifiers

outdir = './classification_outputs/{}'.format(sample_name)
os.mkdir(outdir)

# (1) Kraken2 + Bracken (DB : Rep or Concat) (Confidence : 0.0 or 0.2)
dbtag_to_dbname = {'Rep':'HRGMv2','Concat':'HRGMv2_Concat'}
kraken2_db_dir = '/nbl/user/mjy1064/4_MWAS/1_classification/kraken2/0_kraken_DB_info'

for dbtag in ['Rep','Concat']:
    kraken2_db_path = kraken2_db_dir+"/"+dbtag_to_dbname[dbtag]
    
    for confidence in ['0.0','0.2']:
        outname = '{}__Kraken2_{}__{}'.format(sample_name,dbtag,confidence)

        syslog = outdir+"/"+outname+".log"
       
        rpt = outdir+"/"+outname+".rpt"

        os.system("/usr/bin/time -v -o {} kraken2 --db {} --report {} --threads {} --report-zero-counts --confidence {} --paired {} {}".format(syslog,kraken2_db_path,rpt,thread,confidence,fq1,fq2))
        
        bracken = outdir+"/"+outname+".bracken"
        os.system("/usr/bin/time -v -a -o {} bracken -d {} -i {} -o {} -r 150 -l S1".format(syslog,kraken2_db_path,rpt,bracken))

# (2) Metaphlan4

outname = '{}__Metaphlan4_Marker__None'.format(sample_name)
syslog = outdir+"/"+outname+".log"
bowtie2out = outdir+"/"+outname+".bowtie2out.txt"
metaphlanout = outdir+"/"+outname+".txt"

os.system("/usr/bin/time -v -o {} metaphlan {} --nproc {} --bowtie2out {} -o {} --input_type fastq --unclassified_estimation --bowtie2db /nbl/user/mjy1064/3_genome_assembly/6_new_criteria/11.Marker/4.MetaPhlAn_DB/HRGMv2_MetaPhlAn4_DB --index HRGMv2_MetaPhlAn4_DB".format(syslog,fq,thread,bowtie2out,metaphlanout))


