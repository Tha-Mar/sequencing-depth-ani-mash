from Bio import SeqIO
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

# creating SRR variable so the script runs on the given SRA accession number 
SRR = infile

# extracting the 3rd column from the coverage table that was produced in bt2.py to get all seq depth values
os.system('cut -f 3 ../coverage_table-'+SRR+' > ../depths-'+SRR)

# opening up the new file with just the values and calculating the average coverage for the whole sequence
with open('../depths-'+SRR, 'r') as f:
    depth = f.readlines()
    total = 0
    for i in depth:
        total += int(i)
    max_cov = round(total/len(depth)) # max_coverage represents the highest covereage that the simulated genomes will have

# setting step value and starting coverage value
step = 5 
cov = 5

# using SeqIO to get the total number of reads 
seqs1 = list(SeqIO.parse('../fastq-data-'+SRR+'/'+SRR+'_1.fastq', 'fastq'))
seqs2 = list(SeqIO.parse('../fastq-data-'+SRR+'/'+SRR+'_2.fastq', 'fastq'))

# making a directory to hold the subsampled reads
os.system('mkdir ../sub_samples-'+SRR)

# 3 different seeds for the 3 different subsamples that will be created at each simulated depth
seeds = ['100', '3', '44']

# This loops through all of the sequencing depths that need to be created 
for i in range(round(max_cov/step)):
    # read 1 and read 2 are the number of reads that need to be extracted from the full fastq file to get the correct coverage
    read1 = str(round(cov/max_cov*len(seqs1)))
    read2 = str(round(cov/max_cov*len(seqs2)))
    # looping through 3 times for each coverage 
    for j in range(3): 
        # following commands use seqtk to extract the specified number of reads randomly (given the seeds provided) and output them to new fastq files
        command1 = '../seqtk/seqtk sample -s'+seeds[j]+' ../fastq-data-'+SRR+'/'+SRR+'_1.fastq '+read1+' > ../sub_samples-'+SRR+'/'+SRR+'_'+str(cov)+'_'+str(j)+'_1.fastq'  
        command2 = '../seqtk/seqtk sample -s'+seeds[j]+' ../fastq-data-'+SRR+'/'+SRR+'_2.fastq '+read2+' > ../sub_samples-'+SRR+'/'+SRR+'_'+str(cov)+'_'+str(j)+'_2.fastq'
        os.system(command1)
        os.system(command2)
    cov += step


#Create a new directory to store QC'd subsamples
os.system('mkdir ../ss_trimmed-'+SRR)


#QC subsamples

# Loop through all FASTQ files in the input directory
for file in os.listdir('../sub_samples-'+SRR+'/'):
    basename = file[:-6]   
    sub_cutadapt= 'cutadapt -q 20 -o ../ss_trimmed-'+SRR+'/' + basename + '_trimmed.fastq ../sub_samples-'+SRR+'/'  + file
    os.system(sub_cutadapt)
    
