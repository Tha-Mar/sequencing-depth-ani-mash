from Bio import SeqIO
import os

os.system('cut -f 3 ~/coverage_table > ~/depths')
with open('../depths', 'r') as f:
    depth = f.readlines()
    total = 0
    for i in depth:
        total += int(i)
    max_cov = round(total/len(depth))

step = 5
cov = 5
SRR = 'SRR32805580' # can change this to infile once we are further into the process
seqs1 = list(SeqIO.parse('../fastq-data/'+SRR+'_1.fastq', 'fastq'))
seqs2 = list(SeqIO.parse('../fastq-data/'+SRR+'_2.fastq', 'fastq'))

os.system('mkdir ../sub_samples')

for i in range(round(max_cov/step)):
    read1 = str(round(cov/max_cov*len(seqs1)))
    read2 = str(round(cov/max_cov*len(seqs2)))
    for j in range(5): # ask about when i move this into the repo how I need to change calling seqtk 
        command1 = '../seqtk/seqtk sample -s100 ../fastq-data/'+SRR+'_1.fastq '+read1+' > ../sub_samples/'+SRR+'_'+str(cov)+'_'+str(j)+'_1.fastq' # will probably want to change ecoli to the SRR number so it can change 
        command2 = '../seqtk/seqtk sample -s100 ../fastq-data/'+SRR+'_2.fastq '+read1+' > ../sub_samples/'+SRR+'_'+str(cov)+'_'+str(j)+'_2.fastq'
        os.system(command1)
        os.system(command2)
    cov += step

# after this there will be 5 pairs of fastq files for each depth in the specified file