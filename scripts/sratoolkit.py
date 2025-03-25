import subprocess 
import Bio.SeqIO as SeqIO
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

#prefetch and fastq dump commands 
download_sra = 'prefetch ' + SRR
fastqdump = 'fasterq-dump ' + SRR + ' -O ' + fastq_filepath


#run commands in the command line
subprocess.run(download_sra, shell=True)
subprocess.run(fastqdump, shell=True)

#QC the reads commands
cutadapt1 = 'cutadapt -q 20 -o ../fastq-data/' + SRR + '_1_trimmed.fastq ../fastq-data/'  + SRR + '_1.fastq'
FastQC1 = 'fastqc ../fastq-data/' + SRR + '_1_trimmed.fastq -o ../fastqc-out -f fastq'
cutadapt2 = 'cutadapt -q 20 -o ../fastq-data/' + SRR + '_2_trimmed.fastq ../fastq-data/'  + SRR + '_2.fastq'
FastQC2 = 'fastqc ../fastq-data/' + SRR + '_2_trimmed.fastq -o ../fastqc-out -f fastq'


#Create directory to store FastQC files
os.makedirs('../fastqc-out',exist_ok=True)

#Run QC commands
subprocess.run(cutadapt1, shell=True)
subprocess.run(FastQC1, shell=True)
subprocess.run(cutadapt2, shell=True)
subprocess.run(FastQC2, shell=True)


#create a directory for spades output 
os.makedirs('../spades-out',exist_ok=True)

#spades assembly command 
spades_cmd = 'spades.py -1 ../fastq-data/' + SRR + '_1_trimmed.fastq -2 ../fastq-data/' + SRR + '_2_trimmed.fastq -o ../spades-out' 

#run spades command in the command line
subprocess.run(spades_cmd,shell=True)

