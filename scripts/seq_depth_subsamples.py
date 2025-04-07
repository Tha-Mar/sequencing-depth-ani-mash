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

os.system('cut -f 3 ../coverage_table > ../depths')
with open('../depths', 'r') as f:
    depth = f.readlines()
    total = 0
    for i in depth:
        total += int(i)
    max_cov = round(total/len(depth))

step = 5
cov = 5
seqs1 = list(SeqIO.parse('../fastq-data/'+SRR+'_1.fastq', 'fastq'))
seqs2 = list(SeqIO.parse('../fastq-data/'+SRR+'_2.fastq', 'fastq'))

os.system('mkdir ../sub_samples')
seeds = ['100', '3', '44']

for i in range(round(max_cov/step)):
    read1 = str(round(cov/max_cov*len(seqs1)))
    read2 = str(round(cov/max_cov*len(seqs2)))
    for j in range(3): # ask about when i move this into the repo how I need to change calling seqtk 
        command1 = '../seqtk/seqtk sample -s'+seeds[j]+' ../fastq-data/'+SRR+'_1.fastq '+read1+' > ../sub_samples/'+SRR+'_'+str(cov)+'_'+str(j)+'_1.fastq' # will probably want to change ecoli to the SRR number so it can change 
        command2 = '../seqtk/seqtk sample -s'+seeds[j]+' ../fastq-data/'+SRR+'_2.fastq '+read2+' > ../sub_samples/'+SRR+'_'+str(cov)+'_'+str(j)+'_2.fastq'
        os.system(command1)
        os.system(command2)
    cov += step

# after this there will be 5 pairs of fastq files for each depth in the specified file

#Create a new directory to store QC'd subsamples
os.system('mkdir ../sub_samples_trimmed')


#QC subsamples

# Loop through all FASTQ files in the input directory
for file in os.listdir('../sub_samples/'):
    basename = file[:-6]   
    sub_cutadapt= 'cutadapt -q 20 -o ../sub_samples_trimmed/' + basename + '_trimmed.fastq ../sub_samples/'  + file
    os.system(sub_cutadapt)
    
