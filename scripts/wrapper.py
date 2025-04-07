import os 
import logging
import argparse
import sys


#function to parse command line arguments
def check_arg(args=None):
    parser = argparse.ArgumentParser(description='input location of data directory')
    parser.add_argument('-i', '--input', help='path to input data',required ='True') #add command line arguement for input file
    return parser.parse_args(args)

#retrieve command line arguments and assign to variables
args = check_arg(sys.argv[1:])
infile = args.input #store input SRR#

#Move into scripts directory
os.chdir("./scripts")

#Run script to download SRR fastq files and assemble with SPAdes
os.system(f"python sratoolkit.py --input {infile}")
os.system(f"python bt2.py --input {infile}")
os.system(f'python seq_depth_subsamples.py --input {infile}')
os.system(f'python assembly.py --input {infile}')
os.system(f'python fastani-mash.py --input {infile}')
os.system('Rscript visuals.R')





