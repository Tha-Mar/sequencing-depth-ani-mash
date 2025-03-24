import os
# below I use the argparse function from the start_argparse.py file we were given

'''import sys
import argparse

#function to parse command line arguments
def check_arg(args=None):
    parser = argparse.ArgumentParser(description="ADD TITLE OF SCRIPT HERE (shows on help)")
    parser.add_argument("-i", "--input",
    help="input file",
    required=True)
    parser.add_argument("-o", "--output",
    help="output file",
    required=True)
    return parser.parse_args(args)

#retrieve command line arguments
arguments = check_arg(sys.argv[1:])
infile = arguments.input
outfile = arguments.output'''

os.system('mkdir ../bt2')
bowtie2_index = 'bowtie2-build ../spades-out/contigs.fasta ../bt2/bt2_index'
bowtie2_cmd = 'bowtie2 -x ../bt2/bt2_index -1 ../fastq-data/SRR32805580_1.fastq -2 ../fastq-data/SRR32805580_2.fastq -S ../bt2/SRR32805580.sam'

samtools_view = 'samtools view -b ../bt2/SRR32805580.sam > ../bt2/SRR32805580.bam'
samtools_cmd = 'samtools coverage -b ../bt2/SRR32805580.bam -o ../coverage_table'

os.system(bowtie2_index)
os.system(bowtie2_cmd)
os.system(samtools_view)
os.system(samtools_cmd)