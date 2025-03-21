import subprocess 
import Bio.SeqIO as SeqIO
import os

#create directory for fastq files 
os.makedirs('../fastq-data',exist_ok=True) 
fastq_filepath = '../fastq-data'

SRR = 'SRR32805580' #SRR chosen by user 

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