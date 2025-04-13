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

SRR = infile

os.system('cut -f 3 ../coverage_table-'+SRR+' > ../depths-'+SRR)
with open('../depths-'+SRR, 'r') as f:
    depth = f.readlines()
    total = 0
    for i in depth:
        total += int(i)
    max_cov = round(total/len(depth))

step = 5
cov = 5
seqs1 = list(SeqIO.parse('../fastq-data-'+SRR+'/'+SRR+'_1.fastq', 'fastq'))
seqs2 = list(SeqIO.parse('../fastq-data-'+SRR+'/'+SRR+'_2.fastq', 'fastq'))

os.system('mkdir ../sub_samples-'+SRR)
seeds = ['100', '3', '44']

for i in range(round(max_cov/step)):
    read1 = str(round(cov/max_cov*len(seqs1)))
    read2 = str(round(cov/max_cov*len(seqs2)))
    for j in range(3): 
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
    
