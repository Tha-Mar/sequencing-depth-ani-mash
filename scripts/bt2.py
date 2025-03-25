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

#create directory for fastq files 
os.makedirs('../fastq-data',exist_ok=True) 
fastq_filepath = '../fastq-data'

SRR = infile

os.system('mkdir ../bt2')
bowtie2_index = 'bowtie2-build ../spades-out/contigs.fasta ~/bt2/bt2_index'
bowtie2_cmd = 'bowtie2 -x ../bt2/bt2_index -1 ../fastq-data/'+SRR+'_1_trimmed.fastq -2 ../fastq-data/'+SRR+'_2_trimmed.fastq -S ../bt2/'+SRR+'.sam'

samtools_view = 'samtools view -b ../bt2/'+SRR+'.sam > ../bt2/'+SRR+'.bam'
samtools_sort = 'samtools sort ../bt2/'+SRR+'.bam -o ../bt2/sorted_'+SRR+'.bam'
samtools_cmd = 'samtools depth ../bt2/sorted_'+SRR+'.bam -o ../coverage_table '

os.system(bowtie2_index)
os.system(bowtie2_cmd)
os.system(samtools_view)
os.system(samtools_sort)
os.system(samtools_cmd)