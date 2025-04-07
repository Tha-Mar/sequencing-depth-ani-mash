import subprocess 
import Bio
import Bio.SeqIO as SeqIO
import os


#create directory for fastq files 
os.makedirs('../fastq-data',exist_ok=True) 
fastq_filepath = '../fastq-data'

SRR = "SRR32805580"

#prefetch and fastq dump commands 
download_sra = 'prefetch ' + SRR
fastqdump = 'fasterq-dump ' + SRR + ' -O ' + fastq_filepath

#run commands in the command line
subprocess.run(download_sra, shell=True)
subprocess.run(fastqdump, shell=True)

#Shorten fastq files for testing
command1 = '../seqtk/seqtk sample -s1 ../fastq-data/'+SRR+'_1.fastq 285000 > ../fastq-data/'+SRR+'_1_test.fastq'
command2 = '../seqtk/seqtk sample -s1 ../fastq-data/'+SRR+'_2.fastq 285000 > ../fastq-data/'+SRR+'_2_test.fastq'

subprocess.run(command1, shell=True)
subprocess.run(command2,shell=True)


#QC the reads commands
cutadapt1 = 'cutadapt -q 20 -o ../fastq-data/' + SRR + '_1_trimmed.fastq ../fastq-data/'  + SRR + '_1_test.fastq'
FastQC1 = 'fastqc ../fastq-data/' + SRR + '_1_trimmed.fastq -o ../fastqc-out -f fastq'
cutadapt2 = 'cutadapt -q 20 -o ../fastq-data/' + SRR + '_2_trimmed.fastq ../fastq-data/'  + SRR + '_2_test.fastq'
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
