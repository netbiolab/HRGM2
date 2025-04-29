#!/usr/bin/env python3

#first: sample name
#second: output_bin dir (metaBAT2)
#third: output_bin dir (maxbin2)
#fourth: output_bin dir (concoct)
#fifth: output_bin_refinement dir
#sixth: threads

import os,sys
sample_name = sys.argv[1]
dir_metabat2 = sys.argv[2] + "/" + sample_name
dir_maxbin2 = sys.argv[3] + "/" + sample_name
dir_concoct = sys.argv[4] + "/" + sample_name
dir_bin_ref = sys.argv[5] + "/" + sample_name
thread = sys.argv[6]

def remove_non_fasta(_name):
        _files = os.listdir(_name)
        for _file in _files:
                if not (_file.endswith('.fa') or _file.endswith('.fasta')):
                        os.system('rm '+_name+'/'+_file)


remove_non_fasta(dir_metabat2)
remove_non_fasta(dir_maxbin2)
remove_non_fasta(dir_concoct)

os.system("metawrap bin_refinement -t "+thread+" -m 40 -c 50 -o "+dir_bin_ref+" -A "+dir_metabat2+" -B "+dir_maxbin2+" -C "+dir_concoct)
