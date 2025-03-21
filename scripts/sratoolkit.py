import subprocess 
import Bio.SeqIO as SeqIO
import os

os.makedirs('../fastq-data',exist_ok=True)
fastq_filepath = '../fastq-data'

SRR = 'SRR32805580'
download_sra = 'prefetch ' + SRR
fastqdump = 'fasterq-dump ' + SRR + ' -O ' + fastq_filepath

subprocess.run(download_sra, shell=True)
subprocess.run(fastqdump, shell=True)

os.makedirs('../spades-out',exist_ok=True)

spades_cmd = 'spades.py -1 ../fastq-data/' + SRR + '_1.fastq -2 ../fastq-data/' + SRR + '_2.fastq -o ../spades-out' 

subprocess.run(spades_cmd,shell=True)