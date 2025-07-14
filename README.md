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
>   assembles quality-controlled reads as contigs using MEGAHIT
> * **hifiasm_meta.py**
>   assembles HiFi reads as contigs using hifiasm-meta

### 03.BeforeBinning
> * **pre_binning.py**
>   is a wrapper that can run the following codes at once
> > * **build_contig_index.py**
> > builds an index to align with contig
> > * **align_read_to_contig.py**
> > aligns reads to contig
> > * **SAMtoBAM.py**
> > converts SAM to BAM 
> > * **sortingBAMfile.py**
> > sorts BAM
> > * **indexingBAMfile.py**
> > indexes sorted BAM

### 04.Binning
> * **binning_pipeline.py**
>   is a wrapper that can run pipelines of MetaBAT2, MaxBin2.0, and CONCOCT at once
> > * **metaBAT2_pipeline.py**
> > is a sub-wrapper that can run codes for binning using MetaBAT2
> > > * **depth_file.py**
> > > generates a depth file from sorted BAM
> > > * **metaBAT2.py**
> > > runs MetaBAT2 for binning from the depth file and contigs
> > * **maxbin2_pipeline.py**
> > is a sub-wrapper that can run codes for binning using MaxBin2.0
> > > * **contig_abundance.py**
> > > generates a contig abundance file from MetaBAT2 depth file
> > > * **maxbin2.py**
> > > runs MaxBin2.0 for binning from the contig abundance file and contigs
> > * **concoct_pipeline.py**
> > is a sub-wrapper that can run codes for binning using CONCOCT
> > > * **cut_contig.py**
> > > cuts contigs into smaller parts
> > > * **coverage_table.py**
> > > generates table with coverage depth information per sample and subcontig
> > > * **concoct.py**
> > > runs CONCOCT for binning from the coverage table and contigs
> > > * **merge_subcontig_clustering.py**
> > > merges subcontig clustering into original contig clustering
> > > * **extract_bin.py**
> > > extracts bins as individual FASTA
> > > * **megahit_bin_change_header.py**
> > > unifies the contig header format of CONCOCT with other binning tools when using MEGAHIT as an assembler
> * **metaWRAP.py**
> combines the binning results from the three tools into a more robust bin set using the bin refinement module of MetaWRAP
> * **gunc_run_sample.py**
> identifies genome chimerism using GUNC

### 05.Dereplication
> * **self_sketch_mash.py**
> calculates the Mash distance between genomes belonging to the same order
> * **mash2cluster_0.1.py**
> performs average-linkage-based hierarchical clustering with a 0.1 cutoff to establish preliminary clusters
> * **animf.py**
> calculates average nucleotide identity (ANI) and coverage for each pair of genomes within each preliminary cluster
> * **ani_results_to_distance_dict.py**
> applies coverage threshold and saves ANI results into a distance dictionary
> * **secondary_clustering.py**
> conducts average-linkage-based hierarchical clustering with an ANI threshold of 95% to cluster genomes at the species level
> * **ani_results_to_distance_dict_cov0.81.py**
> is identical to ani_results_to_distance_dict.py, except that it uses a coverage threshold of 0.81 to remove duplicate genomes
> * **non_redundant_clustering_sample_derep_ver2.py**
> performs average-linkage-based hierarchical clustering within each species cluster to eliminate duplicate genomes

### 06.GenomeAnnotation
> * **gtdbtk_dataset.py**
> runs GTDB-Tk classify_wf to assign GTDB taxonomic annotation to genomes
> * **make_all_run_prokka.py**
> makes a shell script to run Prokka for 230,632 redundant genomes of HRGM2
> * **make_all_run_barrnap.py**
> makes a shell script to run Barrnap for 230,632 redundant genomes of HRGM2
> * **summarize_rRNA.py**
> counts the number of rRNA from Barrnap results
> * **make_all_run_tRNAscanSE.py**
> makes a shell script to run tRNAscan-SE for 230,632 redundant genomes of HRGM2
> * **summarize_tRNA.py**
> counts the number of tRNA from tRNAscan-SE results

### 07.Pangenome
> * **make_panaroo_inputs.py**
> makes input lists to run Panaroo
> * **run_panaroo.py**
> runs Panaroo to construct pan-genomes
> * **make_pangenome_faa.py**
> obtains faa sequences corresponding to pan-genome references
> * **run_eggnog_mapper.py**
> runs eggNOG-mapper for pan-genomes to annotate functions
> * **run_eggnog_mapper_cds_mode.py**
> is identical to run_eggnog_mapper.py, except that it uses fna file of pan-genome and "--itype CDS" option
> * **run_rgi.py**
> runs RGI for pan-genomes to predict antibiotic resistance genes 

### 08.Marker
> * **panaroo_graph_to_node.py**
> obtains nucleotide sequences and amino acid sequences of the pan-genome from the final graph
> * **size_1_node_summary.py**
> is for the same purpose as panaroo_graph_to_node.py, specifically for singleton species
> * **remove_redundancy.py**
> clusters identical proteins together
> * **length_filtering.py**
> extracts protein families with lengths between 150 and 1,500 amino acids
> * **paralog_filtering.py**
> extracts protein families with, on average, less than 1.5 copies per genome
> * **coreness.py**
> computes coreness in a particular species of protein families
> * **coreness_filtering.py**
> performs filtering based on a threshold determined by the size of the species cluster
> * **calc_uniqueness.py**
> calculates the number of species that share a particular protein family
> * **core_uniqueness_filtering.py**
> identifies unique core protein families for each species
> * **make_candidate_reads.py**
> fragments the DNA sequences of the marker candidates into 150 bp segments
> * **make_align_coreness.py**
> calculates coreness based on alignment
> * **find_markers_ver3.py**
> finds species-specific markers based alignment coreness
> * **final_marker_filtering.py**
> selects the top 200 markers, based on uniqueness and length, per species 

### 09.Benchmark
> * **camisim_simulation.py**
> generates simulated samples to compare taxonomic profiling methods
> * **run_classification.py**
> runs various taxonomic profiling methods for simulated samples
> * **computational_resource.py**
> summarizes the elapsed time and maximum RAM for each taxonomic profiling method
> * **summary_classification_evaluation_metrics.py**
> compares predicted results with the answer and calculates precision, recall, and F1 score
> * **merge_metrics_summary.py**
> merges the metric results per sample into one
> * **normalization_size.py**
> summarizes the species sizes for use in length normalization
> * **summary_bray_curtis_similarity.py**
> calculates Bray-Curtis similarity between the predicted profile and the real profile
> * **merge_similarity_summary.py**
> merges the similarity results per sample into one

### 10.ProteinCatalog
> * **prokka_CDS_parsing.py**
> obtains protein sequences from Prokka results
> * **cluster_identical_proteins.py**
> clusters identical proteins together
> * **extract_unique_proteins.py**
> extracts protein sequences from the above clusters
> * **make_cluster_info_file.py**
> makes metadata containing cluster member information for the HRGM2 protein family
> * **update_cluster_info_file.py**
> adds a ‘the number of member proteins’ column to cluster_info.tsv
> * **make_taxonomic_map.py**
> makes metadata containing taxonomy information for the HRGM2 protein family

### 11.GEMs
> * **run_carveme.py**
> runs CarveMe to reconstruct genome-scale metabolic models
> * **search_GEM_info.py**
> calculates the number of metabolites/reactions/gene-associated reactions for GEMs
> * **run_smetana.py**
> runs SMETANA to predict pairwise metabolic interactions for species
> * **calc_comp_pair_prop_taxonomy_rank.py**
> calculates the proportion of cooperative and competitive pairs within the same and across different taxonomic clades
> * **cooperative_order_of_lmi_clades.py**
> calculates cooperative pair proportion between LMI order and other orders
> * **calc_metabolite_dontation_to_LMI.py**
> calculates the association between metabolite supply and the cooperative behavior of species toward LMI orders
> * **community_wise_smetana.py**
> runs SMETANA to get MIP and MRO scores for a disease-associated species community and random communities
> * **species_pair_smetana_score.py**
> calculates the SMETANA score for species pairs within the CD-associated species community
> * **essential_metabolites_from_main_donors.py**
> investigates key metabolites delivered to the receiver species by the two main donors of CD-associated species community
> * **compare_donor_high_low_group.py**
> investigates the relative abundances of receiver species and the abundance group of donor species in the CD samples
> * **summarize_crc_nutritional_requirement_sets.py**
> investigates metabolites commonly required by CRC-associated species from the nutritional requirement set of SMETANA
> * **CRC_dominance_search.py**
> investigates the dominance of species within CRC samples
