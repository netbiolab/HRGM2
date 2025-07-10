# HRGM2 Code
This repository contains code used for HRGM2 construction.

## Code description
### 01.QualityControl
> * **trimmomatic_PE.py**
>   removes the adapter sequences and low-quality bases of Illumina sequencing samples
> * **reference_genome_removal_paired_gzin.py**
>   aligns sample reads against the human reference genome and removes the aligned reads as human contaminants
> * **minimap2_hifi.py**
>   removes human contaminants from PacBio HiFi sequencing samples

### 02.GenomeAssembly
> * **metaSPAdes.py**
>   assembles quality-controlled reads as contigs using metaSPAdes
> * **megahit.py**
>   assembles quality-controlled reads as contigs using megahit

### 03.BeforeBinning
> * **pre_binning.py**
>   is a wrapper that can run the following codes at once
> * **build_contig_index.py**
>   builds an index to align with contig
> * **align_read_to_contig.py**
>   aligns reads to contig
> * **SAMtoBAM.py**
>   converts SAM to BAM 
> * **sortingBAMfile.py**
>   sorts BAM
> * **indexingBAMfile.py**
>   indexes sorted BAM

### 04.Binning
### 05.Dereplication
### 06.GenomeAnnotation
### 07.Pangenome
### 08.Marker
### 09.Benchmark
### 10.ProteinCatalog
