# HRGM2 Data

## Metadata
### Description
- HRGMv2_Cluster_metadata.tsv : Species-level metadata for the 4,824 HRGMv2 clusters (e.g., taxonomy, genome quality, etc.)
- Dereplication_genomes_metadata.tsv : Metadata for all 230,632 genomes used prior to dereplication
- HRGMv2_gtdbr220_results.tsv : GTDB r220-based taxonomic assignments for the 4,824 HRGMv2 species
### Zenodo DOI
<https://doi.org/10.5281/zenodo.19480672>

---
## GEMs
### Description
- Genome-scale metabolic models (GEMs, in XML format) reconstructed for all non-redundant genomes in HRGMv2.
- GEM reconstruction failed for the following four genomes due to unknown reasons: (GENOME087726 in HRGMv2_0709, GENOME205746 in HRGMv2_3350, GENOME226109 in HRGMv2_3524, GENOME227506 in HRGMv2_3550)
### Zenodo DOI
<https://doi.org/10.5281/zenodo.19482535>

---
## Representative genomes
### Description
- Genome sequences (FASTA format) for 4,824 HRGMv2 representative genomes (one per species)
### Zenodo DOI
<https://doi.org/10.5281/zenodo.19482781>

---
## Pangenomes
### Description
- Pangenome data for all 4,824 species, structured as follows:
1. For Multi-genome species (2,639 species)
  
   : Species with more than one non-redundant genome. Each folder contains the full output of Panaroo v1.3.0. (Refer to the Panaroo GitHub for detailed file descriptions.)
   - combined_DNA_CDS.fasta.gz
   - combined_protein_CDS.fasta.gz
   - combined_protein_cdhit_out.txt
   - combined_protein_cdhit_out.txt.clstr
   - final_graph.gml
   - gene_data.csv.gz
   - gene_presence_absence.csv
   - gene_presence_absence.Rtab
   - gene_presence_absence_roary.csv
   - pan_genome_reference.fa – nucleotide sequences
   - pan_genome_reference.faa – amino acid sequences
   - pre_filt_graph.gml
   - struct_presence_absence.Rtab
   - summary_statistics.txt
   - emapper_results/ – eggNOG-mapper results for pan_genome_reference.fa
   - rgi_results/ - RGI results for pan_genome_reference.fa


2. For Single-genome species (2,185 species)

   : Species with only one non-redundant genome. Pangenomes were generated directly from the representative genome, including:
   - pan_genome_reference.fa – nucleotide sequences
   - pan_genome_reference.faa – amino acid sequences
   - emapper_results/ – eggNOG-mapper results for pan_genome_reference.fa
   - rgi_results/ – RGI results results for pan_genome_reference.fa
     
### Zenodo DOI
This dataset has been split. 
- Part 1: <https://doi.org/10.5281/zenodo.19483642>
- Part 2: <https://doi.org/10.5281/zenodo.19487814>
- Part 3: <https://doi.org/10.5281/zenodo.19489118>
- Part 4: <https://doi.org/10.5281/zenodo.19489530>
- Part 5: <https://doi.org/10.5281/zenodo.19490162>
- Part 6: <https://doi.org/10.5281/zenodo.19490766>
- Part 7: <https://doi.org/10.5281/zenodo.19491184>
- Part 8: <https://doi.org/10.5281/zenodo.19492155>
- Part 9: <https://doi.org/10.5281/zenodo.19496353>
- Part 10: <https://doi.org/10.5281/zenodo.19508753>

To reconstruct, ```cat HRGMv2_Pangenomes.part_* > HRGM2_Pangenomes.tar.gz```

---
## 16S_rRNA
### Description
- 16S_presence_absence.tsv : Presence/absence table indicating whether a 16S rRNA sequence was predicted for each of the 4,824 HRGMv2 species (based on Barrnap results)
- 16S_rRNA_library.fasta : FASTA file containing the predicted 16S rRNA DNA sequences for species with detected 16S rRNA (subset of HRGMv2 species)
- 16S_rRNA_report.tsv : Summary statistics per HRGMv2 species cluster, including: number of predicted 16S rRNA sequences, length of the longest 16S rRNA sequence (in base pairs), and percentage of full-length 16S rRNA sequence 

### Zenodo DOI
<https://doi.org/10.5281/zenodo.19483551>

---
## MetaPhlAn4_DB
### Description
- MetaPhlAn4-compatible custom database for HRGMv2 species (HRGMv2_MetaPhlAn4_DB/ : Indexed Bowtie2 database folder for MetaPhlAn4 analysis)
- (Usage) metaphlan commands with  ```--bowtie2db HRGMv2_MetaPhlAn4_DB (downloaded database folder) --index HRGMv2_MetaPhlAn4_DB```
### Zenodo DOI
<https://doi.org/10.5281/zenodo.19483953>

---
## Kraken2_Rep_DB
### Description
- Custom taxonomy database compatible with Kraken2 and Bracken
- Database built using a single representative sequence per species
- (Usage) kraken2 commands with ```--db HRGMv2_Rep (downloaded database folder)```
### Zenodo DOI
<https://doi.org/10.5281/zenodo.19492246>

---
## Kraken2_Concat_DB
### Description
- Custom taxonomy database compatible with Kraken2 and Bracken
- Database built using concatenated sequences per species
- (Usage) kraken2 commands with ```--db HRGMv2_Concat (downloaded database folder)```
### Zenodo DOI
This dataset has been split. 
- Part 1: <https://doi.org/10.5281/zenodo.19508916>
- Part 2: <https://doi.org/10.5281/zenodo.19508925>

To reconstruct, ```cat HRGMv2_Kraken2_Concat_DB.part_* > HRGM2_Kraken2_Concat_DB.tar.gz```

---
## Nonredundant genomes
### Description
- Final set of 155,211 dereplicated genomes used to define HRGMv2 species
### Zenodo DOI
This dataset has been split. 
- Part 1: <https://doi.org/10.5281/zenodo.19496139>
- Part 2: <https://doi.org/10.5281/zenodo.19499800>
- Part 3: <https://doi.org/10.5281/zenodo.19501013>

To reconstruct, ```cat Nonredundant_genomes.part_* > HRGM2_Nonredundant_genomes.tar.gz```

---
## Redundant genomes
### Description
- Genome sequences of 230,632 input genomes (prior to dereplication)
### Zenodo DOI
This dataset has been split. 
- Part 1: <https://doi.org/10.5281/zenodo.19501855>
- Part 2: <https://doi.org/10.5281/zenodo.19502700>
- Part 3: <https://doi.org/10.5281/zenodo.19503297>
- Part 4: <https://doi.org/10.5281/zenodo.19504199>
- Part 5: <https://doi.org/10.5281/zenodo.19505035>

To reconstruct, ```cat Redundant_genomes.part_* > HRGM2_Redundant_genomes.tar.gz```

---
## Proteins
### Description
1.HRGMv2_Unique_Proteins/ : Unique protein sequences after redundancy removal
- HRGMv2_Unique_Proteins_rep_seq.faa.gz : Representative sequences for unique CDS sequences (amino acid, faa)
- HRGMv2_Unique_Proteins.cluster_info.updated.tsv.gz : Cluster info for Unique proteins
- HRGMv2_Unique_Proteins.taxonomic_map.tsv.gz : Taxonomy info for Unique proteins

2.HRGMv2_{identity}_Proteins/ : Clustered protein catalogs at 100%, 95%, 90%, 70%, and 50% identity thresholds
- HRGMv2_{identity}_Proteins_rep_seq.faa.gz : Representative sequences {identity}% protein families (amino acid, faa)
- HRGMv2_{identity}_Proteins_cluster.tsv.gz : Cluster info for {identity}% protein families (representative sequences - member)
- HRGMv2_{identity}_Proteins.cluster_info.updated.tsv.gz : Cluster info for {identity}% protein families
- HRGMv2_{identity}_Proteins.taxonomic_map.tsv.gz : Taxonomy info for {identity}% protein families
- emapper_results : eggNOG-mapper results for {identity}% proteins families
- deepgoplus_results : deepgoplus results for 90% protein families (after filtering)
### Zenodo DOI
This dataset has been split. 
- Part 1: <https://doi.org/10.5281/zenodo.19534052>
- Part 2: <https://doi.org/10.5281/zenodo.19534058>

To reconstruct, ```cat HRGMv2_Proteins.part_* > HRGM2_Proteins.tar.gz```

---
## CAZymes
### Description
- Output of run_dbcan v4.1.4 (standalone version of dbCAN3). CAZyme families were annotated from 155,211 non-redundant genomes.
### Zenodo DOI
This dataset has been split. 
- Part 1: <https://doi.org/10.5281/zenodo.19547966>
- Part 2: <https://doi.org/10.5281/zenodo.19547970>
- Part 3: <https://doi.org/10.5281/zenodo.19547972>
- Part 4: <https://doi.org/10.5281/zenodo.19547975>

To reconstruct, ```cat 2.HRGMv2_CAZymes.part_* > HRGM2_CAZymes.tar.gz```

---
## Defense systems
### Description
- Output of DefenseFinder for genome-resolved detection of bacterial defense systems.
### Zenodo DOI
<https://doi.org/10.5281/zenodo.19550803>
