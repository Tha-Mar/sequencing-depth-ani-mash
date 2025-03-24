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

#Run script to download SRR fastq files and assemble with SPAdes
os.system(f"python ./scripts/sratoolkit.py --input {infile}")
os.system(f"python ./scripts/bt2.py --input {infile}")
os.system(f'python ./scripts/seq_depth_subsamples.py --input {infile}')







