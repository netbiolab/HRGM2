#!/usr/bin/env python3

import pandas as pd
import os

result_df = pd.DataFrame(columns=['Sample','Classification method','Time (min)','Max RAM (GB)'],index=list(range(300)))
i = 0

sample_list = os.listdir("./classification_outputs")
sample_list.sort()

for sample in sample_list:
	sample_dir = './classification_outputs/{}'.format(sample)
	
	logfiles = [x for x in os.listdir(sample_dir) if x.endswith('.log')]
	logfiles.sort()

	for logfile in logfiles:
		method = logfile[logfile.find('__')+2:logfile.rfind('.')]
		
		time_list = []
		ram_list = []

		f = open(sample_dir+"/"+logfile)
		for line in f:
			line = line.strip()
			
			if line.startswith('Elapsed (wall clock) time (h:mm:ss or m:ss)'):
				minute,second = line.split()[-1].split(":")
				minute = float(minute)
				second = float(second)
				time = minute + second/60
				time_list.append(time)

			elif line.startswith('Maximum resident set size (kbytes)'):
				kb = int(line.split()[-1])
				gb = kb * 1e-6
				ram_list.append(gb)

		f.close()

		total_time = sum(time_list)
		max_ram = max(ram_list)

		result_df.loc[i] = [sample,method,total_time,max_ram]
		i += 1


result_df.to_csv('computational_resource.tsv',sep='\t')
