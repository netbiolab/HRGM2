#!/usr/bin/env python3

import sys,os

hrgm = sys.argv[1]
thread = sys.argv[2]

input_file = './panaroo_inputs/{}.panaroo_input.list'.format(hrgm)
output_dir = './panaroo_outputs/{}'.format(hrgm)
os.mkdir(output_dir)

os.system('panaroo -i {} -o {} -t {} --clean-mode strict -c 0.90 -f 0.5 --merge_paralogs --core_threshold 0.90'.format(input_file,output_dir,thread))
