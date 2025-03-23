from Bio import SeqIO
import os

# max_cov = will have to get it from samtools coverage from bam file from assembly 
max_cov = 10 # need to write a command using samtools to get the full coverage 
step = 5
cov = 5
SRR = 'SRR13921543' # can change this to infile once we are further into the process
seqs1 = list(SeqIO.parse(SRR+'_1.fastq', 'fastq'))
seqs2 = list(SeqIO.parse(SRR+'_2.fastq', 'fastq'))

for i in range(int(max_cov/step)):
    read1 = str(round(cov/max_cov*len(seqs1)))
    read2 = str(round(cov/max_cov*len(seqs2)))
    for j in range(5): # ask about when i move this into the repo how I need to change calling seqtk 
        command1 = '../../seqtk/seqtk sample -s100 '+SRR+'_1.fastq '+read1+' > test_cov_depths/ecoli_'+str(cov)+'_'+str(j)+'_1.fastq' # will probably want to change ecoli to the SRR number so it can change 
        command2 = '../../seqtk/seqtk sample -s100 '+SRR+'_2.fastq '+read1+' > test_cov_depths/ecoli_'+str(cov)+'_'+str(j)+'_2.fastq'
        os.system(command1)
        os.system(command2)
    cov += step

# after this there will be 5 pairs of fastq files for each depth in the specified file