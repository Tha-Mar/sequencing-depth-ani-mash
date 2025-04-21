import os
import glob
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

# creating SRR variable so the file paths reflect the user specified SRA 
SRR = infile

# creating a list of the paths for the trimmed simulated reads
reads = glob.glob('../ss_trimmed-'+SRR+'/'+SRR+'_*_*_1_trimmed.fastq')

# for each of the read pairs in the list ...
for read in reads:
    # assemble the reads using spades 
    file = os.path.basename(read)
    spades_cmd = 'spades.py -1 '+read+' -2 '+read[:-15]+'2_trimmed.fastq -o ../sub_assemblies-'+SRR+'/'+file[:-16]
    os.system(spades_cmd)