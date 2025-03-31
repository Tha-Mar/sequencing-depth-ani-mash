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

