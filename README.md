# HRGM2 Code
This repository contains code used for HRGM2 construction.

## Code description
### 01.QualityControl
> * **trimmomatic_PE.py**   
>   : removes the adapter sequences and low-quality bases of Illumina sequencing samples
> * **reference_genome_removal_paired_gzin.py**
>   : aligns sample reads against the human reference genome and removes the aligned reads as human contaminants
> * **minimap2_hifi.py**
>   : removes human contaminants from PacBio HiFi sequencing samples

### 02.GenomeAssembly
> * **metaSPAdes.py**
>   : assembles quality-controlled reads as contigs
> 
### 03.BeforeBinning
### 04.Binning
### 05.Dereplication
### 06.GenomeAnnotation
### 07.Pangenome
### 08.Marker
### 09.Benchmark
### 10.ProteinCatalog
