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

#create a directory for spades output 
os.makedirs('../spades-out',exist_ok=True)

#spades assembly command 
spades_cmd = 'spades.py -1 ../fastq-data/' + SRR + '_1.fastq -2 ../fastq-data/' + SRR + '_2.fastq -o ../spades-out' 

#run spades command in the command line
subprocess.run(spades_cmd,shell=True)

