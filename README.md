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

## R Packages
+ ggplot2
+ stringr

## Pipeline Functionality 
1. wrapper.py
   - Calls all scripts in pipeline given an input SRR number  
2. sratoolkit.py
   - Uses prefetch and fasterq dump to download SRA file and convert to paired end fastq read files
   - Assembles the reads using SPAdes to create a fasta file 
3. bt2.py
   - This script is used to calculate the sequencing depth for the assembly 
   - bowtie2 creates an index and maps the reads to the assembly outputting a sam file
   - samtools converts the sam to a sorted bam
   - samtools depth calculates the sequencing depth at every nucleotide position
4. seq_depth_subsamples.py
   - Given the average sequencing depth this script generates paired end fastq files simulating various read coverages
   - seqtk pulls a given number of reads (that represents a percentage of the full reads) from the full fastq files to simulate each specific depth (starting at 5x going up by steps of 5 until average depth of full assembly is reached)
   - Each coverage is simulated 3 times to ensure accurate representation of the genome
5. assembly.py
   - All simulated read datasets are assembled using SPAdes
6. fastani-mash.py
   - Each subset assembly is compared with the full genome assembly to calculate the ANI and Mash score
   - Outputs two tables, one for each scoring metric
7. visuals.R
   - Takes the tables with scoring metrics to create plots to compare bewtween the different coverage subsets
   - Outputs a directory with comparison plot images

## Testing The Pipeline
In order to test the pipeline, we have already preset a SRR file to use and shortened the number of reads so that the max coverage is 15. The SRR used in the test code is `SRR32805580`. This allows us to skip the bowtie2 step to determine the maximum coverage. It also reduces the number of assemblies that need to be made. 

In order to run the test script, you will call the script (no input needed):
```bash
python wrapper_test.py
```




