## Overview:

Improvements in next generation sequencing has allowed for a large increase in the collection of publicly available genomes. The ability to use these genomes in multiple studies is a very big benefit to researchers, but not all genomes are equal. There are several factors that can assess the quality of these genomes including sequencing depth. Sequencing depth is the number of times a region of a genome is sequenced and is calculated by dividing the total number of bases from reads that align to a genome by the total length of the genome. Research has shown that a greater sequencing depth is important for producing quality assemblies (Rocha et al.). Multiple reads over an area allow for the correction of sequencing errors and greater accuracy. Sequencing at high depths can be costly, so it is important to know how deep sequencing needs to be to achieve a desired goal. 

Comparing the similarity of genomes is a common task in genomic research and can be done many ways. When comparing microbial genomes, alignment is not often used as the occurrence of horizontal gene transfer and genome rearrangement can produce inaccurate results. Instead, other metrics such as average nucleotide identity (ANI) and Mash are used. ANI is an alignment-based metric that only compares orthologous sequences instead of aligning the entire genome. Orthologous sequences can still vary greatly allowing ANI to give useful insight to the relatedness of two genomes. ANI is accurate in comparing draft genomes along with complete genomes. Mash is an alignment-free k-mer based method that is used to compare the approximate distance between genomes. Mash calculates the Jaccard distance by comparing sketches, which are a smaller subset of the full sequence data.  Mash is extremely useful when dealing with large datasets as it is very fast and has shown to produce results that correlate with ANI scores. 

This pipeline will illuminate whether sequencing depth has an impact on ANI and Mash scores. The goal is to simulate genomes with varying sequencing depths for any given SRA file and calculate ANI values and Mash scores at each depth compared to the original genome.  If sequencing depth has no affect, the ANI and Mash scores should reflect that the genomes are the same. The output will show if sequencing depth impacts the accuracy of either and if it does at what level. 

Sources

Rocha U, Kasmanas JC, Toscan R, Sanches DS, Magnusdottir S, et al. (2024) Simulation of 69 microbial communities indicates sequencing depth and false positives are major drivers of bias in prokaryotic metagenome-assembled genome recovery. PLOS Computational Biology 20(10): e1012530.  https://doi.org/10.1371/journal.pcbi.1012530

Jain, C., Rodriguez-R, L.M., Phillippy, A.M. et al. High throughput ANI analysis of 90K prokaryotic genomes reveals clear species boundaries. Nat Commun 9, 5114 (2018). https://doi.org/10.1038/s41467-018-07641-9

Ondov, Brian D et al. “Mash: fast genome and metagenome distance estimation using MinHash.” Genome biology vol. 17,1 132. 20 Jun. 2016, doi:10.1186/s13059-016-0997-x

## Context:

There is no standardized method for assembling a genome, and sequencing depth can impact the 
accuracy and reliability of genomic analysis. Average nucleotide identity (ANI) and Mash scores 
are commonly used to assess genome similarity, yet the impact of sequencing depth on this metrics 
remains unclear. This project aims to evaluate how varying sequencing depths influence ANI and 
Mash scores, and give more clarity on their reliability under these different conditions. 
Understanding this is important, as it will provide researchers with better insight on the 
accuracy of their data and genomic comparisons.

## Goals: 

- Create a reference genome assembly and various read sets at different depth coverages with 
multiple random samples generated of each 

- Users will be able to assess ANI and mesh scores of read sets at different depth coverages in 
comparison with a reference genome assembly. 

- Success will be measured based on compared ANI and mash scores between different read sets of
depth coverage. Higher ANI percentage and a lower mash score indicate a higher assemby
similarity

## Non-goals:

- This project will not focus on optimizing genome assembly parameters past standard settings.

- This project will not compare different genome assemblers. 

- We will not be comparing the ANI and Mash scores to each other. 

- Sequencing depth will not be assessed for evenness throughout the entire genome assembly.



## Proposed Solutions:
1.	Retrieve a user-specified read file when provided an SRR# using SRA toolkit
2.	Evaluate quality of raw reads using FastQC and QC the full set of reads using cutadapt to trim any sequencing adapters
3.	Create the full dataset assembly using SPAdes.
4.	 To determine the sequencing depth of the genome with all of the data, we will utilize SAMtools depth. This will be established as the maximum sequencing depth of the sample
5.	Generate read sets representing different sequencing depths of specified sample using seqTK. Sequencing depths of per 5x coverage to the maximum depth will be analyzed. Five subsample datasets will be created for each sequencing depth to ensure reads are randomly subsampled
6.	Evaluate quality of subsampled raw reads using FastQC and QC the subsample of reads using cutadapt
7.	Assemble each subsampled dataset using SPAdes
8. Utilize FastANI to assess sequence similarity  
    - **a.** Input all assembled genomes with the varying coverage depth which are compared with the reference genome  
    - **b.** Outputs an ANI score, which provides the mean nucleotide identity of orthologous genes shared between two genomes  
9. Utilize Mash to assess sequence similarity  
    - **a.** Input all assembled genomes with the varying coverage depth which are compared with the reference genome  
    - **b.** Outputs a distance metric, the Mash distance, which estimates the mutation rate between two sequences  
10. Further Analysis  
    - **a.** Comparisons between varying depths of coverage  
    - **b.** Comparisons between random subsamples at each depth  
    - **c.** Visualizations of sequence similarities and comparisons 

## Workflow
![image](https://github.com/user-attachments/assets/8cb7825e-5d34-42a8-ac50-94896e68e2e8)

Milestones:

