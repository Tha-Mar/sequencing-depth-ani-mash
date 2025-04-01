# sequencing-depth-ani-mash  
How does sequencing depth affect ANI and MASH scores? Project by Umar Siddiqui, Lila Nelson, and Jerrin John.  

## Project Overview
Analyzing how sequencing depth affects genome similarity metrics, specifically ANI and Mash distance. By simulating different sequencing depths, we evaluate their impact on accuracy and reliability. This study helps assess potential biases in genome comparisons due to varying coverage levels.  
__For and in depth explanation of the project see Design_Doc.md__

## Dependencies  
+ [FastQC](https://github.com/s-andrews/FastQC)
+ [SRA Toolkit](https://github.com/ncbi/sra-tools/wiki/01.-Downloading-SRA-Toolkit)
+ [cutadapt](https://github.com/marcelm/cutadapt/)
+ [SPAdes](https://github.com/ablab/spades)
+ [seqtk](https://github.com/lh3/seqtk)
+ [bowtie2](https://github.com/BenLangmead/bowtie2)
+ [samtools](https://github.com/samtools/samtools)
+ [FastANI](https://github.com/ParBLiSS/FastANI)
+ [MASH](https://github.com/marbl/Mash)

## Python Packages
+ os
+ subprocess
+ sys
+ glob
+ argparse
+ SeqIO

## Pipeline Functionality 
1. wrapper.py
   - calls all scripts in pipeline given an input SRR number  
2. sratoolkit.py
   - uses prefetch and fasterq dump to download SRA file and convert to paired end fastq read files
   - assembles the reads using SPAdes to create a fasta file 
3. bt2.py
   - this script is used to calculate the sequencing depth for the assembly 
   - bowtie2 creates an index and maps the reads to the assembly outputting a sam file
   - samtools converts the sam to a sorted bam
   - samtools depth calculates the sequencing depth at every nucleotide position
4. seq_depth_subsamples.py
   - given the average sequencing depth this script generates paired end fastq files simulating various read coverages
   - seqtk pulls a given number of reads (that represents a percentage of the full reads) from the full fastq files to simulate each specific depth (starting at 5x going up by steps of 5 until average depth of full assembly is reached)
   - each coverage is simulated 3 times to ensure accurate representation of the genome
5. assembly.py
   - all simulated read datasets are assembled using SPAdes 

