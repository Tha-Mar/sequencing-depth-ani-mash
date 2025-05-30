import os
import argparse
import sys

#function to parse command line arguments
def check_arg(args=None):
    parser = argparse.ArgumentParser(description='input location of data directory')
    parser.add_argument('-i', '--input', help='path to input data',required ='True') #add command line arguement for input file
    return parser.parse_args(args)

#retrieve command line arguments and assign to variables
args = check_arg(sys.argv[1:])
infile = args.input #store input file path

# setting the SRR accession number so this functions for any input
SRR = infile

#create directory for fastq files 
os.makedirs('../fastq-data-'+SRR,exist_ok=True) 
fastq_filepath = '../fastq-data-'+SRR


# creating a directory for bowtie2 output
os.system('mkdir ../bt2-'+SRR)

# creating the commands for building the bowtie2 index and for using that index to map the reads
bowtie2_index = 'bowtie2-build ../spades-out-'+SRR+'/contigs.fasta ../bt2-'+SRR+'/bt2_index'
bowtie2_cmd = 'bowtie2 -x ../bt2-'+SRR+'/bt2_index -1 ../fastq-data-'+SRR+'/'+SRR+'_1_trimmed.fastq -2 ../fastq-data-'+SRR+'/'+SRR+'_2_trimmed.fastq -S ../bt2-'+SRR+'/'+SRR+'.sam'

# creating the commands to take the .sam file from bt2 convert it to a .bam, sort that .bam file, and calcuate the depth
samtools_view = 'samtools view -b ../bt2-'+SRR+'/'+SRR+'.sam > ../bt2-'+SRR+'/'+SRR+'.bam'
samtools_sort = 'samtools sort ../bt2-'+SRR+'/'+SRR+'.bam -o ../bt2-'+SRR+'/sorted_'+SRR+'.bam'
samtools_cmd = 'samtools depth ../bt2-'+SRR+'/sorted_'+SRR+'.bam -o ../coverage_table-'+SRR

# calling each of the functions in order that were created above
os.system(bowtie2_index)
os.system(bowtie2_cmd)
os.system(samtools_view)
os.system(samtools_sort)
os.system(samtools_cmd)